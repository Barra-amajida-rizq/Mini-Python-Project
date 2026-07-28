import main

def kalk_absen():
    #variable
    print('=== Kalkulator Kehadiran Mahasiswa ===')
    nama = input("Nama Mahasiswa: ")
    total = int(input("Total Pertemun: "))
    hadir = int(input("Jumlah Kehadiran: "))

    #penghitungan
    jumlah_kehadiran = (hadir / total) * 100

    status = "Boleh mengikuti ujian" if (jumlah_kehadiran >= 75) else "Tidak boleh mengikuti ujian"

    #print
    print("Presentase kehadiran: ", jumlah_kehadiran)
    print("Status: ", status)

    if jumlah_kehadiran >= 75:
        print("Anda boleh mengikuti ujian")
    else:
        presentase = (total * 75) / 100
        selisih = presentase - hadir
        print("Tidak boleh mengikuti ujian, anda perlu mengikuti kelas tamabahan sebanyak: ", selisih)

if __name__ == "__main__":
    kalk_absen()
    main()