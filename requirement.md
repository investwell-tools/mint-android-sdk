project-root
│
├── gradlew
├── gradlew.bat
├── gradle
│   └── wrapper
│       ├── gradle-wrapper.jar
│       └── gradle-wrapper.properties
│
├── build.gradle
├── settings.gradle
├── gradle.properties
└── libs
    └── mint-2.1.7.aar


## choose your publishing house 

JitPack
or
Maven Central



## Then give permission:
chmod +x gradlew
 then run 
 ./gradlew publish

 ## check your project root 

 gradlew
gradlew.bat
gradle/wrapper/gradle-wrapper.jar
gradle/wrapper/gradle-wrapper.properties

## Run this in your project:
./gradlew publish

or run 

chmod +x gradlew
./gradlew publish

## check after deployment success 

implementation("com.github.investwell-tools:mint-sdk:2.1.7")


## before publishing docs need to build and generate site

export GITHUB_TOKEN=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

 GITHUB_USER=laxmikant86
 GITHUB_TOKEN=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

 ./gradlew publishReleasePublicationToMavenLocal
 
  ./gradlew publishReleasePublicationToGitHubPackagesRepository
