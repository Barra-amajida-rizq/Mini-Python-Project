import main

def PenghitunganBiayaFotoCopy():
    print("=== Kalkulator Biaya FotoCopy ===")
    batas = int(input("Berapa banyak mata kuliah yang akan di print?: "))

    print("")
    total = 0
    for i in range(batas):
        matakuliah = input("Nama mata kuliah: ")
        halaman = int(input("Jumlah halaman: "))
        jenis = int(input("Jenis (1 = HitPut, 2 = Berwarna): "))

        if jenis == 1:
            harga = halaman * 200
        elif jenis == 2:
            harga = halaman * 500
        else:
            print("Pilihan hanya 1 untuk hitam dan putih, 2 untuk berwarna.")

        print("")
        print("Biaya", matakuliah,":", harga)
        print("")
        total = total + harga

    print("==================================")

    if total >= 50000:
        diskon = (total * 10) / 100
    else:
        diskon = 0

    bayar = total - diskon
    print("Total Biaya :", total)
    print("Diskon :", diskon)
    print("Total Pembayaran: ", bayar)

if __name__ == "__main__":
    PenghitunganBiayaFotoCopy()
    main()


