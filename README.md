# DealRecon - Scraper de Ofertas de Games 🎮🔥  
**por [Ruše] | GitHub: [Natrona](https://github.com/Natrona)**  

![Banner](https://cdn.cloudflare.steamstatic.com/store/home/store_home_share.jpg)

---

## ✨ Sobre o Projeto
**DealRecon** é um script simples e direto que busca promoções de jogos em lojas populares como:

<p align="center">
  <img src="https://upload.wikimedia.org/wikipedia/commons/8/83/Steam_icon_logo.svg" width="50" />
  <img src="https://upload.wikimedia.org/wikipedia/commons/3/31/Epic_Games_logo.svg" width="50" />
  <img src="https://upload.wikimedia.org/wikipedia/commons/f/f8/GOG.com_logo.svg" width="50" />
</p>

---

## ⚙️ Tecnologias Usadas
- **Python 3**
- **Terminal/Termux**
- (Futuramente) **Requests + BeautifulSoup**

---

## ✅ Requisitos
- Python 3 instalado
- Termux no Android ou terminal no PC

---

## 🚀 Como Usar no Termux

```bash
# Atualize pacotes e instale dependências
pkg update && pkg upgrade
pkg install git python -y

# Clone este repositório
git clone https://github.com/Natrona/DealRecon.git
cd DealRecon

# Rode o script
python scraper_games.py
