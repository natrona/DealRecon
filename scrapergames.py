import requests
from bs4 import BeautifulSoup

def coletar_ofertas_steam():
    url = 'https://store.steampowered.com/search/?specials=1'
    headers = {
        'User-Agent': 'Mozilla/5.0'
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    ofertas = []
    for item in soup.find_all('a', class_='search_result_row'):
        titulo = item.find('span', class_='title').text
        preco_antigo = item.find('strike').text if item.find('strike') else 'N/A'
        preco_novo = item.find('div', class_='search_price').text.strip().split()[-1]
        desconto = item.find('div', class_='search_discount').text.strip()
        ofertas.append(f"{titulo} - {preco_antigo} -> {preco_novo} ({desconto})")

    return ofertas

def main():
    print("=== OFERTAS ATUAIS DA STEAM ===")
    ofertas = coletar_ofertas_steam()
    with open('ofertas.txt', 'w', encoding='utf-8') as f:
        for oferta in ofertas:
            print(oferta)
            f.write(oferta + '\n')

if __name__ == "__main__":
    main()
