# DealRecon - Scraper de Ofertas de Games 🎮🔥  
**por [Ruše] | GitHub: [Natrona](https://github.com/Natrona)**  

![Steam Banner](https://i.imgur.com/RFjzSxg.png)  
![Epic Games Banner](https://i.imgur.com/f3SbhKx.png)  
![GOG Banner](https://i.imgur.com/Z7UUbGK.png)

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
