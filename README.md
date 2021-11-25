# Python-ADB-Wrapper
A wrapper script to make working with ADB (Android Debug Bridge) easier

This project was just a simple test to see if I could wrap some adb stuff in Python (and even automate backups via a list of strings/apps for example).

I had some issues understanding the different license types, but to keep it simple: This Project is **freely licensed / public domain?** -> **You can do whatever you want** with it, no credits, no asking etc... Do what you want.

Upon startup / import, you'll be asked to set the ADB Path. If you don't want that, simply set the path in the script yourself and save it / deleted the rest of the path thing at the top. I trust that you are smart enough to handle this basic first step if your goal is to modify and reuse the code. If not, simply input your desired option.

The Script is kept as simple and the imports as short / low as possible (Only 1 -> Subprocess)

### Function List
  - execute(command, deviceID):
  - execute(command):
  - selectDevice(deviceID):
  - listDevices():
  - listApps(appType="thirdparty", listPath=False):
  - listApps(listPath=False):
  - listFeatures():
  - listLibraries():
  - getFullAppName(app):
  - getFullAppPath(app):
  - backupAPK(appName):
  - backupAPKList(appNameList):
  - backupOBB(appName):
  - backupOBBList(appNameList):
  - backupFullApp(appName):
  - backupFullAppList(appNameList):
## Notes:
  - execute exists twice in case you want to use a specific device id, regular execute with auto choose       your connected android device.
  - execute is not just used mainly in the code by other functions. It can also be used by you in order  to run a specific adb code, just in case.
  - listApps has multiple options, default being no params => Displays/returns a list of your regular (called third party excl. system apps) apps. If you set listPath to True, you'll receive the full complete path (with "cryptic" letters etc..., default = False)
  - backupAPK backups APK in the current folder where the script is being ran.
    - DO NOTE, sometimes the functions will say something about "NoneType". This issue should be fixed (renamed the overloaded function with list as param). Though if it does happen, it means probably that it couldn't find an app with that name.
  - backupOBB works now (updated)
  - backupFullApp works now (updated).
