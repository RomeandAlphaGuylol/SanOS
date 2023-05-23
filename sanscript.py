from sys import *
import os
class sanscript:
    def __init__(self, file):
        self.sfile = file
        openFile = open(file, "r").read()
        code = openFile.splitlines()
        if code.__contains__("main.py"):
            os.system("./a.out")
if __name__=="__main__":
    sanscript(argv[1])


