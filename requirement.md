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

 git tag v2.2.0 && git push origin v2.2.0

deploy on production directly 
./gradlew publishReleasePublicationToGitHubPackagesRepository

 ./gradlew publishReleasePublicationToMavenLocal
 
  ./gradlew publishReleasePublicationToGitHubPackagesRepository
