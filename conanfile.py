from conans import ConanFile, tools
import os


class MsysInstallerConan(ConanFile):
    name = "msys_installer"
    version = "1.0"
    license = "http://www.mingw.org/license"
    url = "http://github.com/danimtb/conan-msys-installer"
    settings = "os", "compiler"
    build_policy = "missing"
    description = "Msys"
    build_requires = "7z_installer/1.0@conan/stable", "mingw_installer/1.0@conan/stable"

    def configure(self):
        if (self.settings.os != "Windows" and self.settings.compiler != "gcc"):
            raise Exception("Not valid configuration: %s, %s. %s should be used in Windows, gcc" % (self.settings.os, self.settings.compiler, self.name))

    def build(self):

        files = {
            "msys-bash": "http://prdownloads.sourceforge.net/mingw/bash-3.1.23-1-msys-1.0.18-bin.tar.xz",
            "msys-bzip2": "http://prdownloads.sourceforge.net/mingw/bzip2-1.0.6-1-msys-1.0.17-bin.tar.lzma",
            "msys-bzip2-dll": "http://prdownloads.sourceforge.net/mingw/libbz2-1.0.6-1-msys-1.0.17-dll-1.tar.lzma",
            "msys-core": "http://prdownloads.sourceforge.net/mingw/msysCORE-1.0.19-1-msys-1.0.19-bin.tar.xz",
            "msys-core-ext": "http://prdownloads.sourceforge.net/mingw/msysCORE-1.0.19-1-msys-1.0.19-ext.tar.xz",
            "msys-core-lic": "http://prdownloads.sourceforge.net/mingw/msysCORE-1.0.19-1-msys-1.0.19-lic.tar.xz",
            "msys-core-doc": "http://prdownloads.sourceforge.net/mingw/msysCORE-1.0.19-1-msys-1.0.19-doc.tar.xz",
            "msys-coreutils": "http://prdownloads.sourceforge.net/mingw/coreutils-5.97-3-msys-1.0.13-bin.tar.lzma",
            "msys-diffutils": "http://prdownloads.sourceforge.net/mingw/diffutils-2.8.7.20071206cvs-3-msys-1.0.13-bin.tar.lzma",
            "msys-dos2unix": "http://prdownloads.sourceforge.net/mingw/dos2unix-7.3.2-1-msys-1.0.18-bin.tar.lzma",
            "msys-file": "http://prdownloads.sourceforge.net/mingw/file-5.04-1-msys-1.0.13-bin.tar.lzma",
            "msys-magic-dll": "http://prdownloads.sourceforge.net/mingw/libmagic-5.04-1-msys-1.0.13-dll-1.tar.lzma",
            "msys-findutils": "http://prdownloads.sourceforge.net/mingw/findutils-4.4.2-2-msys-1.0.13-bin.tar.lzma",
            "msys-gawk": "http://prdownloads.sourceforge.net/mingw/gawk-3.1.7-2-msys-1.0.13-bin.tar.lzma",
            "msys-grep": "http://prdownloads.sourceforge.net/mingw/grep-2.5.4-2-msys-1.0.13-bin.tar.lzma",
            "msys-gzip": "http://prdownloads.sourceforge.net/mingw/gzip-1.3.12-2-msys-1.0.13-bin.tar.lzma",
            "msys-less": "http://prdownloads.sourceforge.net/mingw/less-436-2-msys-1.0.13-bin.tar.lzma",
            "msys-libiconv": "http://prdownloads.sourceforge.net/mingw/libiconv-1.14-1-msys-1.0.17-dll-2.tar.lzma",
            "msys-libintl": "http://prdownloads.sourceforge.net/mingw/libintl-0.18.1.1-1-msys-1.0.17-dll-8.tar.lzma",
            "msys-make": "http://prdownloads.sourceforge.net/mingw/make-3.81-3-msys-1.0.13-bin.tar.lzma",
            "msys-regex-dll": "http://prdownloads.sourceforge.net/mingw/libregex-1.20090805-2-msys-1.0.13-dll-1.tar.lzma",
            "msys-sed": "http://prdownloads.sourceforge.net/mingw/sed-4.2.1-2-msys-1.0.13-bin.tar.lzma",
            "msys-tar": "http://prdownloads.sourceforge.net/mingw/tar-1.23-1-msys-1.0.13-bin.tar.lzma",
            "msys-termcap": "http://prdownloads.sourceforge.net/mingw/termcap-0.20050421_1-2-msys-1.0.13-bin.tar.lzma",
            "msys-termcap-dll": "http://prdownloads.sourceforge.net/mingw/libtermcap-0.20050421_1-2-msys-1.0.13-dll-0.tar.lzma",
            "msys-texinfo": "http://prdownloads.sourceforge.net/mingw/texinfo-4.13a-2-msys-1.0.13-bin.tar.lzma",
            "msys-xz": "http://prdownloads.sourceforge.net/mingw/xz-5.0.3-1-msys-1.0.17-bin.tar.lzma",
            "msys-lzma-dll": "http://prdownloads.sourceforge.net/mingw/liblzma-5.0.3-1-msys-1.0.17-dll-5.tar.lzma",
            "msys-z-dll": "http://prdownloads.sourceforge.net/mingw/zlib-1.2.7-1-msys-1.0.17-dll.tar.lzma"
        }

        for util_name in files:
            tools.download(files[util_name], util_name)
            self.run("7z x %s" % util_name)
            self.run("7z x %s~" % util_name)
            os.unlink(util_name)
            os.unlink("%s~" % util_name)
    
    def package(self):
        self.copy("*", dst="", src=".")

    def package_info(self):
        self.env_info.path.append(os.path.join(self.package_folder, "bin"))
