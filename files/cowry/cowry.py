# -*- coding: utf-8 -*-
import requests,json,time,os
from fake_useragent import UserAgent

uat = UserAgent()
r = requests.Session()
def tunggu(t):
        while t:
                wd='[#] Jeda selama '+str(t)+" detik "
                print(wd,end='\r',flush=True)
                time.sleep(1)
                t -= 1

ua = uat.random
url = 'https://www.coowry.com/arlethdesign'
spam = 'https://www.coowry.com/api/tokens'
hd = {
        "accept": "*/*",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
        "content-length": "28",
        "content-type": "application/json",
        "origin": "https://www.coowry.com",
        "referer": "https://www.coowry.com/arlethdesign",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": uat.random
}
if os.name == 'nt':os.system('cls')
else:os.system('clear')
os.chdir('..')
os.system('cat banner.txt')
os.chdir('..')
print("===============================")
print("=        Shark Project        =")
print("===============================")
try:
        a = r.get(url,headers={'user-agent':ua}).cookies
        no = input("Contoh : +628xxx\nSilahkan Masukkan nomor target : ")
        target = {"msisdn":no}
        jsn = json.dumps(target)
        for i in range(5):
                b = r.post(spam,headers=hd,cookies={'_cwpeople_keyle_key':a["_cwpeople_key"]},data=jsn).text
                c = json.loads(b)["type"]
                if c == 'ok':
                        print("Selamat!! Telah  Sukses Mengirim Pesan Ke No "+no)
                        tunggu(0)
                else:
                        print("Maaf Limit Terdeteksi,Coba Lagi Lain Kali")
                        exit()
except KeyboardInterrupt:
        print("Terima Kasih Telah Menggunakan Tools Saya")
        exit()
except Exception as e:
        print("Kesalahan",e)
