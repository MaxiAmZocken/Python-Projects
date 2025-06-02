import psutil
from pystray import Icon as icon, Menu as menu, MenuItem as item
import time
import threading
import webbrowser
from PIL import Image
import subprocess

log_messages = []

def log(messages):
    print(messages)
    log_messages.append(messages)

def automation():
    # start loop
    while True:
        #list all currently opened processes
        process_names = [proc.info["name"] for proc in psutil.process_iter(["name"])]
        #check if EA Anti Cheat is open
        if "EAAntiCheat.GameServiceLauncher.exe" in process_names:  
            #check if autohotkey is open
            for process in psutil.process_iter(["name"]):
                if process.info["name"] == "AutoHotkey64.exe":
                    #kill autohotkey process
                    process.kill()
                    log("AutoHotkey has been closed")

        #check if ea anti cheat or battlefield is not open
        elif "EAAntiCheat.GameServiceLauncher.exe" not in process_names and "bfv.exe" not in process_names and "AutoHotkey64.exe" not in process_names:
            #open autohotkey
            subprocess.Popen([r"C:\Program Files\AutoHotkey\UX\AutoHotkeyUX.exe",r"D:\Programming\Git\My-Stuff\My Daily Driver.ahk"])
            log("AutoHotkey has been opened")

        time.sleep(1)

def close(icon, item):
    icon.stop()

def open_github(icon, item):
    webbrowser.open("https://www.github.com/maxiamzocken/python-projects")

tray_icon = icon("My Daily Drive", Image.open(r"D:\Programming\Git\Python-Projects\Automation\python.png"), menu=menu(
    item("Github Repo", open_github),
    item("Quit", close)
))

threading.Thread(target=automation, daemon=True).start()
tray_icon.run()
log("Tray Icon has been created")