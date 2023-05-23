import time
import os

class responses:
    def blacklistwords():
        print("Im will not be ready to assist you if you continue using these words")
        time.sleep(2)
        print(">:(")
        
class dev:
    def version():
        file = open("status.sanfig", "r")
        contents = file.readlines()
        print(contents)
    def fightt():
        os.system("java Game.java")