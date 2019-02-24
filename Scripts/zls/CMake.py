import subprocess

class CMake():
    def __init__(self, path = ".."):
        self.path = path
        self.command = ["cmake"]
        self.definitions = []
        self.generator = None
        self.build_config = None
        self.build_target = None

    def add_definition(self, definition, value):
        self.definitions.append([definition, value])

    def set_generator(self, is64bit):
        if not is64bit:
            self.generator = "Visual Studio 15 2017"
        else:
            self.generator = "Visual Studio 15 2017 Win64"

    def config(self):
        command = self.command.copy()
        for define in self.definitions:
            command.append("-D%s=%s" % (define[0], define[1]))

        command.append(self.path)

        if self.generator != None:
            command.append("-G%s" % (self.generator))

        return subprocess.run(command)

    def set_build_config(self, config):
        self.build_config = config

    def set_build_target(self, target):
        self.build_target = target

    def build(self):
        command = self.command.copy()
        command.append("--build")
        command.append(".")

        if self.build_target != None:
            command.append("--target")
            command.append(self.build_target)

        if self.build_config != None:
            command.append("--config")
            command.append(self.build_config)

        return subprocess.run(command)
