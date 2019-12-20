#!/usr/bin/python3
# Circuitizer Schematics Format

import os
import sys
import time
import shutil

class Circuit:
    def __init__(self):
        self.work = 'working.circuit'
        self.time = 0
    def clean(self):
        try:
            file = open(self.work, 'w')
            file.write('')
            file.close()
        except FileNotFoundError:
            print('No working circuit found!')
    def header(self, file):
        file = open(self.work, 'a')
        file.write('crt = [')
        file.close()
    def footer(self, file):
        code = """
]
for sys in crt:
    self.pen.goto(sys[0], sys[1])
    self.pen.getscreen().addshape(sys[2])
    self.pen.shape(sys[2])
    self.pen.stamp()
self.pen.home()
"""
        file = open(self.work, 'a')
        file.write(code)
        file.close()
    def save(self, file):
        start = time.time()
        shutil.copy(self.work, file)
        return time.time() - start
    def load(self, file):
        start = time.time()
        file = open(file).readlines()
        return file, time.time() - start
    def load_compile(self, file):
        file = file.replace('.pyd', '') if sys.platform == 'win32' else file.replace('.so', '')
        exec("import " + file)
    def realtime(self, x, y, symbol):
        file = open(self.work, 'a')
        file.write('\n(' + str(x) + ', ' + str(y) + ', "' + symbol + '"),')
        file.close()
    def compile(self, file):
        argv = ['module', 'mingw64']
        try:
            new = file.replace('.circuit', '.py')
            os.rename(file, new)
        except FileExistsError:
            os.remove(new)
            os.rename(file, new)
        if os.system('nuitka --version') == 0:
            os.system('nuitka' + ' ' + new + ' --' + ' --'.join(argv))

def test():
    # test case for the schematic format
    test = Circuit()
    # clean the realtime save file first
    test.clean()
    # generate the header required for the file
    test.header(test.work)
    # add some data to the file
    test.realtime(30, 40, 'and.gif')
    # generate the footer required for the file
    test.footer(test.work)
    # the file where will save
    crt = 'untitled.circuit'
    # saving the circuit file (copying from the realtime file)
    test.save(crt)
    # compile the circuit file
    test.compile(crt)
    # load the circuit file to the UI
    print(test.load(crt.replace('.circuit', '.py')))
    # load the compiled circuit file to the UI
    print(test.load_compile(crt.replace('.circuit', '.pyd')))

if __name__ == "__main__":
    test()
