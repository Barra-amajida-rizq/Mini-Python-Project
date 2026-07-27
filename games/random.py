import random
from main import main

#main program
def game():
    while True :
        position = random.randint(1, 4)

        print(" ")
        bentuk_goa = "|_|"
        goa_kosong = [bentuk_goa] * 4
        goa = goa_kosong.copy()

        goa[position -1] = "|0_0|"

        goa_kosong = " ".join(goa_kosong)
        goa = " " .join(goa)

        print(f" Perhatikan goa di bawah ini{goa_kosong}")

        pilihan_user = (input(f"Coba tebak mata nya ada di goa mana? [1 / 2 / 3 / 4]: "))
        while pilihan_user == "":
            print(f"Pilihan anda kosong, silahkan isi sesuai dengan ketentuan.")
            pilihan_user = (input(f"Coba tebak mata nya ada di goa mana? [1 / 2 / 3 / 4]: "))

        pilihan_user = int(pilihan_user)

        if pilihan_user == position :
            print(f"Selamat pilihan anda yaitu {position} benar!!")
            print (f"Terimakasih sudah bermain")
        else :
                print(f"{goa} \n Jawaban {pilihan_user} salah!!, Terimakasih sudah bermain")

        play_again = input("Mau main lagi? [Y/n]: ")
        if play_again == "n":
            print(f"Terima kasih telah bermain!")
            back_menu = input("kembali ke menu utama? [y/n]: ")
            if back_menu == "y":
                main()

if __name__ == '__main__':
     game()