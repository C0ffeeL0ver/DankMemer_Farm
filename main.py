import os
import requests
from dotenv import load_dotenv
import time
import random

count = 1
def Farm():
    global count
    print("Script Count: "+str(count))
    data = {"content":"pls pm"}
    r.post(url, headers=headers, data=data)
    time.sleep(1)

    data = {"content":"f"}
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
    time.sleep(1)

    data = {"content":highlow[random.randrange(0,1)]}
    r.post(url, headers=headers, data=data)
    time.sleep(1)

    data = {"content":"pls use padlock"}
    r.post(url, headers=headers, data=data)
    time.sleep(1)

    data = {"content":"pls use bank"}
    r.post(url, headers=headers, data=data)
    time.sleep(1)

    data = {"content":"1"}
    time.sleep(1)
    r.post(url, headers=headers, data=data)
    
    data = {"content":"pls dep max"}
    r.post(url, headers=headers, data=data)
    count += 1
    time.sleep(40)

load_dotenv()
Authorization = os.getenv('Authorization_Token')
url = os.getenv('url')
headers = {'Authorization': Authorization,}
highlow = ["low","high"]
r = requests.session()
while(True):
    Farm()