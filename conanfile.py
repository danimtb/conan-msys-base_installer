from conans import ConanFile, tools
import os


class MsysInstallerConan(ConanFile):
    name = "msys_installer"
    version = "1.0"
    license = "http://www.mingw.org/license"
    url = "http://github.com/danimtb/conan-msys-installer"
    build_policy = "missing"
    description = "Msys"
    build_requires = "7z_installer/1.0@conan/stable", "mingw_installer/1.0@conan/stable"   

    def build(self):

        files = {
            "msys-bash": "https://sourceforge.net/projects/mingw/files/MSYS/Base/bash/bash-3.1.23-1/bash-3.1.23-1-msys-1.0.18-bin.tar.xz",
            "msys-bzip2": "https://sourceforge.net/projects/mingw/files/MSYS/Base/bzip2/bzip2-1.0.6-1/bzip2-1.0.6-1-msys-1.0.17-bin.tar.lzma",
            "msys-core": "https://sourceforge.net/projects/mingw/files/MSYS/Base/msys-core/msys-1.0.19-1/msysCORE-1.0.19-1-msys-1.0.19-bin.tar.xz",
            "msys-core-ext": "https://sourceforge.net/projects/mingw/files/MSYS/Base/msys-core/msys-1.0.19-1/msysCORE-1.0.19-1-msys-1.0.19-ext.tar.xz",
            "msys-core-lic": "https://sourceforge.net/projects/mingw/files/MSYS/Base/msys-core/msys-1.0.19-1/msysCORE-1.0.19-1-msys-1.0.19-lic.tar.xz",
            "msys-core-doc": "https://sourceforge.net/projects/mingw/files/MSYS/Base/msys-core/msys-1.0.19-1/msysCORE-1.0.19-1-msys-1.0.19-doc.tar.xz",
            "msys-coreutils": "https://sourceforge.net/projects/mingw/files/MSYS/Base/coreutils/coreutils-5.97-3/coreutils-5.97-3-msys-1.0.13-bin.tar.lzma",
            "msys-diffutils": "https://sourceforge.net/projects/mingw/files/MSYS/Base/diffutils/diffutils-2.8.7.20071206cvs-3/diffutils-2.8.7.20071206cvs-3-msys-1.0.13-bin.tar.lzma",
            "msys-dos2unix": "https://sourceforge.net/projects/mingw/files/MSYS/Extension/dos2unix/dos2unix-7.3.2-1/dos2unix-7.3.2-1-msys-1.0.18-bin.tar.lzma",
            "msys-file": "https://sourceforge.net/projects/mingw/files/MSYS/Base/file/file-5.04-1/file-5.04-1-msys-1.0.13-bin.tar.lzma",
            "msys-findutils": "https://sourceforge.net/projects/mingw/files/MSYS/Base/findutils/findutils-4.4.2-2/findutils-4.4.2-2-msys-1.0.13-bin.tar.lzma",
            "msys-gawk": "https://sourceforge.net/projects/mingw/files/MSYS/Base/gawk/gawk-3.1.7-2/gawk-3.1.7-2-msys-1.0.13-bin.tar.lzma",
            "msys-grep": "https://sourceforge.net/projects/mingw/files/MSYS/Base/grep/grep-2.5.4-2/grep-2.5.4-2-msys-1.0.13-bin.tar.lzma",
            "msys-gzip": "https://sourceforge.net/projects/mingw/files/MSYS/Base/gzip/gzip-1.3.12-2/gzip-1.3.12-2-msys-1.0.13-bin.tar.lzma",
            "msys-less": "https://sourceforge.net/projects/mingw/files/MSYS/Base/less/less-436-2/less-436-2-msys-1.0.13-bin.tar.lzma",
            "msys-libiconv": "https://sourceforge.net/projects/mingw/files/MSYS/Base/libiconv/libiconv-1.14-1/libiconv-1.14-1-msys-1.0.17-dll-2.tar.lzma",
            "msys-libintl": "https://sourceforge.net/projects/mingw/files/MSYS/Base/gettext/gettext-0.18.1.1-1/libintl-0.18.1.1-1-msys-1.0.17-dll-8.tar.lzma",
            "msys-make": "https://sourceforge.net/projects/mingw/files/MSYS/Base/make/make-3.81-3/make-3.81-3-msys-1.0.13-bin.tar.lzma",
            "msys-sed": "https://sourceforge.net/projects/mingw/files/MSYS/Base/sed/sed-4.2.1-2/sed-4.2.1-2-msys-1.0.13-bin.tar.lzma",
            "msys-tar": "https://sourceforge.net/projects/mingw/files/MSYS/Base/tar/tar-1.23-1/tar-1.23-1-msys-1.0.13-bin.tar.lzma",
            "msys-termcap": "https://sourceforge.net/projects/mingw/files/MSYS/Base/termcap/termcap-0.20050421_1-2/termcap-0.20050421_1-2-msys-1.0.13-bin.tar.lzma",
            "msys-texinfo": "https://sourceforge.net/projects/mingw/files/MSYS/Base/texinfo/texinfo-4.13a-2/texinfo-4.13a-2-msys-1.0.13-bin.tar.lzma",
            "msys-xz": "https://sourceforge.net/projects/mingw/files/MSYS/Base/xz/xz-5.0.3-1/xz-5.0.3-1-msys-1.0.17-bin.tar.lzma"
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
