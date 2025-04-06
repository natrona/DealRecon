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

## 🚀 Como Usar

### 1. Executar diretamente (sem baixar nada):

```bash
cd /sdcard
python -c "import requests; exec(requests.get('https://raw.githubusercontent.com/Natrona/DealRecon/main/scrapergames.py').text)"
```

---

### 2. Baixar o script individualmente (uso offline)

#### Usando `wget`:

```bash
cd /sdcard
wget https://raw.githubusercontent.com/Natrona/DealRecon/main/scrapergames.py
python scrapergames.py
```

#### Usando `curl`:

```bash
cd /sdcard
curl -O https://raw.githubusercontent.com/Natrona/DealRecon/main/scrapergames.py
python scrapergames.py
```

---

### 3. Clonar o repositório completo

```bash
# Atualizar pacotes e instalar Git e Python (no Termux)
pkg update && pkg upgrade
pkg install git python -y

# Clonar o repositório
cd /sdcard
git clone https://github.com/Natrona/DealRecon.git
cd DealRecon

# Executar o script
python scrapergames.py
```

---

## © Créditos
Desenvolvido por **Ruše**  
GitHub: [Natrona](https://github.com/Natrona)
