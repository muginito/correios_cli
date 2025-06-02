import requests
import shutil
import os

url = "https://rastreamento.correios.com.br/core/securimage/securimage_show.php"

querystring = {"0.16719525520571643":""}

payload = ""
headers = {
    "User-Agent": "insomnia/9.3.3",
    "Host": "rastreamento.correios.com.br",
    "Accept": "image/avif,image/webp,image/png,image/svg+xml,image/*;q=0.8,*/*;q=0.5",
    "Accept-Language": "pt-BR,pt;q=0.8,en-US;q=0.5,en;q=0.3",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "DNT": "1",
    "Connection": "keep-alive",
    "Referer": "https://rastreamento.correios.com.br/app/index.php",
    "Cookie": "INGRESSCOOKIE=1721929966.453.29376.319612|d316b6cb73f76a05fbd6481b33cfe310; SRORASTRO=1bb8fb0a7c7e893dff06c405114bc293; dtCookie=v_4_srv_4_sn_909FC7F29C79BDA329DD1872EC35F3E1_perc_0_ol_1_app-3A1076fce661cc53ae_0_app-3A8e990702c01fb5e9_0_app-3Ae7480cca014a6912_0_app-3A1093dab665066341_0_rcs-3Acss_0; LBprdint2=1262092298.47873.0000; LBprdExt2=835256330.47873.0000; TS68997872027=08482f588dab2000d0a0e4f404fbe0125c0487a99a1fd4b9552750f86c2d611b67cc6117a3fdff12087168c6d51130006c611b71e548807562984fd617ec496857baad40a305ab271929639fe911b38bcf92c4b3e1c77d9fe71d18910223ebe2; LBprdInt=1278787850.47873.0000; LBprdExt=2268315914.47873.0000",
    "Sec-Fetch-Dest": "image",
    "Sec-Fetch-Mode": "no-cors",
    "Sec-Fetch-Site": "same-origin",
    "Priority": "u=5, i",
    "TE": "trailers"
}
def get_response():
    response = requests.request("GET", url, data=payload, headers=headers, params=querystring, stream=True)
    return response

def captcha_img():
    response = get_response()
    with open("./captcha/img.jpg", 'wb') as f:
        response.raw.decode_content = True
        shutil.copyfileobj(response.raw, f)

def open_captcha():
    os.startfile("img.jpg", cwd= "captcha")

def remove_captcha():
    os.remove("./captcha/img.jpg")
