#!/usr/bin/env python3

from resultado import get_resultado
import json
import pandas as pd
from captcha import captcha_img, open_captcha

# def salva_encomenda(nome, codigo):
#     with open("./encomendas.json", "r+", encoding="utf-8") as f:
#         data = json.load(f)
#         if nome in data or codigo in data:
#             return True
#         json.dump({nome:codigo})
#         f.close()
#     return False

# def remove_num(o: str):
#     with open("./rastreamento/codigos-de-rastreio.json", "r+") as f:
#         data = json.load(f)

#         for i in data["objeto"]:
#             if o == i:

def existe_encomenda(nome, codigo):
    with open("./encomendas.json", "r") as fp:
        encomendas = json.load(fp)
        print(encomendas)

# def salva_encomenda(nome, codigo):





if __name__ == "__main__":
    opt = 0
    menu = "\n1 - Nova encomenda\n \
2 - Exibir encomendas\n \
3 - Sair\n"
    while(opt != 3):

        opt = int(input(menu))

        if opt == 1:
            codigo_encomenda = input("\nCÓDIGO DE RASTREIO: ")
            nome_encomenda = input("\nNOME PARA ENCOMENDA: ")
            if salva_encomenda(nome_encomenda, codigo_encomenda):
                print("\nNome para encomenda ou código de rastreio já existem\n")
                continue
            else:
                print("\nEncomenda registrada com sucesso\n")
                continue
        if opt == 2:
            print("\nEscolha sua encomenda: ")
            print(json.load(open("./encomendas.json", "r")))




    # objeto = input("CÓDIGO DE RASTREIO: ")

    # if salva_encomenda(objeto)

    # captcha_img()
    # open_captcha()
    # captcha = input("CAPTCHA: ")

    # resultado = get_resultado(objeto, captcha)

    # print(resultado)
