try:
  import os, requests, json, datetime, math, random
  from time import sleep
  ccc='cc'
  kiemtra=''
  win=lose=0
  do = "\033[1;91m"
  xanhbien = "\033[1;36m"
  vang = "\033[0;33m"
  hong = "\033[1;35m"
  xanhduong = "\033[1;34m"
  xanhla = "\033[1;32m"
  xanh="\033[1;32m"
  cam="\033[1;33m"
  blue="\033[1;34m"
  lam="\033[1;34m"
  tim="\033[1;34m"
  syan="\033[1;36m"
  xnhac= "\033[1;96m"
  den="\033[1;90m"
  luc="\033[1;92m"
  xduong="\033[1;94m"
  trang="\033[1;97m"
  xanhnhat = "\033[1;36m"
  trang1 = "\033[1;37m"
  stop=0
  nguoc=0
  checkk=requests.get('https://api.im2018.com/api/game/guess_Odd?page=1&limit=50&type=24').text
  landau=checkk
  os.system('clear')
  if datetime.datetime.now().minute%2==0:
    print(f'{xanhla}Đang check cầu!! Đợi đợt sau!!')
    while True:
      sleep(0.5)
      if datetime.datetime.now().minute%2!=0:
        break
  else:
    print(f'{xanhla}Đang check cầu!! Đợi đợt sau!!')
  while True:
    tg=datetime.datetime.now()
    gio=tg.hour
    phut=tg.minute
    giay=tg.second
    if phut%2==0:
      if stop==0:
        os.system('clear')
        stop=1
        while True:
          sleep(0.5)
          check=requests.get('https://api.im2018.com/api/game/guess_Odd?page=1&limit=50&type=24').text
          if check!=checkk:
            giayy=datetime.datetime.now().second
            nano=int(datetime.datetime.now().strftime('%f'))
            break
        kq=json.loads(check)
        so=[entry['number'] for entry in kq['data']]
        result=[entry['result'] for entry in kq['data']]
        serial=[entry['serial'] for entry in kq['data']]
        tinh=0
        for i in so:
          tinh+=i
        if tinh>80:
          while True:
            tinh//=so[0]
            if tinh<=80:
              break
        tinh+=1
        if checkk!=landau:
          if kiemtra in result[0]:
            win+=1
            print(f'{xanhla}Win: {win}  (+1)')
            print(f'{do}Lose: {lose}')
            if ccc=='cc':
              ccc=''
            requests.get('https://api.telegram.org/bot7407325672:AAEEBeXZkgwwA57qDyYdgrt6OcoZY6VfEZY/sendMessage?chat_id=-1002228172695&text=🏆Kết quả: Thắng ✅')
            requests.get('https://api.telegram.org/bot7407325672:AAEEBeXZkgwwA57qDyYdgrt6OcoZY6VfEZY/sendMessage?chat_id=-1002228172695&text='+'🟢 Thắng: '+str(win)+'\n🔴 Thua: '+str(lose))
          else:
            lose+=1
            print(f'{xanhla}Win:  {win}')
            print(f'{do}Lose: {lose}  (+1)')
            if ccc=='cc':
              ccc=''
            requests.get('https://api.telegram.org/bot7407325672:AAEEBeXZkgwwA57qDyYdgrt6OcoZY6VfEZY/sendMessage?chat_id=-1002228172695&text=🏆Kết quả: Thua ⛔')
            requests.get('https://api.telegram.org/bot7407325672:AAEEBeXZkgwwA57qDyYdgrt6OcoZY6VfEZY/sendMessage?chat_id=-1002228172695&text='+'🟢 Thắng: '+str(win)+'\n🔴 Thua: '+str(lose))
          requests.get('https://api.telegram.org/bot7407325672:AAEEBeXZkgwwA57qDyYdgrt6OcoZY6VfEZY/sendMessage?chat_id=-1002228172695&text=================================')
        if tinh%2==0:
          cau='Even'
          cl='Chẵn'
          requests.get('https://api.telegram.org/bot7407325672:AAEEBeXZkgwwA57qDyYdgrt6OcoZY6VfEZY/sendMessage?chat_id=-1002228172695&text=Mọi người! Hãy Đánh 𝘾𝙝ẵ𝙣 ('+str(tinh)+')')
        else:
          cau='Odd'
          cl='Lẻ'
          requests.get('https://api.telegram.org/bot7407325672:AAEEBeXZkgwwA57qDyYdgrt6OcoZY6VfEZY/sendMessage?chat_id=-1002228172695&text=Mọi người! Hãy Đánh 𝙇ẻ ('+str(tinh)+')')
        print(f'{xnhac}{cau} ({cl})   |  {int(tinh)}     ({so[0]})    -({giayy}s + {nano})\n')
        kiemtra=cau
        print('\n')
        checkk=check
    else:
      sleep(0.5)
      if stop==1:
        stop=0
      print(f'\r{vang}--- {gio}  :  {phut}  :  {giay} ---',end='')
except:
  requests.get('https://api.telegram.org/bot7407325672:AAEEBeXZkgwwA57qDyYdgrt6OcoZY6VfEZY/sendMessage?chat_id=-1002228172695&text=👉Admin Đã Dừng Bot👈')