import os
import StringIO
from conans import ConanFile

class MsysTestConan(ConanFile):
    generators = "gcc"
    settings = {"os", "arch", "compiler"}

    def build(self):
        self.run("make -C %s" % self.conanfile_directory)

    def test(self):
        self.run("main")