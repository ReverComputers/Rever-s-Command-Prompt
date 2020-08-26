#Etan's Python made command line!
#Change tries to 0 to disable it.
#commandline is the variable for commands.
#Varibles and import functions!
import os
import sys
import random
import time
import simpleaudio as sa
import psutil
import platform
from datetime import datetime
def get_size(bytes, suffix="B"):
    """
    Scale bytes to its proper format
    e.g:
        1253656 => '1.20MB'
        1253656678 => '1.17GB'
    """
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor

tries = 1
name = input("Hello there! What's your name?")
#Intro (Please don't take it for yourselves and sell it!)
print (
              """
                                            ___________________
                                           | >_               |
                                           |                  |
                                           |                  |
                                           |                  |
                                           |                  |
                                           |__________________|

                                  Made for beginners, techies, everyone!
               
               """

        )
print(
              """

                \        /\        / |-----  |      |------- |--------| |\        /| |-----
                 \      /  \      /  |       |      |        |        | | \      / | |
                  \    /    \    /   |-----  |      |        |        | |  \    /  | |-----
                   \  /      \  /    |       |      |        |        | |   \  /   | |
                    \/        \/     |-----  |_____ |------- |________| |    \/    | |-----

                I did a lot of time on this ASCII art. Please credit me before you use this!

                Made by Etan Zheng in New York!

             """
            )
time.sleep(1)
os.system('cls' if os.name == 'nt' else "printf '\033c'")
uname = platform.uname()
print(f"System: {uname.system}")
print(f"Release: {uname.release}")
print(f"Version: {uname.version}")
print(f"Machine: {uname.machine}")
print(f"Processor: {uname.processor}")
#Main code!~
print("Welcome to my command line. You can do stuff. Type cmds for a list of commands. By the way, this is version b1.1 (The Beta Expansion pack!).")
while tries == 1:
    os.system('cls' if os.name == 'nt' else "printf '\033c'")
    print('')
    commandline = input(">")
#cmds (A list of commands)
    if commandline == "cmds":
        print("")
        print("Here's the list of commands!")
        print("OS Commands")
        print("view is gonna make the computer view it.")
        print("sysinfo is is the system info.")
        print("")
        print("Python-made games")
        print("123 is a game inspired by rock, paper,scissors(its broken)")
        print("sag (means some adventure game, you can get annoyed by a bunch of kids in that game.")
        print("")
        print("Python-made tools")
        print("about is about this command line program.")
        print("cal is a calculator")
        print("counter is a counter that counts up from 1 to infinity")
        print("")
        print("useless stuff")
        print("echo (show a message)")
        print("mineshafter (play minecraft java edition for free: will need java)")
        print("")
        print("Musical Commands")
        print("music is python playing music.")
        
#view (view files using the deafult system programs)
    elif commandline == "view":
        print("")
        filepath = input("OK," + name + ",please enter the file's name and the file's extension.")
        os.startfile(filepath)
#123 (a game inspired by rock, paper, scissors)
    elif commandline == "123":
        print("")
        playerchoose = int(0)
        cpuchoose = int((random.randint(1,3)))
        print("Please know that 1 beats 3, 2 beats 1, 3 beats 2." + name + ".")
        rps = input("What do you choose?")
        if rps == 1:
            playerchoose = 1
            print("1,")
            time.sleep(1)
            print("2,")
            time.sleep(1)
            print("3!")
            print(playerchoose)
            print(cpuchoose)
            if cpuchoose == 1:
                print("Tie!")
            elif cpuchoose == 2:
                print("You lost!")
            elif cpuchoose == 3:
                print("You win!")
        elif rps == 2:
            playerchoose = 2
            print("1,")
            time.sleep(1)
            print("2,")
            time.sleep(1)
            print("3!")
            print(playerchoose)
            print(cpuchoose)
            if cpuchoose == 1:
                print("You win!")
            elif cpuchoose == 2:
                print("Tie!")
            elif cpuchoose == 3:
                print("You lose!")
        elif rps == 3:
            playerchoose = 3
            print("1,")
            time.sleep(1)
            print("2,")
            time.sleep(1)
            print("3!")
            print(playerchoose)
            print(cpuchoose)
            if cpuchoose == 1:
                print("You lose!")
            elif cpuchoose == 2:
                print("You win!")
            elif cpuchoose == 3:
                print("Tie!")
        else:
            pass
#about (You can use edit this, but can you please add me to your credits?)
    elif commandline == "about":
        print("")
        print(
              """
               ___________________
               | >_               |
               |                  |
               |                  |
               |                  |
               |                  |
               |__________________|
               
        Made for beginners, techies, everyone!
               """

        )

        print("Etan's Command Line!")
        print("")
        print("Made by Etan Zheng")
        print("A basic terminal based on Python 3.8.")
        print("This command line program is owned by " + name + ".")
#cal (a calculator program.)
    elif commandline == "cal":
        print("")
        first = int(input("What's the first number of your math problem? (Do whole numbers, not decimals)"))
        operation = str(input("What's your operation?(+ for addition, - for subtraction, / for division, "
                              "* for multiplication.)"))
        second = int(input("What's your second number?"))
        if operation == "+":
            print(first+second)
        elif operation == "-":
            print(first-second)
        elif operation == "/":
            print(first/second)
        elif operation == "*":
            print(first*second)
#counter (a counter made using for function.)
    elif commandline == "counter":
        print("")
        countto = int(input("What number do you want to count to, " + name + "?"))
        for x in range(1,countto):
            print(x)
    elif commandline == "guessmynumber":
        print("")
        long = 10
        number = (random.randint(1, 1000))
        real_number = (random.randint(1, 20) * 50)
        while long == 1:
            guess = int(input("Guess my number! " + name + "! You have 10 tries! (You can change it by changing the code, Python programmers!)"))
            if guess < real_number:
                print("Higher...")
                long = -1
            elif guess > real_number:
                print("Lower...")
                long = -1
            elif guess == real_number:
                print("Congratulations! My number is " + real_number + "!")
                long = (0)
        print("Sorry, but you lost. Good game " + name + ".")
        print("The number was " + guess + ".")
#music (deprecated)
    elif commandline == "music":
        print("")
        filename = input("Please enter your music filepath")
        wave_obj = sa.WaveObject.from_wave_file(filename)
        play_obj = wave_obj.play()
        play_obj.wait_done()
    elif commandline == "sag":
        sagtry = 1
        while sagtry == 1:
            saggp = input("You're at the playground, " + name + ", and a angry mob of kids who wants you to play tag is annoying you. What should you do? 1 for push them, 2 for ignore them, 3 for go somewhere else, 4 to end the game.")
            if saggp == "1":
                print("Mommy!")
                print("The kids mom talk to your mom.")
                print("Your mom spanks you. Ouch!")
            elif saggp == "2":
                print("The angry mob of kids still annoys you to play tag with them. You know you're too old, so you ignore them.")
            elif saggp == "3":
                area = input("Where do you wanna go? (1 for playground, 2 for store, 3 for farm, 4 for the castle.")
                print("this is demo, I'm kinda lazy")
            elif saggp == "4":
                print("Bye!")
                sagtry = -1
    elif commandline == "echo":
        print("")
        echoo == input("What message do you wanna force the computer say, " + name +"?")
        print(echo)
    elif commandline == "mineshafter":
        os.system("java -jar Mineshafter-launcher.jar")
    elif commandline == "sysinfo":
        print("="*40, "System Information", "="*40)
        uname = platform.uname()
        print(f"System: {uname.system}")
        print("="*40, "Boot Time", "="*40)
        boot_time_timestamp = psutil.boot_time()
        bt = datetime.fromtimestamp(boot_time_timestamp)
        print(f"Boot Time: {bt.year}/{bt.month}/{bt.day} {bt.hour}:{bt.minute}:{bt.second}")
        print(f"Release: {uname.release}")
        print(f"Version: {uname.version}")
        print(f"Machine: {uname.machine}")
        print(f"Processor: {uname.processor}")
        print("="*40, "CPU Info", "="*40)
        # number of cores
        print("Physical cores:", psutil.cpu_count(logical=False))
        print("Total cores:", psutil.cpu_count(logical=True))
        # CPU frequencies
        cpufreq = psutil.cpu_freq()
        print(f"Max Frequency: {cpufreq.max:.2f}Mhz")
        print(f"Min Frequency: {cpufreq.min:.2f}Mhz")
        print(f"Current Frequency: {cpufreq.current:.2f}Mhz")
        # CPU usage
        print("CPU Usage Per Core:")
        for i, percentage in enumerate(psutil.cpu_percent(percpu=True)):
            print(f"Core {i}: {percentage}%")
        print(f"Total CPU Usage: {psutil.cpu_percent()}%")
        print(f"Memory: |")
        print("         |")
        print("         ↓")
        print("="*40, "Memory Information", "="*40)
        # get the memory details
        svmem = psutil.virtual_memory()
        print(f"Total: {get_size(svmem.total)}")
        print(f"Available: {get_size(svmem.available)}")
        print(f"Used: {get_size(svmem.used)}")
        print(f"Percentage: {svmem.percent}%")
        print("="*20, "SWAP", "="*20)
        # get the swap memory details (if exists)
        swap = psutil.swap_memory()
        print(f"Total: {get_size(swap.total)}")
        print(f"Free: {get_size(swap.free)}")
        print(f"Used: {get_size(swap.used)}")
        print(f"Percentage: {swap.percent}%")
#else message (Make it what you feel like!)
    else:
        print("")
        print("What? That command does not exist! If you don't know what commands you can do, type in cmds!(If you "
              "know how to program python and you have WinRAR, extract the python file from the exe file and then "
              "reprogram the python commands.")
