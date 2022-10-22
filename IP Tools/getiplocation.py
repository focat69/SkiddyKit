import socket
import threading
import os
from time import sleep
os.system("cls && title PWN C2 // Menu")

black = "\033[0;30m"
red = "\033[0;31m"
green = "\033[0;32m"
yellow = "\033[0;33m"
blue = "\033[0;34m"
magenta = "\033[0;35m"
cyan = "\033[0;36m"
white = "\033[0;37m"
bright_black = "\033[0;90m"
bright_red = "\033[0;91m"
bright_green = "\033[0;92m"
bright_yellow = "\033[0;93m"
bright_blue = "\033[0;94m"
bright_magenta = "\033[0;95m"
bright_cyan = "\033[0;96m"
bright_white = "\033[0;97m"

def ipInfo(addr=''):
    from urllib.request import urlopen
    from json import load
    if addr == '':
        url = 'https://ipinfo.io/json'
    else:
        url = 'https://ipinfo.io/' + addr + '/json'
    res = urlopen(url)
    #response from url(if res==None then check connection)
    data = load(res)
    #will load the json response into data
    for attr in data.keys():
        if attr == "readme":
          pass
        elif attr == "ip":
          print(f'{magenta}[{white}{attr.upper()}{magenta}]{white}',' '*34+f'\t{magenta}->{white}\t',data[attr])
        else:
          print(f'{magenta}[{white}{attr.upper()}{magenta}]{white}',' '*26+f'\t{magenta}->{white}\t',data[attr])

def main():
  print(f"""{magenta}
███████╗██╗  ██╗██╗██████╗ ██████╗ ██╗   ██╗██╗  ██╗██╗████████╗
██╔════╝██║ ██╔╝██║██╔══██╗██╔══██╗╚██╗ ██╔╝██║ ██╔╝██║╚══██╔══╝
███████╗█████╔╝ ██║██║  ██║██║  ██║ ╚████╔╝ █████╔╝ ██║   ██║   
╚════██║██╔═██╗ ██║██║  ██║██║  ██║  ╚██╔╝  ██╔═██╗ ██║   ██║   
███████║██║  ██╗██║██████╔╝██████╔╝   ██║   ██║  ██╗██║   ██║   
╚══════╝╚═╝  ╚═╝╚═╝╚═════╝ ╚═════╝    ╚═╝   ╚═╝  ╚═╝╚═╝   ╚═╝   
{white}
SkiddyKit [Ip Location Finder]
By focat @ 2022
""")
  print(f"{magenta}[{white}...{magenta}]{white} Enter IP Address (Leave blank for your own IP)...")
  c = input(f"{magenta}[{white}INPUT{magenta}]{white} {magenta}[{white}>{magenta}]{white} ")
  if c.count(".") == 3:
    print(f"{magenta}[{white}INFO{magenta}]{white} Proper IP Address obtained...")
    print(f"{magenta}[{white}...{magenta}]{white} Getting information...")
    ipInfo(c)
  elif c == "":
    print(f"{magenta}[{white}INFO{magenta}]{white} Proper IP Address obtained...")
    print(f"{magenta}[{white}...{magenta}]{white} Getting information...")
    ipInfo()
  input("Press enter to quit.")

main()
quit()