from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get
from pisi.actionsapi import shelltools

def setup():
    options = "--with-zlib \
               --with-python \
               --with-readline \
               --enable-ipv6 \
               --disable-static \
               --with-threads"

    if get.buildTYPE() == "emul32":
        options += " --libdir=/usr/lib32 \
                     --bindir=/emul32/bin \
                     --without-python"
        shelltools.export("CC", "%s -m32" % get.CC())

    autotools.configure(options)

def build():
    autotools.make()

def check():
    autotools.make("check")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    if get.buildTYPE() == "emul32":
        # prevent that binaries under /usr/bin overwrites 64-bit binaries
        pisitools.removeDir("/emul32")
        pisitools.removeDir("/usr/share/gtk-doc")
        return

    for i in ["", "-python"]:
        pisitools.rename("/%s/libxml2%s-%s" % (get.docDIR(), i, get.srcVERSION()), "libxml2%s" % i)

    pisitools.dodoc("AUTHORS", "ChangeLog", "NEWS", "README", "TODO")
    pisitools.removeDir("/usr/share/gtk-doc")