import os
import time
from datetime import date

space = " "
heading = "------------------------------\n[TOLLES PROGRAMM] -> by Maxiii\n------------------------------"
today = date.today()

#added a on/off switch for the "while loop"
switch = 1

#variable for price
need_to_pay = 0
#variable for shopping list
list = []

#startup 
os.system("cls")
for i in range (2):
    print("--------------\nstarting .\n--------------")
    time.sleep(0.5)
    os.system("cls")
    print("--------------\nstarting ..\n--------------")
    time.sleep(0.5)
    os.system("cls")
    print("--------------\nstarting ...\n--------------")
    time.sleep(0.5)
    os.system("cls")

#while loop for multiple orders until you wirte "exit"
while switch == 1:
    print(heading)
    print(space)
    print("1 - Pommes - 1€")
    print("2 - Bratwurst 2€")
    print("3 - Cola - 3€")
    print(space)
    print(f"price : {need_to_pay}€")
    print(space)
    print("enter a article number")
    userinput1 = input("> ")

    if userinput1 == "1":
        need_to_pay = need_to_pay + 1
        list.append("Pommes - 1€")
        os.system("cls")
    elif userinput1 == "2":
        need_to_pay = need_to_pay + 2
        list.append("Bratwurst - 2€")
        os.system("cls")
    elif userinput1 == "3":
        need_to_pay = need_to_pay + 3
        list.append("Cola - 3€")
        os.system("cls")
    elif userinput1 == "exit":
        #change switch to 0, so the loop ends
        switch -= 1
    else:
        print("wrong commmand, try again")
        time.sleep(1)
        os.system("cls")

f = open(f"C:\\Users\\maxi_\\Documents\\GIT\\Python-Projects\\Cash-Register\\Logs\\{today}.txt", "a")
for shopping_list in list:
    f.write(f"{shopping_list}\n")
f.close()

os.system("cls")
print(heading)
print(space)

#print out what we added to our shopping_list variable with a "for loop"
print("You ordered : ")
for shopping_list in list:
    print(shopping_list)
print(space)

#print out what we added to the need_to_pay variable
print("You need to pay :")
print(f"{need_to_pay}€")
input()