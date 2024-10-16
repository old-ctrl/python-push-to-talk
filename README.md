# python push-to-talk for roblox

a simple python script for push-to-talk using `ctypes`. roblox doesn't have push-to-talk (which is honestly ridiculous), so this script does the job. the default key is **"j"**, but you can change it up.

## features

- mutes your mic by default, unmutes when you hold down the key.
- customizable push-to-talk key (default: **"j"**).
- uses `ctypes` to control the mic and `keyboard` to detect key presses.

## setup

1. make sure you’ve got python 3.x installed.
2. install the `keyboard` library:
   ```bash
   pip install keyboard
