#!/usr/bin/python3

import os
import tarfile

# Unzip assets
if not os.path.isfile('_tkinter.pyd'):
    with tarfile.open('lib.tar.xz') as f:
        f.extractall('.')
    try:
        os.remove('lib.tar')
    except:
        pass

# Launch entry point
import mainUI
mainUI.main()