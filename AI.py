
  
  
  
url=f'https://api.im2018.com/api/game/guess_Odd?page=1&limit={500}&type=24'
  
import os, requests, json, datetime, math, random
from time import sleep
os.system('pip install numpy && pip install scikit-learn')
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
nguoc=0
while True:
    os.system('clear')
    print(f'{xanhla}[1] 👉 {xanhnhat}Nhóm Chính\n{xanhla}[2] 👉 {xanhnhat}Nhóm Phụ')
    try:
      nhom=int(input(f'{trang}Nhập số: '))
    except ValueError:
      pass
    if nhom in [1,2]:
      break
if nhom==1:
    nhom='-4211789911'
else:
    nhom='-1002228172695'
stop=0
checkk=requests.get(url).text
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
          sleep(1)
          check=requests.get(url).text
          if check!=checkk:
            giayy=datetime.datetime.now().second
            nano=int(datetime.datetime.now().strftime('%f'))
            break
        kq=json.loads(check)
        result=[entry['result'] for entry in kq['data']]
        so=[entry['number'] for entry in kq['data']]
        so=so[::-1]
        import numpy as np
        from sklearn.linear_model import LinearRegression
        
        
        # Tạo dữ liệu đầu vào và đầu ra cho mô hình
        X = np.arange(1, len(so)+1).reshape(-1, 1) # Các giá trị từ 1 đến 12
        y = np.array(so)
        
        # Khởi tạo và huấn luyện mô hình Linear Regression
        model = LinearRegression()
        model.fit(X, y)
        
        # Dự đoán các giá trị từ 1 đến 80
        X_pred = np.arange(1, 81).reshape(-1, 1)
        tinh = model.predict(X_pred)
        
        if checkk!=landau:
          if kiemtra in result[0]:
            win+=1
            print(f'{xanhla}Win: {win}  (+1)')
            print(f'{do}Lose: {lose}')
            if ccc=='cc':
              ccc=''
            requests.get(f'https://api.telegram.org/bot7407325672:AAEEBeXZkgwwA57qDyYdgrt6OcoZY6VfEZY/sendMessage?chat_id={nhom}&text=🏆Kết quả: Thắng ✅  ({so[0]})')
            requests.get(f'https://api.telegram.org/bot7407325672:AAEEBeXZkgwwA57qDyYdgrt6OcoZY6VfEZY/sendMessage?chat_id={nhom}&text='+'🟢 Thắng: '+str(win)+'\n🔴 Thua: '+str(lose))
          else:
            lose+=1
            print(f'{xanhla}Win:  {win}')
            print(f'{do}Lose: {lose}  (+1)')
            if ccc=='cc':
              ccc=''
            requests.get(f'https://api.telegram.org/bot7407325672:AAEEBeXZkgwwA57qDyYdgrt6OcoZY6VfEZY/sendMessage?chat_id={nhom}&text=🏆Kết quả: Thua ⛔  ({so[0]})')
            requests.get(f'https://api.telegram.org/bot7407325672:AAEEBeXZkgwwA57qDyYdgrt6OcoZY6VfEZY/sendMessage?chat_id={nhom}&text='+'🟢 Thắng: '+str(win)+'\n🔴 Thua: '+str(lose))
        requests.get(f'https://api.telegram.org/bot7407325672:AAEEBeXZkgwwA57qDyYdgrt6OcoZY6VfEZY/sendMessage?chat_id={nhom}&text=================================')
        if tinh%2==0:
          cau='Even'
          cl='Chẵn'
          requests.get(f'https://api.telegram.org/bot7407325672:AAEEBeXZkgwwA57qDyYdgrt6OcoZY6VfEZY/sendMessage?chat_id={nhom}&text=Mọi người! Hãy Đánh 𝘾𝙝ẵ𝙣 ('+str(tinh)+')')
        else:
          cau='Odd'
          cl='Lẻ'
          requests.get(f'https://api.telegram.org/bot7407325672:AAEEBeXZkgwwA57qDyYdgrt6OcoZY6VfEZY/sendMessage?chat_id={nhom}&text=Mọi người! Hãy Đánh 𝙇ẻ ('+str(tinh)+')')
        print(f'{xnhac}{cau} ({cl})   |  {int(tinh)}     ({so[0]})    -({giayy}s + {nano})\n')
        kiemtra=cau
        print('\n')
        checkk=check
    else:
      sleep(0.5)
      if stop==1:
        stop=0
      print(f'\r{vang}--- {gio}  :  {phut}  :  {giay} ---',end='')