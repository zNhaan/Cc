import requests
import os 
from time import sleep

url = "https://data.mang5g.me/api/v1/user/order/checkout"

header = {
  "Accept":"application/json",
  "Accept-Encoding":"gzip, deflate, br",
  "Accept-Language":"vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5",
  "Cache-Control":"no-cache",
  "Content-Language":"vi-VN",
  "Content-Length":"45",
  "Content-Type":"application/json",
  "Cookie":"_ga=GA1.1.222023184.1704082155; XSRF-TOKEN=eyJpdiI6IlpXazB1VjVxMWNpZWZuSG9LWUR1K3c9PSIsInZhbHVlIjoiWVFVMGY3Wi9oZHlxMVZydUlkMU04aDBqSmVxVkIyWlZ3T05rdVlXUHEwNVpvMjN4ODhzdlZWRTNlYnphSG45RHJibWxYdksxZW5XRUN0aGM3bWJiUlQ2NzFMTmQ3QVZKRDRRbFJva1hTRUFOeThmaDNPQWJDYkppOGV5UHZaQ2MiLCJtYWMiOiI0MmM1M2RhMzZjNjA1YTI3NzkyMWRmYTkyYWRmMzdkZDM1YTBiYjA2Zjg2YWE2ODc4MDVmNzgyMGMwNzMwNGE4IiwidGFnIjoiIn0%3D; _ga_KWEQLWN5QH=GS1.1.1704082155.1.1.1704082168.0.0.0; v2board_session=eyJpdiI6IlV6VjhFUDlMSXJyOXgwU2F2aDd6RlE9PSIsInZhbHVlIjoiemFpS3IzVXNOQXJTTjZJblFlMTVrVmQyRndEeFMvWGRpNFJRMzgxK0cxWlJOZVlFV1F5Q0xoSkdxMVlTYXV2VVpic0FDNFpBa21WVkcvbUU4ODI3WHhLcGNlV3FLUHFGWFBiem8rbUdBUUlmM3dPVkwzbCtJWnhZSWg2bUpFUUciLCJtYWMiOiJjY2U0ZDJiMjU3Mzg0NzRiOTA1NTE2MjVlMGU2MGQwOWRlOWE3Y2M5ZDVkODViOWI5YjdkNDcwNzhjMTljNTRkIiwidGFnIjoiIn0%3D",
  "Origin":"https://data.mang5g.me",
  "Pragma":"no-cache",
  "Referer":"https://data.mang5g.me/",
  "Sec-Ch-Ua":"\"Not_A Brand\";v=\"8\", \"Chromium\";v=\"120\"",
  "Sec-Ch-Ua-Mobile":"?1",
  "Sec-Ch-Ua-Platform":"Android",
  "Sec-Fetch-Dest":"empty",
  "Sec-Fetch-Mode":"cors",
  "Sec-Fetch-Site":"same-origin",
  "User-Agent":"Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36",
}

data = {
    "trade_no": "2024010111015547357",
    "method": 1
}
os.system('clear')
while True:
  cc = requests.post(url=url, header=header, data=data)
  print("Thành Công!")
  sleep(600)
