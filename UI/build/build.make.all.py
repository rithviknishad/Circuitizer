#!/usr/bin/python3
# Build Script for Circuitizer UI
# usage: python build.make.all.py

import os
import sys
import glob
import shutil
import tarfile
import ntpath

# import build configurations for the project
exec(open('build/build.config').read())

LINUX_SETUP_SH = 'build/build.' + LINUX_SETUP_SH 
PYTHON_PIP_CONFIG = 'build/build.' + PYTHON_PIP_CONFIG
OPTIMISE_SIZE_LIST = 'build/build.' + OPTIMISE_SIZE_LIST
OPTIMISE_TAR_LIST = 'build/build.' + OPTIMISE_TAR_LIST

def do(stuff):
    print(stuff)
    os.system(stuff)


# Generate build
if __name__ == "__main__":
    # add the C compiler to build argv
    BUILD_ARGS.append(C_COMPILER)
    # Add disable console argv if specified in build configuration
    if not CONSOLE:
        BUILD_ARGS.append('windows-disable-console' if sys.platform is 'win32' else '')
    # Setup the linux build process
    if sys.platform is 'linux':
        do(LINUX_SETUP_SH)
    # Setup the python pip requirements
    os.system(PYTHON_POINTER + ' -m pip install -r "' + PYTHON_PIP_CONFIG + '" -U')
    if BUILD:
        for file in glob.glob('source/*'):
            # ISSUE: Used try n except statment to make sure we do not
            # copy Permission Denied files
            try:
                shutil.copy(file, os.getcwd())
            except:
                pass
        # Clean previous build folder
        for dir in [
            TARGET_MAIN_FILE[:-3] + '.build/',
            TARGET_MAIN_FILE[:-3] + '.dist/',
            ntpath.basename(RUNTIME_FILE[:-3]) + '.build/',
            ntpath.basename(RUNTIME_FILE[:-3]) + '.dist/'
        ]:
            try:
                shutil.rmtree(dir)
            except:
                pass
        for file in glob.glob('*.py'):
            os.remove(file)
        # build UI
        do(PYTHON_POINTER + ' -m ' + BUILD_PROVIDER + ' --module ' +TARGET_MAIN_FILE + ' --remove-output --' + C_COMPILER)
        # build bootloader and make application entry point
        do(PYTHON_POINTER + ' -m ' + BUILD_PROVIDER + ' ' + RUNTIME_FILE + ' ' + ' --'.join(BUILD_ARGS))
        # copy UI binaries
        for file in glob.glob('*.pyd'):
            shutil.copy(file, ntpath.basename(RUNTIME_FILE[:-3]) + '.dist/')
            os.remove(file)
        # clean build junk
        for file in glob.glob('*.a'):
            os.remove(file)
        for file in glob.glob('*.pyi'):
            os.remove(file)
        for file in glob.glob('*.py'):
            os.remove(file)
    # Enable file-based optimization
    if OPTIMISE: 
        for file in glob.glob(os.getcwd() + '/' + ntpath.basename(RUNTIME_FILE[:-3]) + '.dist/*'):
            for garbage_file in open(OPTIMISE_SIZE_LIST).readlines():
                if os.path.split(file)[1] == garbage_file[:-1]:
                    print(file)
                    try:
                        os.remove(file)
                    except:
                        shutil.rmtree(file)
                        print("Failed to optimize file : " + file)
    # Copy Application Resources
    if COPY_ASSETS:
        shutil.copytree('resource/', ntpath.basename(RUNTIME_FILE[:-3]) + '.dist/resource/')
    # Tar file compression to reduce size of the application
    if REDUCE_SIZE:
        tar = tarfile.open(ntpath.basename(RUNTIME_FILE[:-3]) + '.dist/lib.tar.xz', "w:xz")
        def path_leaf(path):
            head, tail = ntpath.split(path)
            return tail or ntpath.basename(head)
        for name in open(OPTIMISE_TAR_LIST).readlines():
            file = ntpath.basename(RUNTIME_FILE[:-3]) + '.dist/' + name[:-1]
            tar.add(file, arcname=path_leaf(file))
            try:
                os.remove(file)
            except:
                shutil.rmtree(file)
        tar.close()
