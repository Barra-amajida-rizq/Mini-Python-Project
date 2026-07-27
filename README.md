# Mini Python Project

Kumpulan mini project sederhana yang dibuat menggunakan Python untuk belajar dan latihan konsep pemrograman dasar hingga menengah. Repository ini akan terus berkembang seiring bertambahnya project baru.

## 📌 Tentang Repository

Repository ini berisi berbagai mini project Python yang dikerjakan secara bertahap. Setiap project disimpan dalam folder terpisah agar mudah dikelola dan dipelajari satu per satu.

## 📂 Struktur Project

```
Mini-Python-Project/
├── games/
│   └── random.py          # Mini game menggunakan random
├── warung/
│   ├── services/
│   │   └── db.py          # Modul database/penyimpanan data warung
│   └── warung.py          # Logika utama aplikasi warung
├── libs.py                 # Fungsi bantuan umum (welcome_message, exit_message, keluar)
├── main.py                  # Entry point, menu utama untuk memilih mini project
├── requirements.txt
└── README.md
```

> Struktur di atas akan bertambah setiap kali ada mini project baru ditambahkan (misal: `kalkulator/`, `todo_list/`, `quiz/`, dsb).

## 🚀 Cara Menjalankan

1. Clone repository ini:
   ```bash
   git clone https://github.com/Barra-amajida-rizq/Mini-Python-Project.git
   cd Mini-Python-Project
   ```

2. (Opsional) Buat virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate      # Mac/Linux
   venv\Scripts\activate         # Windows
   ```

3. Install dependency (jika ada):
   ```bash
   pip install -r requirements.txt
   ```

4. Jalankan program:
   ```bash
   python main.py
   ```

## 🎮 Daftar Mini Project

| No | Nama Project | Deskripsi | Status |
|----|---------------|-----------|--------|
| 1  | Games (random) | Mini game sederhana berbasis random | ✅ Selesai |
| 2  | Warung | Simulasi aplikasi warung/toko sederhana | ✅ Selesai |
| 3  | *(project berikutnya)* | *(akan ditambahkan)* | 🔜 |

## 🛠️ Teknologi

- Python 3.x
- Modul standar Python (tanpa library eksternal, kecuali disebutkan di `requirements.txt`)

## 📖 Cara Menambahkan Mini Project Baru

1. Buat folder baru dengan nama project, misal `kalkulator/`
2. Tambahkan file Python di dalamnya
3. Import dan hubungkan ke `main.py` agar bisa diakses lewat menu utama
4. Update tabel **Daftar Mini Project** di README ini

## 🤝 Kontribusi

Project ini dibuat untuk pembelajaran pribadi, namun saran dan masukan sangat terbuka lewat Issues atau Pull Request.

## 📄 Lisensi

Bebas digunakan untuk belajar. Silakan fork dan kembangkan sesuai kebutuhanmu.

---
Dibuat dengan ❤️ menggunakan Python oleh [Barra Amajida Rizq](https://github.com/Barra-amajida-rizq)