![Circuitizer Logo]
(https://raw.githubusercontent.com/rithviknishad/Circuitizer/master/docs/logo/logo0.png)

# Circuitizer
Circuitizer is the free and open source electric circuit development suit.

__In development stage__

### Objective:

 - Rich tools for circuit development
 - Rich ananlysis tools for circuit diagnostics
 - Script your own mathematical instructions using our rich tools precompiled in c++
 - View your circuit in 3D, and place your 

# Circuitizer UI

### Setup

In linux you need the ```python3-pip``` package to install python modules
for our project. Also you need the ```python3-tk``` package to run application
that use Tcl/Tk as GUI Toolkit. You can install it in ubuntu using the command

```sh
    $ bash build.make.linux.ubuntu.sh
```

### Build

It is recommended to use mingw64/gcc compiler to build the
circuitizer UI instead of any other compiler for safe compilation

Default python version configured is CPython3.8_amd64.
Should work in other version but not tested.

*Any python can be used to run the build script but open
the script to configure the build information*

```sh
    $ python build.make.all.py
```
