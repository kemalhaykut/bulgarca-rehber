# -*- coding: utf-8 -*-
"""CI: 'flutter create' sonrası Android ayarlarını düzenler."""
import re, pathlib

man = pathlib.Path("android/app/src/main/AndroidManifest.xml")
s = man.read_text(encoding="utf-8")
s = re.sub(r'android:label="[^"]*"', 'android:label="Bulgarca Rehber"', s, count=1)
if "android.permission.INTERNET" not in s:
    s = s.replace("<application", '<uses-permission android:name="android.permission.INTERNET" />\n    <application', 1)
man.write_text(s, encoding="utf-8")

# webview_flutter en az Android 7 (API 24) ister
for name in ["android/app/build.gradle.kts", "android/app/build.gradle"]:
    p = pathlib.Path(name)
    if p.exists():
        g = p.read_text(encoding="utf-8")
        g = re.sub(r'minSdk\s*=\s*flutter\.minSdkVersion', 'minSdk = 24', g)
        g = re.sub(r'minSdkVersion\s+flutter\.minSdkVersion', 'minSdkVersion 24', g)
        # Yayın derlemesinde Android "lint" denetimi çöküyor; APK için gerekli değil, kapatıyoruz.
        if "checkReleaseBuilds" not in g:
            if name.endswith(".kts"):
                block = "android {\n    lint {\n        checkReleaseBuilds = false\n        abortOnError = false\n    }\n"
            else:
                block = "android {\n    lintOptions {\n        checkReleaseBuilds false\n        abortOnError false\n    }\n"
            g = g.replace("android {\n", block, 1)
        p.write_text(g, encoding="utf-8")
        print("minSdk 24:", name)
print("AndroidManifest güncellendi")
