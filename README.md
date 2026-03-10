# MINT SDK Gradle Configuration Guide



[![GitHub Packages](https://img.shields.io/badge/GitHub%20Packages-MINT%20SDK-brightgreen?style=flat-square&logo=github)](https://github.com/orgs/investwell-tools/packages?repo_name=mint-android-app)

![Packages](https://img.shields.io/badge/packages-published-green?style=flat-square&logo=github)




This document provides step-by-step instructions to configure your Android project to use the **MINT SDK** from Investwell Tools' private GitHub Packages repository.

## Table of Contents
- [Prerequisites](#prerequisites)
- [Step 1: Configure gradle.properties](#step-1-configure-gradleproperties)
- [Step 2: Update settings.gradle.kts](#step-2-update-settingsgradle-kts)
- [Step 3: Add MINT SDK Dependency](#step-3-add-mint-sdk-dependency)
- [Verification](#verification)
- [Security Best Practices](#security-best-practices)
- [Troubleshooting](#troubleshooting)

## Prerequisites
- Android Studio with Gradle
- GitHub account with access to `investwell-tools/mint-android-app` repository
- GitHub Personal Access Token (PAT) with `read:packages` scope

## Step 1: Configure gradle.properties

Add the following lines to your project's root `gradle.properties` file:

```properties
# GitHub Packages credentials for MINT SDK
gpr.user=laxmikant86
gpr.key=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

```
> **⚠️ SECURITY**: Never commit `gradle.properties` with credentials to version control. Add it to `.gitignore`.

```

## Step 2: Update settings.gradle.kts

Configure the private Maven repository in your `settings.gradle.kts`:

```kotlin
dependencyResolutionManagement {
    repositoriesMode.set(RepositoriesMode.FAIL_ON_PROJECT_REPOS)
    repositories {
        google()
        mavenCentral()
        
        // MINT SDK - Investwell Tools GitHub Packages
        maven {
            url = uri("https://maven.pkg.github.com/investwell-tools/mint-android-app")
            credentials {
                username = providers.gradleProperty("gpr.user").orNull
                password = providers.gradleProperty("gpr.key").orNull
            }
        }
    }
}
```

## Step 3: Add MINT SDK Dependency

In your **module-level** `build.gradle.kts` (app module), add:

```kotlin
dependencies {
    // MINT SDK (replace with actual version)
    implementation("com.investwell.mint:mint-sdk:X.X.X")
    
    // Other dependencies...
}
```

## Verification

1. **Sync Project**: File → Sync Project with Gradle Files
2. **Clean Build**: `./gradlew clean build`
3. **Check Dependencies**: `./gradlew app:dependencies`

## Security Best Practices

| Practice | Description |
|----------|-------------|
| `.gitignore` | Add `gradle.properties` to `.gitignore` |
| Environment Variables | Use `GITHUB_USER` and `GITHUB_TOKEN` in CI |
| Scoped Tokens | Use PAT with minimal required scopes |
| Local Only | Keep credentials local during development |

## Troubleshooting

### Common Issues

| Issue | Solution |
|-------|----------|
| `401 Unauthorized` | Verify `gpr.user` and `gpr.key` |
| `Repository not found` | Check repository URL and access |
| `Sync failed` | Invalidate caches and restart Android Studio |
| `Dependency not found` | Verify artifact coordinates and version |

### Debug Commands
```bash
# Check repository access
./gradlew build --stacktrace --info

# List all dependencies
./gradlew app:dependencies --configuration implementation
```

---
*Document Version: 2.1.7aar | Last Updated: March 2026*