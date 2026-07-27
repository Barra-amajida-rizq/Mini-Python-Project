import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="db_warung"
)

def tambah_item(kode_barang, nama_barang, harga_barang, stock_barang):
    cursor = db.cursor()
    sql = "INSERT INTO barang (kode_barang, nama_barang, harga_barang, stock_barang) VALUES (%s, %s, %s, %s)"
    val = (kode_barang, nama_barang, harga_barang, stock_barang)
    cursor.execute(sql, val)
    db.commit()

    print("")

    if cursor.rowcount > 0:
        print(f"\nItem {nama_barang} berhasil ditambahkan.\n")
    else: 
        print(f"\nGagal menambahkan item {nama_barang}\n")

def edit_harga(harga_barang, kode_barang):
    cursor = db.cursor()
    #validasi data
    cursor.execute("SELECT * FROM barang WHERE kode_barang = %s", (kode_barang,))
    data = cursor.fetchone()
    if data is None:
        print(f"Item tidak ditemukan, Silahkan periksa kembali kode barang yang ingin di update.")
        return
    
    #update harga
    sql = "UPDATE barang SET harga_barang = %s WHERE kode_barang = %s"
    val = (harga_barang, kode_barang)
    cursor.execute(sql, val)
    db.commit()

    if cursor.rowcount > 0:
        print(f"\nHarga item dengan kode {kode_barang} berhasil diubah menjadi {harga_barang}.\n")
    else:
        print(f"\nGagal mengubah harga item dengan kode {kode_barang}.\n")


def fetch_items():
    cursor = db.cursor()
    cursor.execute("SELECT * FROM barang")
    return cursor.fetchall()