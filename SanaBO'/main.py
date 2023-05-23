import time
import random
import os
from questions import *
from responses import *
from triggers import *
# 1 = yes
# 0 = no
# "1" = probably yes
# "0" = probably no
# "null" = dont know!

class how:
    def python():
        print("Python is a simple, beginner friendly, multi-purpose programming language.")
        time.sleep(5)
        print("use the following code to make a hello world programme")
        time.sleep(1)
        print('print("Hello, World!")')
        time.sleep(1)
        print("and lastly... save it as a file with .py as file extention")
    def java():
        print("Java is a high-level, biolerplate based, Object Oriented Programming Language!")
        time.sleep(2)
        print('System.out.println("Hello, World") // this is a Hello World In Java.')
class jokes:
    def coding():
        used = 1
        jokesigot = ["My old car got some rust, gonna need to use SWC!", "Astronauts land on Moon, programmers say they landed on Lua.", "I once used to code pythons, now they just rattle around with bugs haha", "C is known as the mother of programming languages, I wonder from where did it came from!"]
        print(random.choice(jokesigot))
def display_name():
    print("Oh! my name is SanBO'")
while True:
    question = input("Ask SanBO' something! : ")
    question = question.lower()
    if question.startswith("who are"):
        display_name()
    elif question.startswith("Who are"):
        display_name()
    elif question.startswith("how"):
        if question.endswith("python"):
            how.python()
        elif question.endswith("life"):
            greetings.howislife()
        elif question.__contains__("learn java"):
            how.java()
        else:
            print("please try again!")
    elif question.endswith("joke"):
        joke_type = ["coding", "working"]
        joke_type_randomize = random.choice(joke_type)
        if joke_type_randomize=="coding":
            jokes.coding()
        elif joke_type_randomize=="working":
            print("its working")
    elif question.startswith("say"):
        print(question.removeprefix("say "))
    elif question.endswith("!"):
        sentence = question.removeprefix("!")
        if sentence.__contains__("joke"):
            joke_type = ["coding", "working"]
            joke_type_randomize = random.choice(joke_type)
            if joke_type_randomize=="coding":
                jokes.coding()
            elif joke_type_randomize=="working":
                print("its working")
    elif question.__contains__("created you"):
        creator.sanmick()
    elif question.__contains__("my name is?"):
        name.knows()
    elif question.__contains__("shit"):
        responses.blacklistwords()
        
    elif question.__contains__("clear console"):
        os.system("clear")
    elif question.__contains__("was funny"):
        print("Well, thanks!")
    elif question.__contains__("is funny"):
        print("Well, thanks!")
    elif question.__contains__("marry me"):
        print("Nah, I don't wanna marry a guy who makes Goofy Aah Memes bruh.")
    elif question.__contains__("my rizz"):
        print("Unfortunately, it seems to not see anything invisible as it literally means in-visible (unable to see)")
    elif question.endswith("sussy baka"):
        print("I know right?")
    elif question=="dev ver":
        dev.version()
    elif question.__contains__("hello"):
        greetings.hi()
    elif question.__contains__("hi"):
        greetings.hi()
    elif question.__contains__("sup"):
        greetings.hi()
    elif question.startswith("fortune"):
        yesorno = ["yes", "no"]
        print(random.choice(yesorno))
    elif question=="fightt":
        dev.fightt()
    elif question.endswith("thanks"):
        print("Well, what else can I assist you today!")
    elif question.endswith("quit"):
        print("Oh! bye! :(")
        quit()
    elif question=="dev ver --config":
        os.system("g++ config.cpp")
        os.system("./a.out")
    elif question=="why do the creator exist?":
        print("Creator? a guy with no purpose.")
    elif question.startswith("ok"):
	        print("Cool!, What else can I assist you with?")
    else:
        print("I don't seem to know that answer :(")
        
