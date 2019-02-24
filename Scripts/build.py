import subprocess
import zls

def config_osvr_core(build = "Debug"):
    dirs = zls.Dirs("OSVR-Core")
    dirs.mkdir("build", True)

    cmake = zls.CMake()

    root = "c:/osvr_development/OSVR/"
    libroot = root + "Libs/"
    cmake.add_definition("libfunctionality_DIR", libroot +"libfunctionality/install")
    cmake.add_definition("DIRECTSHOW_QEDIT_INCLUDE_DIR", libroot + "DirectShow/include/")
    cmake.add_definition("DIRECTSHOW_STRMIIDS_LIBRARY", libroot + "DirectShow/lib_x86/strmiids.lib")
    cmake.add_definition("OpenCV_DIR", "C:/OpenCV")
    #cmake.add_definition("OpenCV_STATIC", "OFF")
    cmake.add_definition("JsonCpp_INCLUDE_DIR", root + "OSVR-Core/vendor/vrpn/submodules/jsoncpp/include")
    cmake.add_definition("JsonCpp_LIBRARY", root + "OSVR-Core/vendor/vrpn/submodules/jsoncpp/build/lib/" + build + "/jsoncpp.lib")
    cmake.add_definition("BOOST_ROOT", "C:/Boost")
    cmake.add_definition("CMAKE_CXX_FLAGS", "/D_SILENCE_TR1_NAMESPACE_DEPRECATION_WARNING /EHsc /MP") #/EHsc
    #cmake.add_definition("BOOST_INCLUDEDIR", "C:/Boost/include/boost-1_70")

    proc = cmake.config()
    print(proc)

def build_osvr_core():
    dirs = zls.Dirs("OSVR-Core")
    dirs.chdir("build")
    cmake = zls.CMake()
    cmake.build()

def install_osvr_core():
    dirs = zls.Dirs("OSVR-Core")
    dirs.chdir("build")
    cmake = zls.CMake()
    cmake.set_build_target("INSTALL")
    cmake.build()

def config_jsoncpp():
    dirs = zls.Dirs("OSVR-Core")
    dirs.chdir("vendor")
    dirs.chdir("vrpn")
    dirs.chdir("submodules")
    dirs.chdir("jsoncpp")
    dirs.mkdir("build", True)
    cmake = zls.CMake()
    cmake.config()

def build_jsoncpp():
    dirs = zls.Dirs("OSVR-Core")
    dirs.chdir("vendor")
    dirs.chdir("vrpn")
    dirs.chdir("submodules")
    dirs.chdir("jsoncpp")
    dirs.mkdir("build", True)
    cmake = zls.CMake()
    cmake.set_build_config("Debug")
    cmake.build()
    cmake.set_build_config("Release")
    cmake.build()

def main():
    dirs = zls.Dirs("..")
    #config_jsoncpp()
    #build_jsoncpp()
    config_osvr_core()
    build_osvr_core()
    #install_osvr_core()

if __name__=="__main__":
    main()
