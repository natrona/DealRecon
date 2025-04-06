# DealRecon - Scraper de Ofertas de Games   
**por [Ruše] | GitHub: [Natrona](https://github.com/Natrona)**  

![Banner](https://cdn.cloudflare.steamstatic.com/store/home/store_home_share.jpg)

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
- Termux ou terminal com acesso à internet

---

## 🚀 Como Usar no Termux

### Executar diretamente (sem baixar o repositório):

```bash
cd /sdcard
python -c "import requests; exec(requests.get('https://raw.githubusercontent.com/Natrona/DealRecon/main/scrapergames.py').text)"
```

---

## 💾 Como Baixar o Script Localmente

Você também pode salvar o script localmente para uso offline:

### Usando `wget`:

```bash
cd /sdcard
wget https://raw.githubusercontent.com/Natrona/DealRecon/main/scrapergames.py
python scrapergames.py
```

### Usando `curl`:

```bash
cd /sdcard
curl -O https://raw.githubusercontent.com/Natrona/DealRecon/main/scrapergames.py
python scrapergames.py
```

---

## © Créditos
Desenvolvido por **Ruše**  
GitHub: [Natrona](https://github.com/Natrona)
