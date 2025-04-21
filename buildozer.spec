[app]

title = RoyalWinAI
package.name = royalwinai
package.domain = org.royalwin.ai

source.dir = app
source.include_exts = py,png,jpg,kv,json

version = 1.0
requirements = python3,kivy

icon.filename = %(source.dir)s/icon.png

orientation = portrait
android.permissions = INTERNET

android.api = 33
android.minapi = 21
android.ndk = 25b
android.accept_sdk_license = True
android.build_tools_version = 33.0.0
android.archs = armeabi-v7a,arm64-v8a

copy_libs = 1
log_level = 2
