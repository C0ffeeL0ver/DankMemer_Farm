import os
import requests
from dotenv import load_dotenv
import time
import random

count = 1
Option = 2
def Options():
    global Option
    print("[+][-][-][-][-][-][-][-][-][+]")
    print("[+]                        [+]")
    print("[+]         OPTIONS        [+]")
    print("[+]                        [+]")
    print("[+][-][-][-][-][-][-][-][-][+]")
    print("[+]                        [+]")
    print("[+] 1. Sell fish and hunt  [+]")
    print("[+]      2. Nothing        [+]")
    print("[+]                        [+]")
    print("[+][-][-][-][-][-][-][-][-][+]")
    Option = int(input("\n> "))

def Farm():
    global count
    global Option

    print("Script Count: "+str(count))
    data = {"content":"pls pm"}
    r.post(url, headers=headers, data=data)
    time.sleep(2)

    data = {"content":pm[random.randrange(0,5)]}
    r.post(url, headers=headers, data=data)
    time.sleep(1)

    data = {"content":"pls fish"}
    r.post(url, headers=headers, data=data)
    time.sleep(1)
    
    data = {"content":"pls hunt"}
    r.post(url, headers=headers, data=data)
    time.sleep(1)

    data = {"content":"pls beg",}
    r.post(url, headers=headers, data=data)
    time.sleep(1)

    data = {"content":"pls highlow"}
    r.post(url, headers=headers, data=data)
    time.sleep(2)

    data = {"content":highlow[random.randrange(0,2)]}
    r.post(url, headers=headers, data=data)
    time.sleep(1)

    data = {"content":"pls use padlock"}
    r.post(url, headers=headers, data=data)
    time.sleep(1)

    data = {"content":"pls use bank"}
    r.post(url, headers=headers, data=data)
    time.sleep(2)

    data = {"content":"1"}
    time.sleep(1)
    r.post(url, headers=headers, data=data)
    
    data = {"content":"pls work"}
    r.post(url, headers=headers, data=data)
    time.sleep(1)

    data = {"content":"pls daily"}
    r.post(url, headers=headers, data=data)
    time.sleep(1)

    if(Option == 1):
        #boar
        data = {"content":"pls sell boar all"}
        r.post(url, headers=headers, data=data)
        time.sleep(3)

        #bread
        data = {"content":"pls sell bread all"}
        r.post(url, headers=headers, data=data)
        time.sleep(3)

        #cookie
        data = {"content":"pls sell cookie all"}
        r.post(url, headers=headers, data=data)
        time.sleep(3)
        
        #Deer
        data = {"content":"pls sell deer all"}
        r.post(url, headers=headers, data=data)
        time.sleep(3)

        #Duck
        data = {"content":"pls sell duck all"}
        r.post(url, headers=headers, data=data)
        time.sleep(3)

        #Fish
        data = {"content":"pls sell fish all"}
        r.post(url, headers=headers, data=data)
        time.sleep(3)

        #Pizza
        data = {"content":"pls sell pizza all"}
        r.post(url, headers=headers, data=data)
        time.sleep(3)

        #Rabbit
        data = {"content":"pls sell rabbit all"}
        r.post(url, headers=headers, data=data)
        time.sleep(3)

        #rarefish
        data = {"content":"pls sell rarefish all"}
        r.post(url, headers=headers, data=data)
        time.sleep(3)

        #skunk
        data = {"content":"pls sell skunk all"}
        r.post(url, headers=headers, data=data)
        time.sleep(2)

    data = {"content":"pls dep max"}
    r.post(url, headers=headers, data=data)
    count += 1


    time.sleep(random.randrange(30,51))

    

load_dotenv()
Authorization = os.getenv('Authorization_Token')
url = os.getenv('url')
headers = {'Authorization': Authorization,}
highlow = ["low","high"]
pm = ["f","r","i","c","k"]
r = requests.session()
Options()
while(True):
    Farm()
