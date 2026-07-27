import main
from .services import db

def add():
    kode_barang = input("Masukkan kode barang: ")
    nama_barang = input("Masukkan nama barang: ")
    harga_barang = input("Masukkan harga barang: ")
    stock_barang = input("Masukkan stock barang: ")
    
    db.tambah_item(kode_barang, nama_barang, harga_barang, stock_barang)

def check():
    items = db.fetch_items()
    for item in items:
        kode_barang = item[1]
        nama_barang = item[2]
        harga_barang = item[3]
        stock_barang = item[4]
        print(f'''
Kode: {kode_barang}
Nama: {nama_barang} | {harga_barang}
Stock: {stock_barang}
''')
        
def edit():
    kode_barang = input("Masukkan kode barang yang ingin diubah harganya: ")
    harga_barang = input("Masukkan harga baru: ")
    
    db.edit_harga(harga_barang, kode_barang)

def start():
    while True:
        print()
        menu = int(input("Selamat datang di aplikasi kasir. \nSilahkan pilih menu: \n1. Tambah item \n2. Cek item \n3. Edit \n4. Kembali ke menu utama\n\nPilihan [1 / 2 / 3 / 4]: "))
        print()
        if menu == 1:
            add()
        elif menu == 2:
            check()
        elif menu == 3:
            edit()
        elif menu == 4:
            main.menu()
        else:
            break


if __name__ == '__main__':
    start()