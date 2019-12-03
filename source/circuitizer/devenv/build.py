#!/usr/bin/python3
# Build Script for Circuitizer UI
# usage: python build.py

import os
import sys
import glob
import shutil

OPTIMISE = True
COPY_ASSETS = True
PYTHON_VERSION = 3.8
BUILD_PROVIDER = 'nuitka' # nuitka, PyInstaller
PYTHON_POINTER = 'py'
RUNTIME_FILE = 'main.py'
C_COMPILER = 'mingw64' # msvc=MSVC, clang, mingw64(safest)
OUTPUT_NAME = "Circuitizer"
BUILD_ARGS = [
    '--experimental=use_pefile', 'standalone',
    C_COMPILER, 'plugin-enable=tk-inter', 'show-progress',
    'remove-output', 'windows-disable-console' if sys.platform == 'win32' else ''
] if BUILD_PROVIDER == 'nuitka' else [
    'noconsole', 'onedir', 'noupx',
    'strip', 'noconfirm', 'clean', 'name "Circuitizer"'
]

# Generate build
if __name__ == "__main__":
    # Clean previous build folder
    try:
        shutil.rmtree('main.dist/')
    except:
        pass
    # build UI
    print(PYTHON_POINTER + ' -' + str(PYTHON_VERSION) + ' -m ' + BUILD_PROVIDER + ' ' + RUNTIME_FILE + ' -' + ' --'.join(BUILD_ARGS))
    os.system(PYTHON_POINTER + ' -' + str(PYTHON_VERSION) + ' -m ' + BUILD_PROVIDER + ' ' + RUNTIME_FILE + ' ' + ' --'.join(BUILD_ARGS))
    # Enable file-based optimization
    if OPTIMISE == True: 
        for file in glob.glob(os.getcwd() + '/main.dist/*'):
            for garbage_file in open('optimise').readlines():
                if os.path.split(file)[1] == garbage_file[:-1]:
                    try:
                        os.remove(file)
                    except:
                        print("Failed to optimize file : " + file)
    # Copy Application Resources
    if COPY_ASSETS == True:
        shutil.copytree('res/', 'main.dist/res/')
