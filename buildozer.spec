[app]

title = RoyalWinAI
package.name = royalwinai
package.domain = org.royalwin.ai
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json
version = 1.0
requirements = python3,kivy
orientation = portrait
fullscreen = 1

# (Optional) Icon - add your own PNG later
icon.filename = icon.png

# Entry point
entrypoint = main.py

# Android permissions
android.permissions = INTERNET

# Supported architectures
android.archs = armeabi-v7a, arm64-v8a

# Package format
android.api = 33
android.minapi = 21
android.ndk = 25b
android.sdk = 24
android.ndk_path = 
android.sdk_path = 

# Optimization
android.enable_androidx = 1
android.gradle_dependencies = androidx.appcompat:appcompat:1.2.0

# Keep .pyc files
copy_libs = 1

# Logging
log_level = 2
