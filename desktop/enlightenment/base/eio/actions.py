#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.autoreconf("-vfi")
    autotools.configure()

def build():
    autotools.make()

def install():
    #autotools.Install()
    #autotools.rawInstall()
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    #pisitools.removeDir("/usr/bin")
    #pisitools.removeDir("/usr/share")

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "README")
