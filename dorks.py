#Auto re-coded : S4174MA

import sys
import time
import os

# custom speed strings
def slow(s):
    for c in s + '\n' :
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(10. / 100)
def med(s):
   for c in s + '\n' :
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(4. / 100)
def fast(s):
   for c in s + '\n' :
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(2. / 170)

try:
    from googlesearch import search

except ImportError:
    fast("[!] wait a moment, this program will install google module ...\033[1;32;40m")
    os.system("pip3 install google")
    time.sleep(3)
    print(" ")
    med("[*] done ...")

def banner():
    print("""
 ____             _    _            _____           _     
|  _ \  ___  _ __| | _(_)_ __   __ |_   _|__   ___ | |___ 
| | | |/ _ \| '__| |/ / | '_ \ / _` || |/ _ \ / _ \| / __|
| |_| | (_) | |  |   <| | | | | (_| || | (_) | (_) | \__ \\
|____/ \___/|_|  |_|\_\_|_| |_|\__, ||_|\___/ \___/|_|___/
                               |___/    
    """)


def clear(): #clear function XD
    if sys.platform.startswith('linux'):
        os.system('clear')
    elif sys.platform.startswith('freebsd'):
        os.system('clear')
    else:
        os.system('cls')

# check python version   
if sys.version.startswith("3"):
    slow("[!] python3 detected ...")
    time.sleep(3)
else:
    slow("[x] you must be run using python3 ...")
    time.sleep(3)
    sys.exit(1)

# print starting XD
slow('[!] starting ... ')
time.sleep(2)
clear()
time.sleep(1)
banner()
med("""
\033[1;31;40m[+]\033[00m AUTHOR :\033[32m T3RR8US P4NK
\033[1;31;40m[+]\033[00m TEAM : \033[32m Pinoy ClaySec | R4tzploit | CafSechax |
\033[1;31;40m[+]\033[00m GREETZ : \033[32m T3RR8US | FL3MC3 | L3NC3 | C0DEPY | GRINXZ |""")
time.sleep(2)

try:
    namefile = input("\n\033[1;31;40m[?]\033[00m Want to save the dork result file (\033[32m\033[00mY/\033[31mN\033[00m) ").strip()
    dork = ("")

except KeyboardInterrupt:
        time.sleep(0.5)
        print("\n[!] exit")
        sys.exit(1)


def savefile(namefile):
    file = open((dork) + ".txt", "a")
    file.write(str(namefile))
    file.write("\n")
    file.close()


if namefile.startswith("y" or "Y"):
    print("[!] \033[36minput filename without extension ✓")
    dork = input("\033[00m[?] enter the file name : \033[32m")
    savefile(namefile)


def akhir():
    try:
        dork = input("\033[1;31;40m\n[*] \033[1;37;40mEnter your dork : \033[32m")
        uneed = input("\033[1;37;40m[?]\033[1;37;40m How much do you need :\033[32m ")
        print ("\n ")

        requ = 0

        for results in search(dork, tld="com", lang="en", num=int(uneed), start=0, stop=None, pause=2):
            print ("[*]", results)
            time.sleep(0.1)
            requ += 1.
            if requ >= int(uneed):
                break

            namefile = (results)

            savefile(namefile)
            time.sleep(0.1)

    except KeyboardInterrupt:
            print ("\n")
            print ("[!] exit ..")
            time.sleep(0.5)
            sys.exit(1)

    slow("[!] done ... ")
    sys.exit()



akhir()