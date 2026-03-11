# Mint Android SDK

Investwell offers native Android, iOS and Flutter software development kit (SDK) that facilitates seamless integration with any MFD partner platform application developed using these technologies. This SDK provides the complete features of Investwell Mint including Portfolio performance report, online transaction and scheme analytics. This enables a streamlined end-to-end experience.

Version: 2.1.7 | Updated on 11th Mar, 2026
The Investwell Android SDK is published on Jitpack so it is mandatory to install the Jitpack package:

[2.1.7 (New)](versions/2.1.7.md)

[2.1.4](versions/2.1.4.md)

* Step 1. Add the JitPack repository to your build file. Add it in your root build.gradle at the end of repositories:

```Groovy

allprojects {
  repositories {
maven { url 'https://www.jitpack.io' }
  }
}

```

* Step 2. After adding jitpack dependency add the Investwell SDK dependency in the build.gradle of your app folder.

```Groovy

implementation("com.github.investwell-tools:mint-android-sdk:2.1.7")

```

* Step 3. Add for kotlin DSL root/settings.gradle.kts

```
dependencyResolutionManagement {
    repositories {
        google()
        mavenCentral()
        maven {
            url = uri("https://maven.pkg.github.com/investwell-tools/mint-android-sdk")
        }
    }
}


```
* Step 3. Add for groovy root/settings.gradle

```
dependencyResolutionManagement {
    repositories {
        google()
        mavenCentral()
        maven {
            url = uri("https://maven.pkg.github.com/investwell-tools/mint-android-sdk")
        }
    }
}
```

## Mint SSO Implementation:

**Download Sample Code (Flutter Android Module):**  
[Download from Google Drive](https://drive.google.com/file/d/1fobwGoiZFsThqgrK7A-REn_Lf7akR3NA/view?usp=sharing)


## Step 1:
Add in your manifest file required

**For Native Apps**
Instead of Application extend AppApplication
For **flutter** required to mention it in your Android Manifest file

```
android:allowBackup="false"
tools:replace="android:allowBackup"
android:dataExtractionRules="@xml/data_extraction_rules"
android:name="investwell.activity.AppApplication"
```

***Note:***  In the case of already you have an application class **Example:**

```
         android:allowBackup="true"
        android:dataExtractionRules="@xml/data_extraction_rules"
        android:fullBackupContent="@xml/backup_rules"
        android:icon="@mipmap/ic_launcher"
        android:label="@string/app_name"
        android:name=".DemoApp"
        android:roundIcon="@mipmap/ic_launcher_round"
        android:supportsRtl="true"
        android:theme="@style/Theme.MintSample"
        tools:replace="android:theme,android:allowBackup,android:name"
        tools:targetApi="31" >
        
```
## **Application class**

**Java**
```
public class DemoApp extends AppApplication {
    @Override
    public void onCreate() {
        super.onCreate();
    }
}
```

**Kotlin**
```
class DemoApp : AppApplication {
    @Override
    public void onCreate() {
        super.onCreate();
    }
}

```

## Follow the Documentation to generate SSO Token
**Step 2:**  Pass the ssoToken, fcmToken,classNameWithPackage
Example:

```Kotlin

/** looks like
*ssoToken = 8ff7b6dddb12407dcd0cb3d1fcdabee60b6107863019725689705b587ebb817a
*fcmToken =  your_app_fcmToken
*classWithPackage = “com.example.sample.ManiActivity”
**/
private fun invokeSDK(
    sso: String,
    fcmToken:String,
    domain:String,
    classWithPackage:String= "${this@MainActivity.packageName}.MainActivity"
    ){
        val mintSdk = MintSDK(this@MainActivity)
       mintSdk.configureSDK(true)
       // set enviroment for release true, false for debug 
            mintSDK.setIsProduction(true);
        minced.invokeMintSDK(sso,fcmToken,domain,classWithPackage)
    }

```

**Tips:** In case of getting Android Manifest error add

```
tools:replace="android:resource

```

**Note:** If you wanna use Mint login screen
Mint SDK Login Form:


```Kotlin
MintSDK mintSDK= new MintSDK(this);
            mintSDK.configureSDK(true);
            // set enviroment for release true, false for debug 
            mintSDK.setIsProduction(true);
            mintSDK.mintLogin("spvithlani","your_app_fcm_token");

```

## add your app colors

```xml
<color name="colorPrimary">#009477</color>
<color name="colorPrimaryDark">#00574B</color>
<color name="colorAccent">#FF02D594</color>
<color name="colorToolbar">#009477</color>

```

***Note:*** Color code only hex code accepted
Before generating the **getAuthorizationToken** we have to check whether the is SDK already auth-validated or not
**isAuthValidated** allows us to keep the login data for 10 minutes only if **isAuthValidated** is false then call the getAuthorizationToken API

```
if (!mintSDK.isAuthValidated()){
// call authkey api for ssoToken 
                callGeneratauth("broker");
            }
```


***Tips:*** call ***clearSDKData()*** before logout your app 

```
  mintSDK.clearSDKData();
```


## Features

- Easy integration
- Secure APIs
- Analytics support
- Java & Kotlin compatible