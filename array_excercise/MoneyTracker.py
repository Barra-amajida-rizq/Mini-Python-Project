import main

def MoneyTracker():
    print("=== Pencatatan Pengeluaran Harian ===")

    daftar_pengeluaran = []
    semua_harga = []
    tambah = "ya"
    total = 0
    uang_saku = int(input("Masukkan uang saku anda: Rp"))

    while tambah == "ya" :
        keterangan = input("Keterangan: ")
        harga = int(input("Harga: "))

        daftar_pengeluaran.append([keterangan, harga])
        total = total + harga
        print("")
        tambah = input("Tambah pengeluaran?(ya/tidak): ")
        print("")

    print("=== Daftar Pengeluaran ===")
    for i in range(len(daftar_pengeluaran)):
        keterangan = daftar_pengeluaran[i][0]
        harga = daftar_pengeluaran[i][1]
        print(i+1, keterangan, harga)
        semua_harga.append(daftar_pengeluaran[i][1])

    harga_tertinggi = max(semua_harga)
    for i in range(len(daftar_pengeluaran)):
        if daftar_pengeluaran[i][1] == harga_tertinggi:
            barang_termahal = daftar_pengeluaran[i][0]

    sisa = uang_saku - total



    print("Total Pengeluaran hari ini: ", total)
    print("Sisa uang: ", sisa)
    print(f"Pengeluaran terbesar: {barang_termahal} - {harga_tertinggi:,}")
    if sisa >= 200000:
        print("AMAN")
    else:
        print("TIDAK AMAN")

if __name__ == "__main__":
    MoneyTracker()
    main()