[app]

# App Metadata
title = RoyalWinAI
package.name = royalwinai
package.domain = org.royalwin.ai
version = 1.0

# Project Structure
source.dir = .
source.include_exts = py,png,jpg,kv,json
# Entry point must be main.py in this directory
# (make sure your main.py file exists here)

# Icon
icon.filename = %(source.dir)s/icon.png

# Orientation
orientation = portrait

# Permissions
android.permissions = INTERNET

# Supported Android Versions
android.api = 33
android.minapi = 21
android.ndk = 25b
android.accept_sdk_license = True
android.build_tools_version = 33.0.0

# Architectures
android.archs = armeabi-v7a, arm64-v8a

# Requirements
requirements = python3,kivy

# Debugging
log_level = 2
copy_libs = 1

# Theme and Bootstrap
android.entrypoint = org.kivy.android.PythonActivity
android.apptheme = @android:style/Theme.NoTitleBar
android.bootstrap = sdl2

# Misc
enable_androidx = 1
