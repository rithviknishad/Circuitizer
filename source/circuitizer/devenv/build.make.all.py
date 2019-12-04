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
exec(open('build.config').read())

# Generate build
if __name__ == "__main__":
    # Add disable console argv if specified in build configuration
    if not CONSOLE:
        BUILD_ARGS.append('windows-disable-console' if sys.platform == 'win32' else '')
    # Setup the linux build process
    if sys.platform == 'linux':
        print(LINUX_SETUP_SH)
        os.system(LINUX_SETUP_SH)
    # Setup the python pip requirements
    os.system(PYTHON_POINTER + ' -m pip install -r "' + PYTHON_PIP_CONFIG + '" -U')
    if BUILD:
        # Clean previous build folder
        for dir in [
            TARGET_MAIN_FILE[:-3] + '.build/',
            TARGET_MAIN_FILE[:-3] + '.dist/',
            RUNTIME_FILE[:-3] + '.build/',
            RUNTIME_FILE[:-3] + '.dist/'
        ]:
            try:
                shutil.rmtree(dir)
            except:
                pass
        # build UI
        print(PYTHON_POINTER + ' -' + str(PYTHON_VERSION) + ' -m ' + BUILD_PROVIDER + ' --module ' + TARGET_MAIN_FILE + ' --remove-output --' + C_COMPILER)
        os.system(PYTHON_POINTER + ' -' + str(PYTHON_VERSION) + ' -m ' + BUILD_PROVIDER + ' --module ' +TARGET_MAIN_FILE + ' --remove-output --' + C_COMPILER)
        # build bootloader and make application entry point
        print(PYTHON_POINTER + ' -' + str(PYTHON_VERSION) + ' -m ' + BUILD_PROVIDER + ' ' + RUNTIME_FILE + ' -' + ' --'.join(BUILD_ARGS))
        os.system(PYTHON_POINTER + ' -' + str(PYTHON_VERSION) + ' -m ' + BUILD_PROVIDER + ' ' + RUNTIME_FILE + ' ' + ' --'.join(BUILD_ARGS))
        # copy UI binaries
        for file in glob.glob('*.pyd'):
            shutil.copy(file, RUNTIME_FILE[:-3] + '.dist/')
            os.remove(file)
        # clean build junk
        for file in glob.glob('*.a'):
            os.remove(file)
        for file in glob.glob('*.pyi'):
            os.remove(file)
    # Enable file-based optimization
    if OPTIMISE: 
        for file in glob.glob(os.getcwd() + '/' + RUNTIME_FILE[:-3] + '.dist/*'):
            for garbage_file in open(OPTIMISE_SIZE_LIST).readlines():
                if os.path.split(file)[1] == garbage_file[:-1]:
                    try:
                        os.remove(file)
                    except:
                        print("Failed to optimize file : " + file)
    # Copy Application Resources
    if COPY_ASSETS:
        shutil.copytree('res/', RUNTIME_FILE[:-3] + '.dist/res/')
    # Tar file compression to reduce size of the application
    if REDUCE_SIZE:
        tar = tarfile.open(RUNTIME_FILE[:-3] + '.dist/lib.tar.xz', "w:xz")
        def path_leaf(path):
            head, tail = ntpath.split(path)
            return tail or ntpath.basename(head)
        for name in open(OPTIMISE_TAR_LIST).readlines():
            file = RUNTIME_FILE[:-3] + '.dist/' + name[:-1]
            tar.add(file, arcname=path_leaf(file))
            try:
                os.remove(file)
            except:
                shutil.rmtree(file)
        tar.close()
