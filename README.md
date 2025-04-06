# DealRecon - Scraper de Ofertas de Games 🎮🔥  
**por [Ruše] | GitHub: [Natrona](https://github.com/Natrona)**  

<img src="https://upload.wikimedia.org/wikipedia/commons/8/83/Steam_icon_logo.svg" width="120" height="120"> 
<img src="https://upload.wikimedia.org/wikipedia/commons/3/31/Epic_Games_logo.svg" width="120" height="120">
<img src="https://upload.wikimedia.org/wikipedia/commons/2/29/GOG.com_Logo_2019.svg" width="120" height="120">

---

## ✨ Sobre o Projeto
**DealRecon** é um script simples que coleta promoções quentes de jogos nas principais lojas digitais:

- Steam
- Epic Games
- GOG

Ideal para gamers que querem economizar!

---

## ⚙️ Tecnologias Usadas
- **Python 3**
- **Terminal/Termux**
- (Futuramente) **Requests + BeautifulSoup para scraping real**

---

## ✅ Requisitos
- Python 3 instalado
- Termux ou terminal com Git e Python

---

## 🚀 Como Usar no Termux

```bash
# Atualizar pacotes e instalar Git e Python
pkg update && pkg upgrade
pkg install git python -y

# Clonar o repositório
git clone https://github.com/Natrona/DealRecon.git
cd DealRecon

# Executar o script
python scrapergames.py
