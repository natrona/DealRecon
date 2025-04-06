# scraper_games.py
# Desenvolvido por Ruše (@Natrona)
# Projeto: DealRecon - Coleta de ofertas de jogos

import os

# Cores ANSI
def color(text, code): return f"\033[{code}m{text}\033[0m"
green = lambda t: color(t, "92")
yellow = lambda t: color(t, "93")
cyan = lambda t: color(t, "96")
bold = lambda t: color(t, "1")

def print_header(title):
    print(bold("\n" + "=" * 40))
    print(bold(f"{title.center(40)}"))
    print(bold("=" * 40))

def main():
    os.system("clear")
    print(bold(cyan("DEALRECON - PROMOÇÕES DE GAMES")))
    print("-" * 40)

    print_header("STEAM OFERTAS")
    print(green("• ") + "Red Dead Redemption 2" + yellow("  R$299.90 ") + "→" + green(" R$74.97"))
    print(green("• ") + "Sons Of The Forest" + yellow("       R$88.99 ") + "→" + green(" R$35.59"))
    print(green("• ") + "Devil May Cry 5" + yellow("          R$99.00 ") + "→" + green(" R$24.75"))
    print(green("• ") + "Devil May Cry HD Collection" + yellow(" R$99.00 ") + "→" + green(" R$32.67"))

    print_header("EPIC GAMES GRÁTIS")
    print(green("• ") + "LISA: Definitive Edition" + yellow(" - GRÁTIS"))
    print(green("• ") + "Cat Quest II" + yellow("               - GRÁTIS"))

    print_header("GOG PROMOÇÕES")
    print("• Ver promoções direto no site:")
    print(cyan("  https://www.gog.com/games?price=discounted&sort=popularity"))

if __name__ == "__main__":
    main()
