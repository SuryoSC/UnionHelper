import time
import os
from termcolor import colored
from pyfiglet import Figlet

def helper():
    os.system('cls' if os.name == 'nt' else 'clear')
    f = Figlet(font='slant')
    title = f.renderText("  UnionHelper")
    print("─" * 70)
    print(colored(title, "red"))
    print("─" * 70)
    print()
    try:
        awal = int(input("Masukkan angka awal  : "))
        akhir = int(input("Masukkan angka akhir : "))
        hasil = ",".join(str(i) for i in range(awal, akhir + 1))
        print()
        print("─" * 70)
        print()
        print("Hasil :", colored(hasil, "green"))
    except ValueError:
        print(colored("Error: Masukkan hanya angka, bukan huruf atau simbol!", "red"))
        time.sleep(2)
        helper()

helper()