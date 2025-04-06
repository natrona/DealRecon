# DealRecon - Scraper de Ofertas de Games 🔥  
**por [Ruše] | GitHub: [Natrona](https://github.com/Natrona)**  

![Banner Steam](https://cdn.cloudflare.steamstatic.com/steam/clusters/frontpage/9c6de16c3e54ba029ac3a882d7d5ffcc720ee880.store_home_share.jpg)
![Banner Epic](https://cdn2.unrealengine.com/egs-store-home-carousel-1920x1080-1920x1080-225100f86c2b.jpg)
![Banner GOG](https://items.gog.com/news/gogcom.png)

---

## ✨ Sobre o Projeto
**DealRecon** é um script simples e direto que coleta as promoções mais quentes de jogos nas principais lojas digitais:

- Steam
- Epic Games
- GOG

Ideal para gamers caçadores de ofertas!

---

## ⚙️ Tecnologias Usadas
- **Python 3**
- **Terminal/Termux**
- (Futuramente) **Requests + BeautifulSoup para automação real**

---

## ✅ Requisitos
- Python 3 instalado
- Termux (no Android) ou terminal com Git e Python

---

## 🚀 Como Usar no Termux

```bash
# Atualize pacotes e instale o Python e Git
pkg update && pkg upgrade
pkg install git python -y

# Clone o repositório
git clone https://github.com/Natrona/DealRecon.git
cd DealRecon

# Rode o script
python scrapergames.py
