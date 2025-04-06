# scrapergames.py
# Desenvolvido por Ruše | github.com/Natrona/DealRecon

import requests
import json
import time
import sys
from datetime import datetime

def centralizar(texto, largura=60):
    return texto.center(largura)

def titulo(texto):
    print("\n" + centralizar(texto))
    print(centralizar("-" * len(texto)) + "\n")

def animacao_inicio():
    texto = "Carregando DealRecon"
    for i in range(4):
        sys.stdout.write("\r" + centralizar(texto + "." * i))
        sys.stdout.flush()
        time.sleep(0.5)
    print("\n" + centralizar("Bem-vindo ao DealRecon!\n"))

def coletar_ofertas_steam():
    titulo("OFERTAS DA STEAM")
    try:
        r = requests.get("https://steamspy.com/api.php?request=top100in2weeks")
        data = r.json()
        ofertas = []
        for jogo in data.values():
            p_original = int(jogo["initialprice"])
            p_atual = int(jogo["price"])
            if p_original > p_atual:
                nome = jogo["name"]
                preco_o = p_original / 100
                preco_n = p_atual / 100
                desc = 100 - int((preco_n / preco_o) * 100)
                ofertas.append(f"{nome} - R${preco_o:.2f} → R${preco_n:.2f} ({desc}% OFF)")
        if not ofertas:
            print(centralizar("Nenhuma oferta encontrada."))
        else:
            for o in ofertas[:10]: print(centralizar(o))
        return ofertas
    except Exception as e:
        print(centralizar(f"Erro ao acessar SteamSpy: {e}"))
        return []

def coletar_epic_games():
    titulo("GRÁTIS NA EPIC GAMES")
    try:
        r = requests.get("https://store-site-backend-static.ak.epicgames.com/freeGamesPromotions?locale=pt-BR")
        data = r.json()
        jogos = data["data"]["Catalog"]["searchStore"]["elements"]
        gratis = []
        for j in jogos:
            if j["price"]["totalPrice"]["discountPrice"] == 0:
                gratis.append(j["title"] + " - GRÁTIS")
        if not gratis:
            print(centralizar("Nenhum jogo grátis no momento."))
        else:
            for g in gratis: print(centralizar(g))
        return gratis
    except Exception as e:
        print(centralizar(f"Erro ao acessar Epic: {e}"))
        return []

def gerar_txt(steam, epic):
    nome = f"ofertas_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    with open(nome, "w", encoding="utf-8") as arq:
        arq.write("OFERTAS DA STEAM\n")
        arq.write("\n".join(steam) + "\n\n")
        arq.write("GRÁTIS NA EPIC GAMES\n")
        arq.write("\n".join(epic) + "\n\n")
        arq.write("GOG PROMOÇÕES\n")
        arq.write("https://www.gog.com/games?price=discounted&sort=popularity\n")
    print(centralizar(f"Arquivo salvo: {nome}"))

def menu():
    while True:
        titulo("MENU DEALRECON")
        print(centralizar("1 - Ver ofertas da Steam"))
        print(centralizar("2 - Ver grátis na Epic"))
        print(centralizar("3 - Gerar arquivo .txt"))
        print(centralizar("4 - Sair"))
        op = input("\nEscolha uma opção: ")

        if op == "1":
            coletar_ofertas_steam()
        elif op == "2":
            coletar_epic_games()
        elif op == "3":
            steam = coletar_ofertas_steam()
            epic = coletar_epic_games()
            gerar_txt(steam, epic)
        elif op == "4":
            print(centralizar("Até logo!"))
            break
        else:
            print(centralizar("Opção inválida!"))

if __name__ == "__main__":
    animacao_inicio()
    menu()
