#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2010 TUBITAK/BILGEM
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import kde4
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    kde4.configure()

def build():
    kde4.make()

def install():
    kde4.install()

