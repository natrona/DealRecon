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
            preco_original = int(jogo["initialprice"])
            preco_atual = int(jogo["price"])
            if preco_original > preco_atual:
                nome = jogo["name"]
                print(f"{nome} - R${preco_original / 100:.2f} -> R${preco_atual / 100:.2f}")
                count += 1
                if count >= 5:
                    break

    except Exception as e:
        print("Erro ao acessar SteamSpy:", e)

steamspy_ofertas()
