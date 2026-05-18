#!/usr/bin/env python3
import argparse
import base64
import datetime as dt
import hashlib
import json
import os
import sys
import uuid
import zipfile


HASH_ALGS = [
    ("MD5", hashlib.md5),
    ("SHA-1", hashlib.sha1),
    ("SHA-256", hashlib.sha256),
    ("SHA-384", hashlib.sha384),
    ("SHA-512", hashlib.sha512),
]


def _utc_now_iso() -> str:
    return dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def _file_hashes(path: str):
    hs = [(name, fn()) for name, fn in HASH_ALGS]
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            for _, h in hs:
                h.update(chunk)
    return [{"alg": name, "content": h.hexdigest()} for name, h in hs]


def _safe_purl_generic(name: str, version: str | None, qualifier_type: str):
    # Keep it simple and valid-ish; avoid spaces and slashes.
    n = "".join(c if c.isalnum() or c in (".", "_", "-") else "-" for c in name).strip("-") or "component"
    v = version or "unspecified"
    return f"pkg:generic/{n}@{v}?type={qualifier_type}"


def _mk_component(name: str, version: str | None, purl: str, bom_ref: str, hashes, ctype="library"):
    return {
        "type": ctype,
        "name": name,
        "version": version or "unspecified",
        "purl": purl,
        "bom-ref": bom_ref,
        "hashes": hashes,
        "modified": False,
    }


def generate(aar_path: str, out_path: str, group: str, name: str, version: str, debug: bool):
    if not os.path.isfile(aar_path):
        raise FileNotFoundError(f"AAR not found: {aar_path}")

    tmp_dir = os.path.join(os.path.dirname(out_path), f".bomtmp_{uuid.uuid4().hex}")
    os.makedirs(tmp_dir, exist_ok=True)
    extracted = []

    try:
        if debug:
            print(f"[debug] Reading AAR: {aar_path}")
        with zipfile.ZipFile(aar_path, "r") as z:
            for zi in z.infolist():
                # Focus on jar payloads for BOM components
                if zi.filename.endswith(".jar"):
                    dest = os.path.join(tmp_dir, os.path.basename(zi.filename))
                    with z.open(zi, "r") as src, open(dest, "wb") as dst:
                        dst.write(src.read())
                    extracted.append((zi.filename, dest))
                    if debug:
                        print(f"[debug] Extracted: {zi.filename} -> {dest} ({os.path.getsize(dest)} bytes)")

        serial = f"urn:uuid:{uuid.uuid4()}"
        root_purl = f"pkg:maven/{group}/{name}@{version}?type=aar"
        root_ref = root_purl

        components = []
        dependencies = [{"ref": root_ref, "dependsOn": []}]

        for internal_name, path in sorted(extracted, key=lambda x: x[0]):
            fname = os.path.basename(internal_name)
            comp_name = fname[:-4] if fname.lower().endswith(".jar") else fname
            comp_purl = _safe_purl_generic(comp_name, None, "jar")
            comp_ref = comp_purl
            h = _file_hashes(path)
            components.append(_mk_component(comp_name, None, comp_purl, comp_ref, h, ctype="library"))
            dependencies[0]["dependsOn"].append(comp_ref)
            dependencies.append({"ref": comp_ref, "dependsOn": []})

        bom = {
            "bomFormat": "CycloneDX",
            "specVersion": "1.4",
            "serialNumber": serial,
            "version": 1,
            "metadata": {
                "timestamp": _utc_now_iso(),
                "tools": [
                    {
                        "vendor": "Mint",
                        "name": "generate_bom_from_aar.py",
                        "version": "1.0.0",
                    }
                ],
                "component": {
                    "type": "library",
                    "group": group,
                    "name": name,
                    "version": version,
                    "purl": root_purl,
                    "bom-ref": root_ref,
                },
            },
            "components": components,
            "dependencies": dependencies,
        }

        os.makedirs(os.path.dirname(out_path) or ".", exist_ok=True)
        with open(out_path, "w", encoding="utf-8") as f:
            json.dump(bom, f, indent=2, sort_keys=False)
            f.write("\n")

        if debug:
            print(f"[debug] Wrote BOM: {out_path}")
            print(f"[debug] Components: {len(components)} (jar payloads found in AAR)")
    finally:
        # Best-effort cleanup
        try:
            for _, p in extracted:
                os.remove(p)
            os.rmdir(tmp_dir)
        except Exception:
            pass


def main():
    ap = argparse.ArgumentParser(description="Generate CycloneDX 1.4 BOM from an Android AAR payload.")
    ap.add_argument("--aar", required=True, help="Path to .aar file")
    ap.add_argument("--out", required=True, help="Output BOM json path")
    ap.add_argument("--group", required=True, help="Group ID for root component (maven style)")
    ap.add_argument("--name", required=True, help="Artifact ID / name for root component")
    ap.add_argument("--version", required=True, help="Version for root component")
    ap.add_argument("--debug", action="store_true", help="Print debug logs")
    args = ap.parse_args()
    generate(args.aar, args.out, args.group, args.name, args.version, args.debug)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"[error] {e}", file=sys.stderr)
        sys.exit(2)

