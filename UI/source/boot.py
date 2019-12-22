#!/usr/bin/python3

import os
import sys
import tarfile
import tempfile
import shutil

HOME = os.getcwd()

# Unzip assets lib.tar.xz
if not os.path.isfile('_tkinter.pyd'):
    with tarfile.open('lib.tar.xz') as f:
        f.extractall('.')
    try:
        os.remove('lib.tar')
        os.remove('lib.tar.xz')
    except:
        pass

# Unzip assets tcl.tar.xz
if not os.path.isfile(tempfile.gettempdir() + '/tcl/'):
    with tarfile.open('tcl.tar.xz') as f:
        os.chdir(tempfile.gettempdir())
        f.extractall('.')
    try:
        os.remove('tcl.tar')
        os.remove('tcl.tar.xz')
    except:
        pass

os.chdir(HOME)
os.environ['TCL_LIBRARY'] = tempfile.gettempdir() + '/tcl/'
os.environ['TK_LIBRARY'] = tempfile.gettempdir() + '/tk/'
sys.path.insert(0, tempfile.gettempdir())

# Launch entry point
import mainUI
mainUI.main()
