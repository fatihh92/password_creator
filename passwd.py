# _*_ coding:utf-8 _*_

import random
import time
b = []
def büyük_harf():
    for i in range(3):
        a = random.choice("ABCÇDEFGHIİJKLMNOÖPRSŞTUÜVYZ")
        if a in b:
           continue
        else:
           b.append(a)

def kücük_harf():
    for i in range(3):
        c = random.choice("abcçdefghıijklmnoöprsştuüvyz")
        if c in b:
            continue
        else:
            b.append(c)

def sayi():
    for i in  range(3):
        f = random.randint(0,9)
        if f in b:
            continue
        else:
            b.append(f)

def karakter():
    for i in range(3):
        h = random.choice('!^+%&/()=?_-*}\][{$#£><')
        if h in b:
            continue
        else:
            b.append(h)

def birlesme():
    büyük_harf()
    kücük_harf()
    sayi()
    karakter()
    random.shuffle(b)
#    print("random:",b)
if __name__ == '__main__':
    birlesme()
    while True:
        if len(b) < 12:
            print("eleman sayısı 12den kücük")
            birlesme()
            print(b)
            time.sleep(5)
        else:
            print(b)
            print("uzunluk:",len(b))
            break
