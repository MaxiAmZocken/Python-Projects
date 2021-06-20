# this program was coded by Maxiii
# you can add custom commands, a tutorial is here :
# https://github.com/MaxiAmZocken/Console-Launcher/blob/main/README.md/

import time
import os
import webbrowser

# ^importing all the packages

os.system("color 0a")
os.system("echo off")
os.system("title CONSOLE LAUNCHER V1 by Maxiii")
os.system("cls")

# ^changing the style of the window

print("-------------------------------")
print("[Console Launcher V1] by Maxiii")
print("-------------------------------")

print(" ")

print("Insert a command")

userinput = input(">")

# ^creating the interface

if userinput == "systeminfo":
    os.system("systeminfo")
    input("press any key to exit")

# "systeminfo" is a command that would be too complicated to add as a .bat file"

else:
    os.system(userinput)

# searching your input as a batch (.bat) file in the folder

time.sleep(0.5)
os.system("cls")
print("\\ thank you for using Console Launcher V1 \\")
time.sleep(0.5)
os.system("cls")
print("| thank you for using Console Launcher V1 |")
time.sleep(0.5)
os.system("cls")
print("/ thank you for using Console Launcher V1 /")
time.sleep(0.5)
os.system("cls")
print("\\ thank you for using Console Launcher V1 \\")
time.sleep(0.5)
os.system("cls")
print("| thank you for using Console Launcher V1 |")
time.sleep(0.5)
os.system("cls")
print("/ thank you for using Console Launcher V1 /")
time.sleep(1)
os.system("cls")
print("by Maxiii")

# "thank you" message with the funny animation at the end