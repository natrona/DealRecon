import requests

def steamspy_ofertas():
    print("=== OFERTAS ATUAIS DA STEAM ===")
    try:
        url = "https://steamspy.com/api.php?request=top100in2weeks"
        response = requests.get(url)
        data = response.json()

        count = 0
        for appid in data:
            jogo = data[appid]
            if jogo["initialprice"] > jogo["price"]:
                nome = jogo["name"]
                preco_original = jogo["initialprice"] / 100
                preco_atual = jogo["price"] / 100
                print(f"{nome} - R${preco_original:.2f} -> R${preco_atual:.2f}")
                count += 1
                if count >= 5:
                    break

    except Exception as e:
        print("Erro ao acessar SteamSpy:", e)

steamspy_ofertas()
