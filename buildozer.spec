[app]

# App Metadata
title = RoyalWinAI
package.name = royalwinai
package.domain = org.royalwin.ai
version = 1.0

# Project Structure
source.dir = .
source.include_exts = py,png,jpg,kv,json
# Entry point
entrypoint = app.py.py

# Icon
icon.filename = icon.png

# Orientation
orientation = portrait

# Permissions
android.permissions = INTERNET

# Android Configuration
android.api = 33
android.minapi = 21
android.ndk = 25b
android.accept_sdk_license = True
android.build_tools_version = 33.0.0
android.archs = armeabi-v7a, arm64-v8a

# Requirements
requirements = python3,kivy

# Android extras
android.entrypoint = org.kivy.android.PythonActivity
android.apptheme = @android:style/Theme.NoTitleBar
android.bootstrap = sdl2
enable_androidx = 1

# Debug & Packaging
copy_libs = 1
log_level = 2
