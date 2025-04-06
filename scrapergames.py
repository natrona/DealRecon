# scrapergames.py
# Desenvolvido por Ruše
# Script para coletar promoções de jogos
# GitHub: https://github.com/Natrona/DealRecon

import requests
from bs4 import BeautifulSoup

def coletar_ofertas_steam():
    print("=== OFERTAS ATUAIS DA STEAM ===")
    try:
        url = "https://store.steampowered.com/search/?specials=1"
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')

        jogos = soup.find_all('div', class_='responsive_search_name_combined')

        if not jogos:
            print("Nenhuma oferta encontrada. A estrutura da página pode ter mudado.")
            return

        for i, jogo in enumerate(jogos[:5]):
            titulo_tag = jogo.find('span', class_='title')
            preco_tag = jogo.find_next('div', class_='search_price_discount_combined')

            titulo = titulo_tag.text.strip() if titulo_tag else 'Sem título'
            preco = preco_tag.text.strip() if preco_tag else 'Preço não encontrado'

            print(f"{titulo} - {preco}")

    except Exception as e:
        print("Erro ao coletar dados da Steam:", e)

def main():
    coletar_ofertas_steam()

    print("\n=== EPIC GAMES GRÁTIS ===")
    print("LISA: Definitive Edition - GRÁTIS")
    print("Cat Quest II - GRÁTIS")

    print("\n=== GOG PROMOÇÕES ===")
    print("Ver promoções direto no site: https://www.gog.com/games?price=discounted&sort=popularity")

if __name__ == "__main__":
    main()
