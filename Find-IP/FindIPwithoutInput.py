import socket
import os
from requests import get
space = " "

external_ip = get('https://api.ipify.org').content.decode('utf8')
hostname = socket. gethostname()
local_ip = socket. gethostbyname(hostname)
os.system("cls")
print("Internal IP : "+local_ip)
print("External IP : "+external_ip)
