# scrapergames.py
# Desenvolvido por Ruše | github.com/Natrona/DealRecon

import requests
import json
from datetime import datetime

def coletar_ofertas_steam():
    print("\n=== OFERTAS ATUAIS DA STEAM ===")
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
                ofertas.append(f"{nome} - R${preco_original:.2f} -> R${preco_atual:.2f} ({desconto:.0f}% OFF)")
        return ofertas[:10]
    except Exception as e:
        return [f"Erro ao acessar SteamSpy: {e}"]

def coletar_epic_games():
    print("\n=== EPIC GAMES GRÁTIS ===")
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

def gerar_arquivo(steam, epic):
    nome_arquivo = f"ofertas_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    with open(nome_arquivo, "w", encoding="utf-8") as f:
        f.write("=== OFERTAS ATUAIS DA STEAM ===\n")
        for item in steam:
            f.write(item + "\n")
        f.write("\n=== EPIC GAMES GRÁTIS ===\n")
        for item in epic:
            f.write(item + "\n")
        f.write("\n=== GOG PROMOÇÕES ===\n")
        f.write("Ver promoções: https://www.gog.com/games?price=discounted&sort=popularity\n")
    print(f"\nArquivo salvo como: {nome_arquivo}")

def menu():
    while True:
        print("\n====== DealRecon Menu ======")
        print("1 - Ver ofertas da Steam")
        print("2 - Ver jogos grátis da Epic Games")
        print("3 - Gerar arquivo com todas ofertas")
        print("4 - Sair")
        escolha = input("Escolha uma opção: ")
        if escolha == "1":
            ofertas = coletar_ofertas_steam()
            for o in ofertas: print(o)
        elif escolha == "2":
            ofertas = coletar_epic_games()
            for o in ofertas: print(o)
        elif escolha == "3":
            steam = coletar_ofertas_steam()
            epic = coletar_epic_games()
            gerar_arquivo(steam, epic)
        elif escolha == "4":
            print("Encerrando...")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    menu()
