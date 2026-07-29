import main
from .services.db import cari_barang, kurangi_stock


def input_kode(): 
    kode = input("Kode Barang yang ingin dibeli: ")
    while kode == "":
        print("Kode Barang tidak boleh kosong.")
        kode = input("Kode Barang: ")
    data = cari_barang(kode)

    if data is None:
        print(f"Kode Barang tidak ditemukan, Silahkan periksa kembali kode barang anda.")

    return data

def input_jumlah():
    jumlah = int(input("Jumlah Barang yang ingin dibeli: "))
    while jumlah <= 0:
        print("Jumlah barang harus lebih dari 0.")
        jumlah = int(input("Jumlah Barang yang ingin dibeli: "))
    
    while jumlah >= 100:
        print(f"Jumlah Pembelian tidak boleh lebih dari 100.")
        jumlah = int(input("Jumlah Barang yang ingin dibeli: "))

    return jumlah

def info(nama_barang, harga_barang, stock_barang):
    print(f"Nama Barang: {nama_barang}")
    print(f"Harga Barang: {harga_barang}")
    print(f"Stock Barang: {stock_barang}")

def proses():
    daftar_belanja = []
    tambah = "ya"

    while tambah == "ya":
        data = input_kode()
        if data is None:
            continue

        kode_barang, nama_barang, harga_barang, stock_barang = data
        if stock_barang <= 0:
            print(f"Stock Barang {nama_barang} habis.")
            continue

        info(nama_barang, harga_barang, stock_barang)

        jumlah = input_jumlah(stock_barang)
        if jumlah is None:
            continue

        total = harga_barang * jumlah
        daftar_belanja.append((kode_barang, nama_barang, harga_barang, jumlah, total))

        kurangi_stock(kode_barang, jumlah)

        print(f"{nama_barang} sebanyak {jumlah} berhasil ditambahkan ke daftar belanja.")
        tambah = input("Tambah barang lagi? (ya/tidak): ")
        print("")

        return daftar_belanja
    
def total_belanja(daftar_belanja):
    return sum(item[3] for item in daftar_belanja)

def nota(daftar_belanja):
    print("=== Nota Belanja ===")

    if not daftar_belanja:
        print("Tidak ada barang yang dibeli.")
        return
    
    for i, item in enumerate(daftar_belanja, start = 1):
        nama, harga, jumlah, subtotal = item
        print(f"{i}. {nama} - Harga: {harga} - Jumlah: {jumlah} - Total: Rp{subtotal}")
    
    total = total_belanja(daftar_belanja)

    print("")
    print(f"Total belanja: Rp{total}, ")

def kasir():
    print("=== Kasir Warung ===\n")
    daftar_belanja = proses()
    nota(daftar_belanja)

if __name__ == "__main__":
    main()