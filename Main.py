from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import platform
import cfonts
import colorama
import os


os_name = platform.system()

colorama.init()

cfonts.say("WHATSAPP", colors=["green", "white"])
cfonts.say("PY SPAMMER", colors=["red", "white"])


print(colorama.Fore.GREEN+'''
🔒 - Use at your own risk, we are not responsible for your actions.


☑️ - Made by Mazdak Pakaghideh and OrlatoDev.


📝 - Notes: follow the instructions below and when a Firefox window open, log in Whatsapp Web and return to follow the instructions.


'''+colorama.Fore.RESET)

print(colorama.Fore.RED+'''
=======
📝 - Instructions:
--------------------------------------------------------
|1-) Type the name of the contact or group             |
|                                                      |
|2-) Type the message you want to send                 |
|                                                      |
|3-) Enter how many times you want to send the message |                             
|                                                      |
|4-) Delay beatwean each message                       |
|                                                      |
|5-) Log in to your Whatsapp                           |
|                                                      |
|6-) Type Enter after logging in and you are ready     |
|                                                      |   
|                                                      | 
-------------------------------------------------------|


''')

print(colorama.Fore.BLUE+"Name of contact or group")
name = str(input("=> "))
print( colorama.Fore.CYAN+"Message")
msg = str(input("=> "))
print(colorama.Fore.YELLOW+"Number of messages to send (0 for ultimated)")
num = int(input("=> "))

print(colorama.Fore.GREEN+"Delay beatwean each mesaage (from 0.1)")
delay = float(input("=> "))


browser = webdriver.Firefox(executable_path='your geckodriver path here')

browser.get("https://web.whatsapp.com")

time.sleep(6)

start = str(input("🔥 - Type ENTER when you log into Whatsapp and you're ready: "))


def sendMesaage(reciver, number, message , de):
    print(colorama.Fore.RED+"Spamming...")

    group = browser.find_element_by_xpath(f"//span[@title='{reciver}']")
    group.click()
    typech = browser.find_elements_by_class_name("_1awRl")

    if(number == 0):
        while(1):
            typech[1].send_keys(msg)
            typech[1].send_keys(Keys.ENTER)

            time.sleep(de)

    else:
        for i in range(number):
            typech[1].send_keys(msg)
            typech[1].send_keys(Keys.ENTER)
            time.sleep(de)

    print(colorama.Fore.GREEN+"\nFinish :)")
    os.system("cls")
    browser.close()

sendMesaage(name, num, msg  , delay)

