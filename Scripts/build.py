import subprocess
import zls

def build_osvr_core():
    dirs = zls.Dirs("OSVR-Core")
    dirs.mkdir("build", True)

    command = ["cmake"]

    root = "c:/osvr_development/OSVR3/"
    libroot = root + "Libs/"
    command.append("-D%s=%s" % ("libfunctionality_DIR", libroot +"libfunctionality"))
    command.append("-D%s=%s" % ("DIRECTSHOW_QEDIT_INCLUDE_DIR", libroot + "DirectShow/include/"))
    command.append("-D%s=%s" % ("DIRECTSHOW_STRMIIDS_LIBRARY", libroot + "DirectShow/lib_x86/strmiids.lib"))
    command.append("-D%s=%s" % ( "OpenCV_DIR", libroot + "OpenCV"))
    command.append("..")

    subprocess.run(command)


def main():
    dirs = zls.Dirs("..")

    build_osvr_core()

if __name__=="__main__":
    main()
