import socket

PC = socket.gethostname()

def welcome_message():
    style = "=" * (len(PC))
    print(style)
    print(f"{PC}")
    print(style)

def exit_message():
    print("Terima kasih, Sampai jumpa lagi")
    print("Program di hentikan")
    exit()

def keluar():
    print(f"Terima kasih, Sampai jumpa lagi")
    exit()

if __name__ == '__main__':
    welcome_message()
    exit_message()