import os
import time
import math
import random
from datetime import datetime

class SanScript:
    def storeVar(var, val):
        var = val
class brh:
    def accessFileSystem():
        print("Well Well Calm Down! That's a dangerous Action Right there")


    def showFiles():
        os.system("ls")
    def ENV():
        openENVFile = open("ENV.senv", "r").read()
        ENVlines = openENVFile.splitlines()
        print(ENVlines)
    def power(brh):
        if brh == True:
            os.system("powermenu")
        else:
            print("You don't have BRH/Admin controls")
class user:
    def deleteUser():
        os.chdir("saner")    
        os.chdir("brh")
        os.chdir("spwd")
        pwd = input("Current Password : ")

        pwd_file = open("password.sapwd", "r").read()
        pwds = pwd_file.splitlines()
        if pwds.__contains__(pwd):
            print("Correct Password!")
            os.chdir("..")
            os.chdir("..")
            os.chdir("..")
            os.chdir("saner")
            os.chdir("brh")
            rootUserFile = open("root_user.sanos", "w")
            rootUserFile.write("")
    
            os.chdir("spwd")
            openPwd = open("password.sapwd", "w")
            
            openPwd.write("")

            os.chdir("..")
            os.chdir("..")
            os.chdir("..")
            print("User Account has been deleted!")

        else:      
            print("Incorrect Password!")
        
    

    class root:
        def login(pwd):
            try:
                os.chdir("/saner/brh/spwd/")
                pwd_file = open("password.sapwd", "r").read()
                pwds = pwd_file.splitlines()
                if pwds.__contains__(pwd):
                    print("Correct Password!")
                    fileSystem.ENV()
                else:
                    print("Incorrect Password!")

                    print("sanOS quit regarding security issues, are you YOU?!")
                    quit()

            
            except:
                print("Please create atleast 1 root account to log in to!")
        def ENV_ROOT():
            
            try:
                os.chdir("saner")    
                os.chdir("brh")
                os.chdir("spwd")
                pwd = input("Current Password : ")

                pwd_file = open("password.sapwd", "r").read()
                pwds = pwd_file.splitlines()
                if pwds.__contains__(pwd):
                    print("Correct Password!")
                    os.chdir("..")
                    os.chdir("..")
                    os.chdir("..")
                    os.chdir("ssaner")
                    fileSystem.ENV()
                    os.chdir("..")
                else:      
                    print("Incorrect Password!")
                # Hello(1)
            except:
                pwd = input("Current Password : ")

                pwd_file = open("password.sapwd", "r").read()
                pwds = pwd_file.splitlines()
                if pwds.__contains__(pwd):
                    print("Correct Password!")
                    os.chdir("..")
                    os.chdir("..")
                    os.chdir("..")
                    os.chdir("ssaner")
                    fileSystem.ENV()
                    os.chdir("..")
                else:      
                    print("Incorrect Password!")
                # Hello(1)
    def createRoot(name, pwd):
        
        os.chdir("saner")

        os.chdir("brh")
        rootUserFile = open("root_user.sanos", "w")
        rootUserFile.write(name+"=ALL\n")
  
        os.chdir("spwd")
        createRootPwd = open("password.sapwd", "w")
        
        createRootPwd.write(pwd)
        os.chdir("..")
        os.chdir("..")
        os.chdir("..")
    def createNormalUser(name, pwd):
        try:
            os.chdir("saner")
            os.mkdir("normal")
            os.chdir("normal")
            createNormalFile = open("cnf.sanser", "w")
            createNormalFile.write(name)
            os.chdir("..")
            os.chdir("..")
            os.chdir("..")
            
            try:
                os.mkdir("npwd")
                os.chdir("npwd")
                createNormalPwd = open("nrmss.sapwd", "w")
                createNormalPwd.write(pwd)
                os.chdir("..")
                os.chdir("..")
                os.chdir("..")
                os.chdir("..")

            except:
                os.chdir("npwd")
                createNormalPwd = open("nrmss.sapwd", "w")
                createNormalPwd.write(pwd)
                os.chdir("..")
                os.chdir("..")
                os.chdir("..")
                os.chdir("..")

        except:

            os.chdir("saner")
            os.chdir("normal")
            createNormalFile = open("cnf.sanser", "w")
            createNormalFile.write(name)
            try:
                os.mkdir("npwd")
                os.chdir("npwd")
                createNormalPwd = open("nrmss.sapwd", "w")
                createNormalPwd.write(pwd)
                os.chdir("..")
                os.chdir("..")
                os.chdir("..")
                os.chdir("..")

            except:
                os.chdir("npwd")
                createNormalPwd = open("nrmss.sapwd", "w")
                createNormalPwd.write(pwd)
                os.chdir("..")
                os.chdir("..")
                os.chdir("..")
                

    def createUser(type, name, pwd):
        if type=="root":
            user.createRoot(name, pwd)
        elif type=="normal":
            user.createNormalUser(name, pwd)
class sonsole:
    def clear():
        os.system("clear")
    def createHistory(cmd):
        os.chdir("ssaner")
        createHistoryFile = open("history.sanos", "w")

        createHistoryFile.write(cmd)

        os.chdir("..")
    def getHistory():
        os.chdir('ssaner')
        openHistoryFile = open("history.sanos", "r").read()
        jb_hist = openHistoryFile.splitlines()
        print(jb_hist)
class emof:
    def launch():
        os.chdir("emof")
        try:
            print("[Note: use exit() command to exit out!]")
            os.system("g++ emof_main.cpp")
            os.system("./a.out")
        except:
            print("[Note: use exit() command to exit out!]")
            os.system("./a.out")
print("SanOS by SanMick (c)")
while True:
    sanli = input("❯ ")
    if sanli.startswith("ctd "):

        try:
            os.chdir(sanli.removeprefix("ctd "))
        except:
            print("No directory/folder named: "+sanli.removeprefix("ctd"))
        sonsole.createHistory("ctd")    
    elif sanli.startswith("cf "):
        os.chdir("sahome")
        createFile = open(sanli.removeprefix("cf "), "a")
        sonsole.createHistory(sanli)
        os.chdir("..")
    elif sanli.startswith("edf "):
        os.chdir("sahome")
        sonsole.createHistory(sanli)
        try:
            os.system("vim "+sanli.removeprefix("edf "))
        except:
            os.system("nano "+sanli.removeprefix("edf "))
        os.chdir("..")
    elif sanli=="edf":
        print("SanScript: usage | edf file")
    elif sanli.startswith("del "):
        sonsole.createHistory(sanli)
        try:
            os.system("rm "+sanli.removeprefix("del "))
        except:
            print("Unable to delete! "+sanli.removeprefix("del ")+" Is a directory!")
    elif sanli=="clear":
        sonsole.createHistory(sanli)
        sonsole.clear()
    elif sanli=="cls":
        sonsole.createHistory(sanli)
        sonsole.clear()
    
    elif sanli=="lnch desktop":
        sonsole.createHistory(sanli)
        createMemFile = open("ram.sanos", "a")
        openMemFile = open("ram.sanos", "w")
        val = 10;
        usemem = val=+1
        usemem = val
        usemem = str(usemem)
        openMemFile.write(usemem+"\n")
        print("mem usage: "+usemem)

        try:
            os.system("java Desktop.java")
        except:
            print("Unable to find Desktop file!")
    elif sanli.startswith("sanFo"):
        sonsole.createHistory(sanli)
        if sanli.endswith("-d"):
            
            os.system("neofetch --ascii_distro sanFo")
            
        else:
            os.system("neofetch --ascii_distro "+sanli.removeprefix("sanFo"))

    elif sanli.startswith("wellsay "):
        sonsole.createHistory(sanli+os.linesep)
        print(sanli.removeprefix("wellsay "))
    elif sanli.startswith("wellsayf"):
        openVarFilea = open("var.san", "r").read()
        lines = openVarFilea.splitlines()
        if lines.__contains__(sanli.removeprefix("wellsayf ")):
            print(lines)
    elif sanli.__contains__("="):
        VarFile = open("var.san", "a")
        VarFile.write(sanli)
        print(sanli)
        print("RESTART SANOS TO REGISTER YOUR VARIABLES")
    elif sanli.startswith("$var"):
        
        openVarFilef = open("var.san", "r").read()
        variables = openVarFilef.splitlines()
        print(variables)
    elif sanli.startswith("files"):
        sonsole.createHistory(sanli)
        fileSystem.showFiles()
    elif sanli.startswith("cd"):
        sonsole.createHistory(sanli)
        os.system("mkdir "+sanli.removeprefix("cd"))
    elif sanli.startswith("swaponEquip "):
        sonsole.createHistory(sanli)
        os.system("sudo swapon "+sanli.removeprefix("swaponEquip "))
    
    elif sanli.startswith("ENV"):
        sonsole.createHistory(sanli)
        print("You need Tree Permissions to access ENV Files!")
    elif sanli.startswith("brh "):
        sonsole.createHistory(sanli)
        if sanli.__contains__("ENV"):
            user.root.ENV_ROOT()
        elif sanli.__contains__("dlac"):
            user.deleteUser()
        elif sanli.endswith("poweropt"):
            brh.power(True)
        else:
            print("SanScript: Unknown Command | '"+sanli.removeprefix("brh ")+"'")
    elif sanli == "poweropt":
        brh.power(False)
    elif sanli.startswith("crtuser "):
        sonsole.createHistory(sanli)
        print("Creating user : "+sanli.removeprefix("crtuser "))
        # Hello(0.9)
        accntpwd = input("[New Account's Password] : ")
        # Hello(1)
        re_enter_pwd = input("[Confirm Password] : ")
        if re_enter_pwd==accntpwd:
            sonsole.createHistory(sanli)
            user.createUser("root", sanli.removeprefix("crtuser "), accntpwd)
            print("Correct Password! Creating Root Account "+sanli.removeprefix("crtuser "))
        else:
            print("Account-Creation Procedure Quitted, reason: Unmatching Passwords")
    elif sanli.startswith("whatisthis"):
        sonsole.createHistory(sanli)
        print("Well Hello There!")
        # Hello(1)
        print("Official Operating System of SanMick")
        print("Glory to SanMick!")
    elif sanli.startswith("snr"):
        sonsole.createHistory(sanli)
        os.chdir("saner")
        os.chdir("brh")
        readRootFile = open("root_user.sanos", "r").read()
        snrlines = readRootFile.splitlines()
        if snrlines==[]:
            print("You don't have any root accounts!")
        else:
            print(snrlines)
        os.chdir("..")
        os.chdir("..")
    elif sanli.startswith("imlazy"):
        sonsole.createHistory(sanli)
        print("Well then! time to get up and do something in your life! just think about it, What your life will be if you don't get up and do anything")
    elif sanli.startswith("cuser "):
        sonsole.createHistory(sanli)
        npwd = input("[New  For Account] : ")
        cpwd = input("[Confirm PaPasswordssword For Account] : ")
        if cpwd==npwd:
            print("Password Matched")
            print("Creating Sanser/User : "+sanli.removeprefix("cuser"))
            user.createUser("normal", sanli.removeprefix("cuser "), npwd)
        else:
            print("Passwords didn't match!")

    elif sanli.startswith("fif "):
        sonsole.createHistory(sanli)
        wtfind = input("What do you want to find in the file? : ")
        os.system("grep "+sanli.removeprefix("fif ")+wtfind)
    
    elif sanli.startswith("help"):
        sonsole.createHistory(sanli)
        os.chdir("ssaner")
        openHelpFile = open("commands.sanos", "r").read()
        cmds = openHelpFile.splitlines()
        print(cmds)
        os.chdir("..")
    elif sanli=="time":
        sonsole.createHistory(sanli)
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print("The current time is:", current_time)
    elif sanli.startswith("dlac"):
        sonsole.createHistory(sanli)
        print("You need BRH to do this!") # Idk why I named it as brh ahh
    
    elif sanli.startswith("date"):
        sonsole.createHistory(sanli)
        print(datetime.today())
    elif sanli.startswith("uptime"):
        sonsole.createHistory(sanli)
        os.system("uptime")
    elif sanli.startswith("emof"):
        sonsole.createHistory(sanli)
        if sanli.endswith("--run"):
            emof.launch()
        elif sanli.endswith("--help"):
            os.chdir("emof")
            readFile = open("help.sanos", "r").read()
            lines = readFile.splitlines()
            print(lines)
            os.chdir("..")
        else:
            print("enter --help for emof help!")
    elif sanli=="":
        continue
    elif sanli==" ":
        print("SanScript: Please enter a command!")
    elif sanli.startswith("jb"):
        sonsole.getHistory()
    elif sanli.startswith("gb"):
        os.chdir("..")
    elif sanli.startswith("scd"):
        os.system("pwd")
    elif sanli.startswith("deldir"):
        os.removedirs(sanli.removeprefix("deldir "))
    elif sanli.startswith("mkdir"):
            try:
                os.mkdir(sanli.removeprefix("mkdir "))
            except:
                print("Usage: mkdir <filename>")
            

    elif sanli.startswith("*.dirs"):
        if sanli.endswith("-a"):
            os.system("ls")
        elif sanli.endswith("-s"):
            sorts = input("sort: ")
            os.system("ls '"+sorts+"'")
    elif sanli.startswith("exit()"):
        quit()
    elif sanli.startswith("pwd"):
        if sanli.endswith("-c"):
            print("Proceeding ..")
            
    else:
        print("SanScript: Unknown Command | '"+sanli+"'")
        if sanli.startswith("c"):
            print("Did you mean any of these? | cls, clear")
        elif sanli.startswith("*"):
            print("Did you mean any of these? | *.dirs")
        elif sanli.startswith("$"):
            print("Did you mean any of these? | $var")