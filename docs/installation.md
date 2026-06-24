# Mint SDK Gradle Implementation

The Investwell Android SDK is published on **JitPack**. JitPack’s standard setup is to add its repository in Gradle and then declare the library dependency. 

---

## Step 1: Add Repository

Add JitPack to your root-level Gradle configuration.

### Kotlin DSL (`settings.gradle.kts`)
```kotlin
dependencyResolutionManagement {
    repositoriesMode.set(RepositoriesMode.FAIL_ON_PROJECT_REPOS)
    repositories {
        google()
        mavenCentral()
        maven(url = uri("https://jitpack.io"))
    }
}
```

### Groovy DSL (`build.gradle`)
```gradle
repositories {
    maven { url 'https://jitpack.io' }
}
```

## Step 2: Add the dependency

Use the deprecated old SDK dependency in your app module:

### Kotlin DSL (`build.gradle.kts`)
```kotlin
dependencies {
    implementation("com.github.investwell-tools:mint-android-app:2.1.7")
}
```

### Groovy DSL (`build.gradle`)
```gradle
dependencies {
    implementation 'com.github.investwell-tools:mint-android-app:2.1.7'
}
```

## Notes

- This setup is for the **older deprecated SDK version**.
- Make sure the JitPack repository is available before adding the dependency.
- If your project already centralizes repositories in `settings.gradle.kts`, prefer adding JitPack there instead of module-level `repositories`. Gradle’s newer repository management flow recommends centralizing repositories in settings. 