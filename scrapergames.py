# scrapergames.py
# Desenvolvido por Ruše | github.com/Natrona/DealRecon

import requests
import json
from datetime import datetime
from colorama import Fore, Style, init
from reportlab.pdfgen import canvas
from textwrap import fill

init(autoreset=True)

def titulo(texto):
    return Fore.CYAN + Style.BRIGHT + texto.center(60)

def coletar_ofertas_steam():
    print(titulo("OFERTAS DA STEAM"))
    try:
        response = requests.get("https://steamspy.com/api.php?request=top100in2weeks")
        jogos = response.json()
        ofertas = []
        for jogo in jogos.values():
            if int(jogo['initialprice']) > int(jogo['price']):
                nome = jogo['name']
                preco_original = int(jogo['initialprice']) / 100
                preco_atual = int(jogo['price']) / 100
                desconto = 100 - int((preco_atual / preco_original) * 100)
                ofertas.append(f"{nome} - R${preco_original:.2f} → R${preco_atual:.2f} ({desconto:.0f}% OFF)")
        return ofertas[:10]
    except Exception as e:
        return [f"Erro ao acessar SteamSpy: {e}"]

def coletar_epic_games():
    print(titulo("JOGOS GRÁTIS NA EPIC GAMES"))
    try:
        response = requests.get("https://store-site-backend-static.ak.epicgames.com/freeGamesPromotions?locale=pt-BR")
        data = response.json()
        jogos = data['data']['Catalog']['searchStore']['elements']
        gratis = []
        for jogo in jogos:
            if jogo['price']['totalPrice']['discountPrice'] == 0:
                gratis.append(jogo['title'] + " - GRÁTIS")
        return gratis if gratis else ["Nenhum jogo grátis no momento."]
    except Exception as e:
        return [f"Erro ao acessar Epic Games: {e}"]

def gerar_txt(steam, epic):
    nome = f"ofertas_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    with open(nome, "w", encoding="utf-8") as f:
        f.write("OFERTAS DA STEAM\n")
        f.write("\n".join(steam) + "\n\n")
        f.write("JOGOS GRÁTIS NA EPIC GAMES\n")
        f.write("\n".join(epic) + "\n\n")
        f.write("GOG PROMOÇÕES\n")
        f.write("https://www.gog.com/games?price=discounted&sort=popularity\n")
    print(Fore.GREEN + f"Arquivo TXT salvo como: {nome}")

def gerar_pdf(steam, epic):
    nome = f"ofertas_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
    c = canvas.Canvas(nome)
    c.setFont("Helvetica", 12)
    y = 800
    c.drawString(200, y, "OFERTAS DE JOGOS")
    y -= 30

    c.drawString(50, y, "Steam:")
    y -= 20
    for item in steam:
        c.drawString(60, y, item)
        y -= 15

    y -= 15
    c.drawString(50, y, "Epic Games:")
    y -= 20
    for item in epic:
        c.drawString(60, y, item)
        y -= 15

    y -= 15
    c.drawString(50, y, "GOG Promoções: https://www.gog.com/games?price=discounted&sort=popularity")
    c.save()
    print(Fore.GREEN + f"Arquivo PDF salvo como: {nome}")

def menu():
    while True:
        print(titulo("MENU DEALRECON"))
        print("1 - Ver ofertas da Steam")
        print("2 - Ver jogos grátis da Epic")
        print("3 - Salvar ofertas em TXT")
        print("4 - Salvar ofertas em PDF")
        print("5 - Sair")
        op = input(Fore.YELLOW + "\nEscolha uma opção: ")
        if op == "1":
            ofertas = coletar_ofertas_steam()
            for o in ofertas: print(Fore.WHITE + o)
        elif op == "2":
            ofertas = coletar_epic_games()
            for o in ofertas: print(Fore.WHITE + o)
        elif op == "3":
            gerar_txt(coletar_ofertas_steam(), coletar_epic_games())
        elif op == "4":
            gerar_pdf(coletar_ofertas_steam(), coletar_epic_games())
        elif op == "5":
            print(Fore.CYAN + "Até logo!")
            break
        else:
            print(Fore.RED + "Opção inválida!")

if __name__ == "__main__":
    menu()
