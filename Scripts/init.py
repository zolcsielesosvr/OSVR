import subprocess
import zls

git_root = "https://github.com/zolcsielesosvr/"

def download_all_submodules():
    """ Download all submodules """
    subprocess.run(["git", "submodule", "update", "--init", "--recursive"])

def main():
    dir = zls.Dirs("..")
    download_all_submodules()

if __name__ == "__main__":
    main()
