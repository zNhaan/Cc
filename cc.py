import random
import requests
import os
from time import sleep

url  =  'https://ercminer.pw/index/register_in'
headers= {
  'authority':'ercminer.pw',
  'Accept':'*/*',
  'Accept-Encoding':'gzip, deflate, br',
  'Accept-Language':'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
  'Cache-Control':'no-cache',
  'Content-Length':'116',
  'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
  'Cookie':'s47440dfe=togt3fdqo9tfd2rttjhks3vfek; token=',
  'Origin':'https://ercminer.pw',
  'Pragma':'no-cache',
  'Referer':'https://ercminer.pw//register?code=OxzPaW',
  'Sec-Ch-Ua':'"Not_A Brand";v="8", "Chromium";v="120"',
  'Sec-Ch-Ua-Mobile':'?1',
  'Sec-Ch-Ua-Platform':'"Android"',
  'Sec-Fetch-Dest':'empty',
  'Sec-Fetch-Mode':'cors',
  'Sec-Fetch-Site':'same-origin',
  'User-Agent':'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
  'X-Requested-With':'XMLHttpRequest',
}
os.system('clear')
lan=input('Nhập số lần:  ')
os.system('clear')
for i in range(0,int(lan)):
  sdt=random.randint(100000000,999999999)
  sdt='0'+str(sdt)
  data = {
    'language': 'vi_vn',
    'agent': '10000',
    'mobile': sdt,
    'password': 'nhanga123',
    'spassword': 'nhanga123',
    't_mobile': 'OxzPaW',
    'phone': sdt,
  }
  cc=requests.post(url=url, headers=headers, data=data)
  print('('+str(i+1)+') Thành Công!!')
