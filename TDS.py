import certifi
import ssl
import requests
import json
import urllib
import time
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

'''
def get_recaptcha_anchor():
    url = "https://www.google.com/recaptcha/api2/anchor"
    
    # Các tham số query string
    params = {
        "ar": "1",
        "k": "6Le-MTEiAAAAAHkuafFvPG9y9d4HU-fzxmmGsGV_",
        "co": "aHR0cHM6Ly90cmFvZG9pc3ViLmNvbTo0NDM.",
        "hl": "vi",
        "v": "zIriijn3uj5Vpknvt_LnfNbF",
        "size": "invisible",
        "cb": "to22dfj5q3z"
    }
    
    # Headers của request
    headers = {
        "sec-ch-ua": '"Chromium";v="124", "Android WebView";v="124", "Not-A.Brand";v="99"',
        "sec-ch-ua-mobile": "?1",
        "sec-ch-ua-platform": '"Android"',
        "upgrade-insecure-requests": "1",
        "user-agent": "Mozilla/5.0 (Linux; Android 9; SM-N971N Build/PQ3B.190801.10101846; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/124.0.6367.82 Mobile Safari/537.36",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "x-requested-with": "com.songloimr.tdstiktok",
        "sec-fetch-site": "cross-site",
        "sec-fetch-mode": "navigate",
        "sec-fetch-dest": "iframe",
        "accept-encoding": "gzip, deflate, br, zstd",
        "accept-language": "vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7",
        "priority": "u=0, i"
    }

    # Gửi GET request
    response = requests.get(url, headers=headers, params=params, verify= False)
    
    # Trả về nội dung response
    return response.text

# Gọi hàm và in ra kết quả
result = get_recaptcha_anchor()
print(result)
'''


anchorr = str(input("Anchor URL : "))
anchorr = anchorr.strip()
keysite = "6Le-MTEiAAAAAHkuafFvPG9y9d4HU-fzxmmGsGV_"
#anchorr.split('k=')[1].split("&")[0]
print(keysite)
#6Le-MTEiAAAAAHkuafFvPG9y9d4HU-fzxmmGsGV_
var_co = "aHR0cHM6Ly90cmFvZG9pc3ViLmNvbTo0NDM."
#anchorr.split("co=")[1].split("&")[0] 
print(var_co)
#aHR0cHM6Ly90cmFvZG9pc3ViLmNvbTo0NDM. 
var_v = "zIriijn3uj5Vpknvt_LnfNbF"
#anchorr.split("v=")[1].split("&")[0]
print(var_v)
#zIriijn3uj5Vpknvt_LnfNbF

r1 = requests.get(anchorr, verify= False).text

token1 = r1.split('recaptcha-token" value="')[1].split('">')[0]

var_chr = str(input("CHR ([xx, xx, xx]) : "))
var_vh = str(input("VH : "))
var_bg = str(input("BG : "))
var_chr = str(urllib.parse.quote(var_chr))
print("\n\nBypassing Recaptcha...")

payload = {
    "v":var_v,
    "reason":"q",
    "c":token1,
    "k":keysite,
    "co":var_co,
    "hl":"en",
    "size":"invisible",
    "chr":var_chr,
    "vh":var_vh,
    "bg":var_bg
}

r2 = requests.post("https://www.google.com/recaptcha/api2/reload?k={}".format(keysite), data=payload, verify=False)
try:
    token2 = str(r2.text.split('"rresp","')[1].split('"')[0])
except:
    token2 = 'null'

if token2 == "null":
    print("\nRecaptcha not vulnerable : \n\n"+str(r2.text))
else:
    print("\nRecaptcha Bypassed : \n\n"+str(token2))
    with open("bypassed.txt", "a") as file:
        file.write("RECAPTCHA BYPASSED\n\n\n\nAnchor : "+str(anchorr)+"\n\n\nReload : https://www.google.com/recaptcha/api2/reload?k="+str(keysite)+f"\n\nPayload : v={var_v}&reason=q&c=<token>&k={keysite}&co={var_co}&hl=en&size=invisible&chr={var_chr}&vh={var_vh}&bg={var_bg}")

print("RECAPTCHA BYPASSED\n\n\n\nAnchor : "+str(anchorr)+"\n\n\nReload : https://www.google.com/recaptcha/api2/reload?k="+str(keysite)+f"\n\nPayload : v={var_v}&reason=q&c=<token>&k={keysite}&co={var_co}&hl=en&size=invisible&chr={var_chr}&vh={var_vh}&bg={var_bg}")

url = "https://traodoisub.com/api/?fields=tiktok_run&id=phuocng0308&access_token=TDS0nIwEjclZXZzJiOiIXZ2V2ciwiIyEWOwM2b1hGchl2ZiojIyV2c1Jye"

data = {
    "recaptcha_response": token2
}

response = requests.post(url, data=data, verify=False)

print(response.status_code)
print(response.text)
#v=()&reason=q&c=<token>&k=()&co=()&hl=en&size=invisible&chr=()&vh=()&bg=()
