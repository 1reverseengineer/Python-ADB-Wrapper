import subprocess
adb_path = ""
deviceID = ""
hasPathADB = False
adb_path_in = input("PATH to ADB Options:\n[1] auto (checks local appdata)\n[2] manually?\n[3] Already works via PATH\n\nOption: ")
if(int(adb_path_in) == 1):
    adb_path = "%localappdata%/Android/Sdk/platform-tools/"
    hasPathADB = False
if(int(adb_path_in) == 2):
    adb_path = input("Enter Path: (please use / instead of \\")
    if(not(adb_path[-1] == '/')):
        adb_path += '/'
    hasPathADB = False
if(int(adb_path_in) == 3):
    hasPathADB = True
def execute(command, deviceID):
    adb_response = subprocess.run(adb_path + "adb.exe -s " + deviceID + " shell " + command, shell=True, capture_output=True)
    if(len(adb_response.stderr) >  4):
        print("[Incident occured] \t " + str(adb_response.stderr)[2:-5])
    else:
        return str(str(adb_response.stdout)[2:-9]).replace('\\r', ' ').replace('\\n', ' ').replace('\\t', ' ')
def execute(command):
    adb_response = subprocess.run(adb_path + "adb.exe " + command, shell=True, capture_output=True)
    if(len(adb_response.stderr) >  4):
        print("[Incident occured] \t " + str(adb_response.stderr)[2:-5])
    else:
        return str(str(adb_response.stdout)[2:-9]).replace('\\r', ' ').replace('\\n', ' ').replace('\\t', ' ')
def selectDevice(deviceID):
    deviceID = deviceID.replace('\'','')
def listDevices():
    return execute("devices")[26:].replace("device", "").replace(' ', '')
def listApps(appType="thirdparty", listPath=False):
    appTypeDict = {"thirdparty": "-3", "system": "-s", "disabled": "-d", "enabled": "-e"}
    appType = appTypeDict.get(appType, appType + " is not a valid option")
    if("not a valid" in appType):
        print("[Incident occured] \t " + appType)
        return None
    if(listPath == True):
        listPath = "-f"
    else:
        listPath = ""
    return [app for app in execute("shell pm list packages " + appType + " " + listPath).split('  ')]
def listApps(listPath=False):
    if(listPath == True):
        listPath = "-f"
    else:
        listPath = ""
    return [app for app in str(execute("shell pm list packages -3 " + listPath)).split('  ')]
def listFeatures():
    [print(feature) for feature in execute("shell pm list features").split('  ')]
def listLibraries():
    [print(lib) for lib in execute("shell pm list libraries").split('  ')]
def getFullAppName(app):
    app = str.lower(app)
    for installedApp in listApps():
        if(app in installedApp):
            return str(installedApp)
def getFullAppPath(app):
    app = str.lower(app)
    for installedApp in listApps(True):
        if(app in installedApp):
            return str(installedApp)
def backupAPK(appName):
    print("\t[Loading] This might take a while. Will save .apk file to the current (script) folder.")
    execute("pull " + getFullAppPath(appName)[8:-len(getFullAppName(appName)[8:])-1] + " " + getFullAppName(appName)[8:] + ".apk")
    print("\t[Finished] \t " + getFullAppName(appName)[8:] + ".apk")
    print("\t[Done]")
def backupAPKList(appNameList):
    print("\t[Loading] This might take a while. Will save .apk files in the current (script) folder.")
    for appName in appNameList:
        execute("pull " + getFullAppPath(appName)[8:-len(getFullAppName(appName)[8:])-1] + " " + getFullAppName(appName)[8:] + ".apk")
        print("\t[Finished] \t " + getFullAppName(appName)[8:] + ".apk")
    print("\t[Done]")
def backupOBB(appName):
    print("\t[Loading] This might take a while. Will save OBB folder in the current (script) folder.")
    execute("pull /storage/emulated/0/Android/obb/" + getFullAppName(appName)[8:])
    print("\t[Finished] \t " + getFullAppName(appName)[8:])
    print("\t[Done]")
def backupOBBList(appNameList):
    print("\t[Loading] This might take a while. Will save OBB folders in the current (script) folder.")
    for appName in appNameList:
        execute("pull /storage/emulated/0/Android/obb/" + getFullAppName(appName)[8:])
        print("\t[Finished] \t " + getFullAppName(appName)[8:])
    print("\t[Done]")
def backupFullApp(appName):
    print("\nFetching APK:")
    backupAPK(appName)
    print("\nFetching OBB:")
    backupOBB(appName)
def backupFullAppList(appNameList):
    print("Fetching APK's now.")
    backupAPKList(appNameList)
    print("Fetching OBB's now.")
    backupOBBList(appNameList)