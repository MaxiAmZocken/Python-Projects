import os
import time

switch = 1
space = " "

need_to_pay = 0

while switch == 1:
    print("------------------------------")
    print("[TOLLES PROGRAMM] -> by Maxiii")
    print("------------------------------")
    print(space)
    print("1 - Pommes - 1€")
    print("2 - Bratwurst 2€")
    print("3 - Cola - 3€")
    print(space)
    print(f"price : {need_to_pay}€")
    print(space)
    print("enter a article number")
    userinput1 = input("> ")

    if userinput1 == "101":
        need_to_pay = need_to_pay + 1
        os.system("cls")
    elif userinput1 == "102":
        need_to_pay = need_to_pay + 2
        os.system("cls")
    elif userinput1 == "103":
        need_to_pay = need_to_pay + 3
        os.system("cls")
    elif userinput1 == "exit":
        switch -= 1
    else:
        print("wrong commmand, try again")
        time.sleep(1)
        os.system("cls")

os.system("cls")
print("------------------------------")
print("[TOLLES PROGRAMM] -> by Maxiii")
print("------------------------------")
print(space)
print("You need to pay :")
print(f"{need_to_pay}€")
input()