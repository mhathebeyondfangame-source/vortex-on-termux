import os
import sys
import subprocess

# --- INSTALLATION AUTOMATIQUE DE REQUIREMENTS.TXT ---
def auto_install_requirements():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    req_file = os.path.join(current_dir, "requirements.txt")
    if os.path.exists(req_file):
        print("Installation / Verification des dependances necessaires...")
        try:
            # Execute automatiquement 'pip install -r requirements.txt'
            subprocess.run([sys.executable, "-m", "pip", "install", "-r", req_file], check=True)
            print("Dependances pretes !\n")
        except Exception as e:
            print(f"[ERREUR] Impossible d'installer automatiquement : {e}\n")

# Lancement de l'installation automatique des le debut
auto_install_requirements()

# --- RESTE DU CODE DE MAIN.PY ---
import time
import json
import zipfile

def clear_screen():
    os.system('clear' if os.name != 'nt' else 'cls')

def print_banner_by():
    print("""
 BBBB   Y   Y   T T T T T  S S S S  U   U  K   K  I I I  E E E E  T T T T T  I I I  C C C C
 B   B   Y Y        T      S        U   U  K  K     I    E            T        I    C      
 BBBB     Y         T      S S S S  U   U  K K      I    E E E        T        I    C      
 B   B    Y         T            S  U   U  K  K     I    E            T        I    C      
 BBBB     Y         T      S S S S   UUU   K   K  I I I  E E E E      T      I I I  C C C C
""")

def progress_bar(lang):
    text = "Chargement [" if lang == "FR" else "Loading ["
    print(text, end="", flush=True)
    for _ in range(20):
        time.sleep(0.05)
        print("##", end="", flush=True)
    done_text = "] Termine!" if lang == "FR" else "] Done!"
    print(done_text)

def init_animation():
    print("Initialisation du systeme... / System initialization...")
    time.sleep(1)
    clear_screen()
    if os.name != 'nt':
        os.system("ls -la /")
    time.sleep(2)
    clear_screen()
    
    print_banner_by()
    time.sleep(3)
    clear_screen()
    
    print("============================================================")
    print("       V O R T E X    T O O L S    I N I T I A L I S E")
    print("============================================================")
    time.sleep(2)

def extract_zip_if_needed(target_dir):
    """ Decompresse vortex.zip s'il est present """
    zip_path = os.path.join(target_dir, "vortex.zip")
    if os.path.exists(zip_path):
        print("Decompression de vortex.zip...")
        try:
            with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                zip_ref.extractall(target_dir)
            print("Decompression terminee !")
            time.sleep(1)
        except Exception as e:
            print(f"[ERREUR] Impossible de decompresser vortex.zip : {e}")

def find_file_recursive(base_path, keyword):
    for root, dirs, files in os.walk(base_path):
        for file in files:
            if keyword.lower() in file.lower() and file.endswith('.py'):
                if file.lower() != "main.py":
                    return os.path.join(root, file)
    return None

def main():
    init_animation()

    current_dir = os.path.dirname(os.path.abspath(__file__))
    extract_zip_if_needed(current_dir)

    tools_dir = current_dir
    config_file = os.path.join(current_dir, "config.json")

    config = {}
    if os.path.exists(config_file):
        try:
            with open(config_file, 'r', encoding='utf-8') as f:
                config = json.load(f)
        except Exception:
            pass

    lang = config.get("LANG")
    if not lang:
        clear_screen()
        print("============================================================")
        print(" SELECTION DE LA LANGUE / LANGUAGE SELECTION")
        print("============================================================")
        print("1. Francais")
        print("2. English")
        print("============================================================")
        choice_lang = input("Choix / Choice (1-2) : ").strip()
        lang = "EN" if choice_lang == "2" else "FR"

        save_msg = "Voulez-vous sauvegarder ces parametres ? (O/N) : " if lang == "FR" else "Save settings? (Y/N) : "
        save_opt = input(save_msg).strip().upper()
        if save_opt in ["O", "Y"]:
            config["LANG"] = lang
            with open(config_file, 'w', encoding='utf-8') as f:
                json.dump(config, f, indent=4)
            print("Sauvegarde effectuee !" if lang == "FR" else "Saved!")
            time.sleep(1)

    dox_dir = os.path.join(os.path.expanduser("~"), "Documents", "dox", "Informations")
    os.makedirs(dox_dir, exist_ok=True)
    contacts_file = os.path.join(dox_dir, "contacts_test.txt")
    if not os.path.exists(contacts_file):
        open(contacts_file, 'w', encoding='utf-8').close()

    while True:
        clear_screen()
        print("============================================================")
        if lang == "FR":
            print("    GESTIONNAIRE D'INFORMATIONS")
            print("============================================================")
            print("1. Recherche")
            print("2. Recherche sur le web")
            print("3. PDM (Outil Zip)")
            print("4. Generateur de liens avec pseudo")
            print("5. Generateur de Codes")
            print("6. Email Bombe")
            print("7. Nitro Gen")
            print("8. Recuperer IP d'un site")
            print("9. Scanner de ports reseau")
            print("10. Sodde")
            print("11. Quitter le script")
            print("============================================================")
            choix = input("Votre choix (1-11) : ").strip()
        else:
            print("    INFORMATION MANAGER")
            print("============================================================")
            print("1. Search")
            print("2. Web Search")
            print("3. PDM (Zip Tool)")
            print("4. Username Link Generator")
            print("5. Code Generator")
            print("6. Email Bomb")
            print("7. Nitro Gen")
            print("8. Site IP Lookup")
            print("9. Network Port Scanner")
            print("10. Sodde")
            print("11. Exit")
            print("============================================================")
            choix = input("Your choice (1-11) : ").strip()

        if choix == "1":
            clear_screen()
            mot = input("Nom ou numero a chercher : " if lang == "FR" else "Name or number : ")
            if os.path.exists(contacts_file):
                with open(contacts_file, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read()
                blocks = content.split('Pr')
                for b in blocks:
                    if mot.lower() in b.lower():
                        print(f"\033[92m{b}\033[0m")
                        print("--------------------------------")
            input("\nAppuyez sur Entree pour continuer...")

        elif choix == "2":
            clear_screen()
            req = input("Recherche Google : " if lang == "FR" else "Google Search : ")
            url = f"https://www.google.com/search?q={req}"
            os.system(f"termux-open-url '{url}' 2>/dev/null || xdg-open '{url}' 2>/dev/null")

        elif choix in ["5", "6", "7", "10"]:
            clear_screen()
            progress_bar(lang)
            target = {
                "5": "generateur",
                "6": "bombe",
                "7": "nitro",
                "10": "sodde"
            }[choix]
            
            script_path = find_file_recursive(tools_dir, target)
            if script_path:
                print(f"Lancement de {target}...")
                subprocess.run([sys.executable, script_path])
            else:
                print(f"[ERREUR] Script introuvable pour '{target}' dans : {tools_dir}")
            input("\nAppuyez sur Entree pour continuer...")

        elif choix == "4":
            clear_screen()
            pseudo = input("Entrez le pseudo : " if lang == "FR" else "Enter username : ")
            print(f"\nRoblox    : https://www.roblox.com/users/profile?username={pseudo}")
            print(f"Pinterest : https://www.pinterest.com/{pseudo}/")
            print(f"YouTube   : https://www.youtube.com/@{pseudo}")
            print(f"Instagram : https://www.instagram.com/{pseudo}/")
            print(f"X (Twitter): https://x.com/{pseudo}")
            print(f"Twitch    : https://www.twitch.tv/{pseudo}\n")
            input("Appuyez sur Entree pour continuer...")

        elif choix == "8":
            clear_screen()
            domain = input("Domaine (ex: google.com) : ")
            progress_bar(lang)
            os.system(f"nslookup {domain}")
            input("\nAppuyez sur Entree pour continuer...")

        elif choix == "9":
            clear_screen()
            os.system("netstat -tuln || ss -tuln")
            input("\nAppuyez sur Entree pour continuer...")

        elif choix == "11":
            sys.exit()

# --- EXECUTION DU MAIN ---
if __name__ == "__main__":
    main()