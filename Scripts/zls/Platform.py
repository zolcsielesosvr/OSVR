import platform

def IsWindows():
    return platform.system() == "Windows"

def IsLinux():
    return platform.system() == "Linux"
