import requests

headers = { 'User-Agent': 'Mozilla/5.0 (Linux; Android 10; SM-G975F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Mobile Safari/537.36'}

url = 'https://dev-br.naas.huaweicloud.com:19008/portalpage/b53e444840e043f3acbcb4c1a770290a/20230130145533/pc/auth.html?apmac=f83e95d99b80&uaddress=172.24.22.13&umac=ac198e845abc&authType=1&lang=en_US&ssid=R3Vlc3QtRWR1Y2Eg&pushPageId=37a8de4f-da09-4820-93db-3d2ef0872fda'

while True:
    response = requests.get(url, headers=headers)
    print(response)