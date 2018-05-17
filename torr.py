#_*_  coding:utf- 8_*_

import requests
import random
import time
import socket
print("Local IP: ",socket.gethostbyname(socket.gethostname()))
l = requests.get('https://ifconfig.co/ip')
print("Wan IP: ",l.text)
proxy_list = []
soc_dosya = open('proxy.txt', 'r')
soketler = soc_dosya.readlines()
for i in soketler:
    a = i.strip()
    proxy_list.append(a)
print("---PROXİES---")
while True:
     soc = random.choice(proxy_list)
     print(soc)
     proxies = {'http':'socks5://'+str(soc)+":"+str(9050)}
     k = requests.get('http://mockbin.org/ip',proxies=proxies)
     print(k.text)
     print("waitting...")
     time.sleep(300)