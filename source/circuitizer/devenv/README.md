# Circuitizer UI

### Setup

In linux you need the ```python3-pip``` package to install python modules
for our project. You can install it in ubuntu using the command

```sh
    $ sudo apt-get install python3-pip
```

*Use the python version which you want the project to
setup with using python launcher command*

```sh
    $ python -m pip install -r pip -U --no-cache-dir
```

In linux you need the ```python3-tk``` or ```python3-tkinter``` package to run application
that use Tcl/Tk as GUI Toolkit. You can install it in ubuntu using the command

```sh
    $ sudo apt-get install python3-tk
```

### Build

It is recommended to use mingw64/gcc compiler to build the
circuitizer UI instead of any other compiler for safe compilation

Default python version configured is CPython3.8_amd64.
Should work in other version but not tested.

*Any python can be used to run the build script but open
the script to configure the build information*

```sh
    $ python build.py
```

Python compilers that can be used in this project are
```
nuitka, PyInstaller
```

C compilers that can be used in this project are
```
msvc=MSVC, mingw64(recommended), gcc, clang
```
