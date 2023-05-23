import os
file = input("file: ")


os.system("cp "+file+" compiled.py")
os.system("python3 compiled.py")
