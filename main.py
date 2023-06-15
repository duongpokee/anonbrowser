import random
import os
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import requests

filepx = open("proxy.txt", "r")
px = filepx.read().splitlines()
linepx = len(open("proxy.txt").readlines())
filepx.close

fileua = open("ua.txt", "r")
ua = fileua.read().splitlines()
lineua = len(open("ua.txt").readlines())
fileua.close

i = 0
n = random.choice(range(1, lineua))
ua = ua[int(n)]
m = random.choice(range(1, linepx))
px = px[int(m)]
def getpass():
    global keyau
    keyau = requests.get('https://accclonedp2.000webhostapp.com/pass/chrome.txt').text

def run():
    opts = Options()
    opts.add_argument("user-agent=" + ua)
    opts.add_argument("--proxy-server=" + px) 
    opts.add_argument('window-size=400,600')   
    driver = webdriver.Chrome(options=opts)
    os.system('cls')
    print("")
    print("")
    print("░█████╗░███╗░░██╗░█████╗░███╗░░██╗██╗░░░██╗  ██████╗░██████╗░░█████╗░░██╗░░░░░░░██╗░██████╗███████╗██████╗░")
    print("██╔══██╗████╗░██║██╔══██╗████╗░██║╚██╗░██╔╝  ██╔══██╗██╔══██╗██╔══██╗░██║░░██╗░░██║██╔════╝██╔════╝██╔══██╗")
    print("███████║██╔██╗██║██║░░██║██╔██╗██║░╚████╔╝░  ██████╦╝██████╔╝██║░░██║░╚██╗████╗██╔╝╚█████╗░█████╗░░██████╔╝")
    print("██╔══██║██║╚████║██║░░██║██║╚████║░░╚██╔╝░░  ██╔══██╗██╔══██╗██║░░██║░░████╔═████║░░╚═══██╗██╔══╝░░██╔══██╗")
    print("██║░░██║██║░╚███║╚█████╔╝██║░╚███║░░░██║░░░  ██████╦╝██║░░██║╚█████╔╝░░╚██╔╝░╚██╔╝░██████╔╝███████╗██║░░██║")
    print("╚═╝░░╚═╝╚═╝░░╚══╝░╚════╝░╚═╝░░╚══╝░░░╚═╝░░░  ╚═════╝░╚═╝░░╚═╝░╚════╝░░░░╚═╝░░░╚═╝░░╚═════╝░╚══════╝╚═╝░░╚═╝ ")
    print("=̶=̶=̶=̶=̶=̶=̶=̶=̶=̶=̶=̶=̶=̶=̶=̶=̶=̶=̶=̶=̶=̶=̶=̶=̶=̶=̶=̶=̶=̶=̶=̶=̶=̶=̶=̶=̶=̶=̶=̶=̶=̶=̶=̶=̶=̶=̶=̶=̶=̶=̶=̶=̶")
    print("")
    print("UA: " + ua)
    print("PROXY: " + px)
    print("")
    print("=̶=̶=̶=̶=̶=̶=̶=̶=̶=̶=̶=̶=̶=̶=̶=̶=̶=̶=̶=̶=̶=̶=̶=̶=̶=̶=̶=̶=̶=̶=̶=̶=̶=̶=̶=̶=̶=̶=̶=̶=̶=̶=̶=̶=̶=̶=̶=̶=̶=̶=̶=̶=̶")
    url = input("URL: ")
    try: 
        driver.get(url)
    except:
        print("Proxy die!!!")


def login():
    url = 'https://link4m.com/JgcFmdwn'
    os.system('cls')
    getpass()
    print("Neu Ban Khong Co Mat Khau Hay Vao Link Sau Day De Lay!!!")
    print("====================================================================")
    print(url)
    print("====================================================================")
    print("Key Vinh Vien")
    key = input("Key: ")
    if key == keyau:
        print("")
        print("Dang Nhap Thanh Cong")
        sleep(3)
        os.system('cls')
        run()
    else:
        print("Vui Long Nhap Lai Key!")


login()
