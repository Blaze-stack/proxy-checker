import os
from time import sleep
import requests
import random
import string
from colorama import Fore


os.system("cls")

print(f"{Fore.WHITE}[ {Fore.CYAN}\u00A7 {Fore.WHITE}] {Fore.LIGHTBLACK_EX}proxy checker made by {Fore.WHITE}Blaze{Fore.LIGHTBLACK_EX}, support me via cashapp {Fore.WHITE}$TrentonWaterz{Fore.LIGHTBLACK_EX} | Licensed under {Fore.WHITE}MIT {Fore.LIGHTBLACK_EX}License")
print(f"{Fore.WHITE}[ {Fore.CYAN}\u00A7 {Fore.WHITE}] {Fore.LIGHTBLACK_EX}my github: {Fore.WHITE}https://github.com/Blaze-stack")

site = input(f"{Fore.WHITE}[ {Fore.YELLOW}> {Fore.WHITE}] {Fore.LIGHTBLACK_EX}what site do you want to test on? [needs to start with https://-http://] {Fore.WHITE}(https://github.com is the defalt){Fore.LIGHTBLACK_EX}: {Fore.WHITE}")

if site == "":
	site = "https://github.com"




def scrape():
    scraped = 0
    f = open("proxies.txt", "a+")
    f.truncate(0)
    r = requests.get('https://api.proxyscrape.com/?request=displayproxies&proxytype=http&timeout=1500&ssl=yes')
    proxies = []
    for proxy in r.text.split('\n'):
        proxy = proxy.strip()
        proxy = 'https://' + proxy
        if proxy:
            proxies.append(proxy)
    for p in proxies:
        scraped = scraped + 1 
        f.write((p)+"\n")
    f.close()
    print(f"{Fore.WHITE}[ {Fore.YELLOW}? {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Scraped {Fore.WHITE}{scraped} {Fore.LIGHTBLACK_EX}proxies.")
    sleep(.1)




def readproxies():
    try:
        p = open("proxies.txt", encoding="UTF-8")
    except FileNotFoundError:
        p = open("proxies.txt", "w+", encoding="UTF-8")
        print(f"{Fore.WHITE}[{Fore.RED} ! {Fore.WHITE}]{Fore.LIGHTBLACK_EX} No proxies found in {Fore.WHITE}proxies.txt!{Fore.WHITE}")
        raise SystemExit



    rproxy = p.read().split('\n')
    for i in rproxy:
        if i == "" or i == " ":
            index = rproxy.index(i)
            del rproxy[index]
    p.close()
    
    return rproxy
    
    
rproxy=readproxies()

scrapep = input(f"{Fore.WHITE}[ {Fore.YELLOW}> {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Auto proxy scrape {Fore.WHITE}(yes or no){Fore.LIGHTBLACK_EX}: {Fore.WHITE}")
if scrapep == "yes":
	amount = 150
	fulla = amount
elif scrapep == "no":
	amount = 10000
	fulla = amount



if scrapep == "yes":

    scrape()

if not rproxy:
        print(f"{Fore.WHITE}[{Fore.RED} ! {Fore.WHITE}]{Fore.LIGHTBLACK_EX} No proxies found in {Fore.WHITE}proxies.txt!{Fore.WHITE}")
        raise SystemExit



while amount > 0:
    f = open(f"working-proxies.txt","a", encoding="UTF-8")
    try:
        if not rproxy[0]:
            print(f"{Fore.WHITE}[ {Fore.RED}! {Fore.WHITE}] {Fore.LIGHTBLACK_EX}All proxies are invalid{Fore.WHITE}")
            
            #Here, when all the proxies are invalid, if the users choosed to auto-scrape proxy, the program is scraping new proxies.
            if scrapep == "yes":
                print(f"{Fore.WHITE}[ {Fore.YELLOW}? {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Rescraping Proxies...{Fore.WHITE}")
                scrape()
                rproxy=readproxies()
            else:
                exit()

    except:
        print(f"{Fore.WHITE}[ {Fore.RED}! {Fore.WHITE}] {Fore.LIGHTBLACK_EX}All proxies are invalid{Fore.WHITE}")
        if scrapep == "yes":
            print(f"{Fore.WHITE}[ {Fore.YELLOW}? {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Rescraping Proxies...{Fore.WHITE}")
            scrape()
            rproxy=readproxies()
        else:
            exit()
    
    proxi = random.choice(rproxy)
    proxies = {
        "https": proxi
    }
    amount = amount - 1
    
    try:
        url = requests.get(f"{site}", proxies=proxies, timeout=3)
        if url.status_code == 200:
            print(f"{Fore.WHITE}[ {Fore.GREEN}+ {Fore.WHITE}] {Fore.LIGHTBLACK_EX} working Proxy found! {Fore.WHITE}{code}{Fore.WHITE}")
            f.write(f"\n{proxi}")
            f.close()
        elif url.status_code == 404:
            print(f"{Fore.WHITE}[ {Fore.GREEN}+ {Fore.WHITE}] {Fore.LIGHTBLACK_EX} working Proxy found! {Fore.WHITE}{code}{Fore.WHITE}")
            f.write(f"\n{proxi}")
            f.close()
        elif url.status_code == 429:
            fulla = fulla - 1
            print(f"{Fore.WHITE}[ {Fore.RED}- {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Proxy {Fore.WHITE}{proxi}{Fore.LIGHTBLACK_EX} is ratelimited!")
            index = rproxy.index(proxi)
            del rproxy[index]
        else:
            fulla = fulla - 1
            print(f"{Fore.WHITE}[ {Fore.RED}! {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Invalid Error! | Status code {Fore.WHITE}{url.status_code}")
    except:
        index = rproxy.index(proxi)
        del rproxy[index]
        pw = open(f"proxies.txt","w", encoding="UTF-8")
        for i in rproxy:
            pw.write(i + "\n")
        pw.close()
        fulla = fulla - 1
        print(f"{Fore.WHITE}[ {Fore.RED}- {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Failed connecting to proxy {Fore.WHITE}{proxi}{Fore.LIGHTBLACK_EX} | Removing from list!")

f.close()
print(f"{Fore.WHITE}[ {Fore.YELLOW}? {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Successfully tested {Fore.WHITE}{fulla} proxies {Fore.LIGHTBLACK_EX}{Fore.WHITE}")

input() 