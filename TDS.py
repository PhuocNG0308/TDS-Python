import certifi
import ssl
import requests
import json
import urllib
import time
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry


def process_recaptcha(tiktok_id, tds_token):
    anchorr = "https://www.google.com/recaptcha/api2/anchor?ar=1&k=6Le-MTEiAAAAAHkuafFvPG9y9d4HU-fzxmmGsGV_&co=aHR0cHM6Ly90cmFvZG9pc3ViLmNvbTo0NDM.&v=zIriijn3uj5Vpknvt_LnfNbF&size=invisible"
    anchorr = anchorr.strip()
    keysite = "6Le-MTEiAAAAAHkuafFvPG9y9d4HU-fzxmmGsGV_"
    var_co = "aHR0cHM6Ly90cmFvZG9pc3ViLmNvbTo0NDM."
    var_v = "zIriijn3uj5Vpknvt_LnfNbF"

    r1 = requests.get(anchorr, verify=False).text
    token1 = r1.split('recaptcha-token" value="')[1].split('">')[0]

    var_chr = ""
    var_vh = ""
    var_bg = ""

    payload = {
        "v": var_v,
        "reason": "q",
        "c": token1,
        "k": keysite,
        "co": var_co,
        "hl": "en",
        "size": "invisible",
        "chr": var_chr,
        "vh": var_vh,
        "bg": var_bg
    }

    r2 = requests.post(f"https://www.google.com/recaptcha/api2/reload?k={keysite}", data=payload, verify=False)
    try:
        token2 = str(r2.text.split('"rresp","')[1].split('"')[0])
    except Exception as e:
        token2 = 'null'
    
    if token2 == 'null':
        print("Không thể lấy token reCAPTCHA.")
        return False;

    url = f"https://traodoisub.com/api/?fields=tiktok_run&id={tiktok_id}&access_token={tds_token}"
    data = {
        "recaptcha_response": token2
    }

    response = requests.post(url, data=data, verify=False)
    if response.status_code != 200:
        print("Lỗi khi gửi reCAPTCHA.")
        return False;

    response_data = json.loads(response.text)

    # Kiểm tra nếu có key 'error'
    if 'error' in response_data:
        return False

    print(response.text)

    return True;
