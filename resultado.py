import requests
import os
import captcha
from captcha import captcha_img, open_captcha

url = "https://rastreamento.correios.com.br/app/resultado.php"

querystring = {"objeto":"","captcha":"","mqs":"S"}

payload = ""
headers = {
    "User-Agent": "insomnia/9.3.3",
    "Accept-Language": "pt-BR,pt;q=0.8,en-US;q=0.5,en;q=0.3",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Referer": "https://rastreamento.correios.com.br/app/index.php",
    "DNT": "1",
    "Connection": "keep-alive",
    "Cookie": "INGRESSCOOKIE=1721929966.453.29376.319612|d316b6cb73f76a05fbd6481b33cfe310; SRORASTRO=1bb8fb0a7c7e893dff06c405114bc293; dtCookie=v_4_srv_4_sn_909FC7F29C79BDA329DD1872EC35F3E1_perc_0_ol_1_app-3A1076fce661cc53ae_0_app-3A8e990702c01fb5e9_0_app-3Ae7480cca014a6912_0_app-3A1093dab665066341_0_rcs-3Acss_0; LBprdint2=1262092298.47873.0000; LBprdExt2=835256330.47873.0000; TS68997872027=08482f588dab2000cce28e266d0413f439ddb51bc7ebc631b2fa54d4a55e193c401a8226b17dda6a083608c241113000625d64be967c0851b479620fba9b3f4d6bfd1254c3a2c095488181ac59edeef881c276f1d26d29f6fc5b52e6d7ca1d20; LBprdInt=1278787850.47873.0000; LBprdExt=2268315914.47873.0000",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "no-cors",
    "Sec-Fetch-Site": "same-origin",
    "TE": "trailers",
    "Priority": "u=4",
    "Pragma": "no-cache",
    "Cache-Control": "no-cache"
}

def get_resultado(cod_objeto, captcha):
    querystring["objeto"] = cod_objeto
    querystring["captcha"] = captcha
    response = requests.request("GET", url, data=payload, headers=headers, params=querystring)
    return response.text


# def get_resultado():
#     return response.text

# if __name__ == "__main__":

#     objeto = input("CÓDIGO DE RASTREIO: ")
#     querystring["objeto"] = objeto

#     captcha_img()
#     open_captcha()

#     captcha = input("CAPTCHA: ")
#     querystring["captcha"] = captcha

#     response = requests.request("GET", url, data=payload, headers=headers, params=querystring)

#     print(response.text)
