import subprocess
import zls

git_root = "https://github.com/zolcsielesosvr/"

def download_all_submodules():
    """ Download all submodules """
    subprocess.run(["git", "submodule", "update", "--init", "--recursive"])

def download_opencv():
    """ Download OpenCV """
    command = ["git", "clone"]
    tag = "2.4"
    if tag != None:
        command.append("--branch")
        command.append(tag)
    command.append("--recurse-submodules")
    command.append("https://github.com/opencv/opencv.git")
    command.append("OpenCV")
    subprocess.run(command)

def config_opencv():
    """ Configure OpenCV """
    cmake = zls.CMake()
    cmake.add_definition("CMAKE_INSTALL_PREFIX", "C:/OpenCV")
    cmake.add_definition("CMAKE_CXX_FLAGS", "/D_SILENCE_TR1_NAMESPACE_DEPRECATION_WARNING /DWIN32")
    cmake.add_definition("BUILD_SHARED_LIBS", "ON")
    cmake.config()

def build_opencv(config):
    """ Build OpenCV """
    cmake = zls.CMake()
    cmake.set_build_config(config)
    cmake.build()

def install_opencv(config):
    """ Install OpenCV """
    cmake = zls.CMake()
    cmake.set_build_config(config)
    cmake.set_build_target("INSTALL")
    cmake.build()

def init_opencv():
    dir = zls.Dirs("Libs")
    if not dir.exists("OpenCV"):
        download_opencv()
    dir.chdir("OpenCV")
    dir.mkdir("build_x86", True)
    config_opencv()
    build_opencv("Debug")
    build_opencv("Release")
    install_opencv("Debug")
    install_opencv("Release")

def download_boost():
    """ Download Boost """
    command = ["git", "clone"]
    tag = "boost-1.69.0"
    if tag != None:
        command.append("--branch")
        command.append(tag)
    command.append("--recurse-submodules")
    command.append("https://github.com/boostorg/boost.git")
    command.append("Boost")
    subprocess.run(command)

def init_boost():
    dir = zls.Dirs("Libs")
    if not dir.exists("boost"):
        download_boost()
    dir.chdir("boost")
    subprocess.run(["bootstrap.bat"])
    #subprocess.run(["b2", "install", "--with-thread", "--with-system", "--with-date_time", "--with-chrono", "--with-program_options", "--with-filesystem", "--with-locale", "link=static", "runtime-link=shared", "threading=multi"])
    command = ["b2", "install"]
    justRequiredModules = True
    if justRequiredModules:
        command.append("--with-thread")
        command.append("--with-system")
        command.append("--with-date_time")
        command.append("--with-chrono")
        command.append("--with-program_options")
        command.append("--with-filesystem")
        command.append("--with-locale")
    command.append("link=static")
    command.append("runtime-link=shared")
    command.append("threading=multi")
    subprocess.run(["b2", "install", "link=static", "runtime-link=shared", "threading=multi"])

def init_libfunctionality():
    dir = zls.Dirs("Libs")
    dir.chdir("libfunctionality")
    cmake = zls.CMake()
    dir.mkdir("build", True)
    cmake.add_definition("CMAKE_CXX_FLAGS", "/D_SILENCE_TR1_NAMESPACE_DEPRECATION_WARNING")
    cmake.add_definition("CMAKE_INSTALL_PREFIX", "../install")
    cmake.config()
    cmake.build()
    cmake.set_build_target("INSTALL")
    cmake.build()

def main():
    dir = zls.Dirs("..")
    #download_all_submodules()
    #init_libfunctionality()
    init_opencv()
    #init_boost()

if __name__ == "__main__":
    main()
