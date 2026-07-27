from libs import welcome_message, exit_message
from games import random
from warung import warung
from libs import keluar

def menu():
    welcome_message()
    print(f"Selamat datang Project aplikasi sederhana Python. \nSilahkan Pilih aplikasi apa yang ini dibuka\n1. Mini Games \n2. Warung \n3. Keluar")
    pilihan = input("Silahkan Pilih [1 / 2 / 3]: ")
    if pilihan == "1":
        random.game()
    elif pilihan == "2":
        warung.start()
    elif pilihan == "3":
        keluar()

def main():
    menu()
    exit_message()

if __name__ == '__main__':
    main()