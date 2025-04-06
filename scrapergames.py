# scrapergames.py
# Desenvolvido por Ruše | github.com/Natrona/DealRecon

import requests
from datetime import datetime

def espacamento(texto, largura=60):
    return texto.center(largura)

def titulo(texto):
    print("\n" + espacamento(f"[ {texto} ]") + "\n")

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
                ofertas.append(f"- {nome}\n  De: R${preco_o:.2f} | Por: R${preco_n:.2f} ({desc}% OFF)")
        if not ofertas:
            print(espacamento("Nenhuma oferta encontrada."))
        else:
            for o in ofertas[:10]: print(espacamento(o))
        return ofertas
    except Exception as e:
        print(espacamento(f"Erro ao acessar SteamSpy: {e}"))
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
                gratis.append(f"- {j['title']} (GRÁTIS)")
        if not gratis:
            print(espacamento("Nenhum jogo grátis no momento."))
        else:
            for g in gratis: print(espacamento(g))
        return gratis
    except Exception as e:
        print(espacamento(f"Erro ao acessar Epic: {e}"))
        return []

def gerar_arquivos(steam, epic):
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    txt_nome = f"ofertas_{timestamp}.txt"
    html_nome = f"ofertas_{timestamp}.html"

    with open(txt_nome, "w", encoding="utf-8") as arq:
        arq.write("[ OFERTAS DA STEAM ]\n")
        arq.write("\n".join(steam) + "\n\n")
        arq.write("[ GRÁTIS NA EPIC GAMES ]\n")
        arq.write("\n".join(epic) + "\n\n")
        arq.write("[ GOG PROMOÇÕES ]\n")
        arq.write("https://www.gog.com/games?price=discounted&sort=popularity\n")

    with open(html_nome, "w", encoding="utf-8") as arq:
        arq.write("<html><head><meta charset='utf-8'><title>Ofertas</title></head><body style='font-family:sans-serif;background:#111;color:#eee;padding:20px;'>")
        arq.write("<h2>Ofertas da Steam</h2><ul>")
        for item in steam: arq.write(f"<li>{item.replace('\n', '<br>')}</li>")
        arq.write("</ul><h2>Grátis na Epic Games</h2><ul>")
        for item in epic: arq.write(f"<li>{item}</li>")
        arq.write("</ul><h2>GOG Promoções</h2>")
        arq.write("<p><a href='https://www.gog.com/games?price=discounted&sort=popularity' style='color:#6cf;'>Clique aqui</a></p>")
        arq.write("</body></html>")

    print("\n" + espacamento(f"Arquivos salvos: {txt_nome}, {html_nome}\n"))

def menu():
    while True:
        titulo("MENU")
        print(espacamento("1 - Ver ofertas da Steam"))
        print(espacamento("2 - Ver jogos grátis na Epic Games"))
        print(espacamento("3 - Gerar arquivos de ofertas"))
        print(espacamento("4 - Sair"))
        op = input("\nEscolha uma opção: ")

        if op == "1":
            coletar_ofertas_steam()
        elif op == "2":
            coletar_epic_games()
        elif op == "3":
            steam = coletar_ofertas_steam()
            epic = coletar_epic_games()
            gerar_arquivos(steam, epic)
        elif op == "4":
            print("\n" + espacamento("Encerrando o programa.") + "\n")
            break
        else:
            print(espacamento("Opção inválida."))

if __name__ == "__main__":
    menu()
