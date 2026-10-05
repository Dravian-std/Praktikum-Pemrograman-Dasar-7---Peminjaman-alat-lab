# Praktikum-Pemrograman-Dasar-7---Peminjaman-alat-lab

## 👥 Pembagian Kontribusi Anggota

Proyek ini dikembangkan secara kolaboratif menggunakan pendekatan *Modular Programming* dan *Object-Oriented Programming* (OOP). Untuk mencegah terjadinya *merge conflict* pada repository, tugas dibagi secara spesifik per modul (file) sebagai berikut:

### 1. Aksya - *Student Data Manager* (`mahasiswa.py`)
Bertanggung jawab atas pengelolaan entitas dan struktur data mahasiswa pengguna laboratorium.
* **Implementasi Class:** Merancang Class `Mahasiswa` beserta enkapsulasi atributnya (NIM, Nama, No HP, Status Aktif Peminjaman).
* **Fitur CRUD Mahasiswa:** Mengembangkan fungsi untuk menambah, mengedit, mencari, dan menghapus data mahasiswa.
* **Implementasi Aturan Bisnis:** 
  * Menerapkan validasi **Aturan 2** (Batas Peminjaman): Memastikan satu mahasiswa tidak dapat memiliki lebih dari dua transaksi peminjaman aktif.
  * Menerapkan validasi **Aturan 6** (Penghapusan Data): Memblokir penghapusan data mahasiswa apabila masih terdapat transaksi yang belum diselesaikan (status aktif).

### 2. Keisha - *Equipment Data Manager* (`peralatan.py`)
Bertanggung jawab atas inventarisasi alat laboratorium dan pemantauan kondisi barang.
* **Implementasi Class:** Merancang Class `Peralatan` dengan atribut dinamis untuk mendukung penambahan kategori baru (kode, nama, kategori, kondisi, dan status ketersediaan).
* **Fitur CRUD Peralatan:** Mengembangkan fungsi untuk menambah, mengedit, mencari, dan menghapus data peralatan laboratorium.
* **Implementasi Aturan Bisnis:**
  * Menerapkan validasi **Aturan 1** (Ketersediaan Alat): Memastikan alat yang sedang dipinjam atau rusak tidak dapat dipinjam kembali.
  * Menerapkan logika **Aturan 5** (Kondisi Alat): Mengubah ketersediaan alat menjadi tidak tersedia (*unavailable*) secara otomatis apabila alat dikembalikan dalam kondisi "rusak ringan" atau "rusak berat".

### 3. Amel - *Transaction Controller* (`transaksi.py`)
Bertanggung jawab atas inti sistem operasional peminjaman dan pengembalian alat laboratorium.
* **Implementasi Class:** Merancang Class `TransaksiPeminjaman` dan `Pengembalian`.
* **Integrasi Entitas:** Menghubungkan objek dari Class `Mahasiswa` dengan objek dari Class `Peralatan` di dalam sebuah transaksi.
* **Implementasi Aturan Bisnis:**
  * Menerapkan **Aturan 3** (Isi Transaksi): Menggunakan struktur data *List* dinamis agar satu transaksi dapat menampung banyak alat sekaligus tanpa menggunakan variabel yang terpisah.
  * Menerapkan **Aturan 4** (Pengembalian Sebagian): Membuat algoritma pengecekan di mana status transaksi tetap "aktif" atau "sebagian dikembalikan" sampai semua alat dalam id transaksi tersebut lunas dikembalikan.

### 4. Danang - *System Integrator & UI Developer* (`main.py` & `SistemLaboratorium.py`)
Bertanggung jawab atas perakitan modul, struktur data utama, dan antarmuka pengguna di *command-line/terminal*[cite: 4].
* **Implementasi Class Utama:** Merancang Class Controller `SistemLaboratorium` yang mengelola *Dictionary* dan *List* utama sistem (menggantikan fungsi database).
* **Menu Interaktif:** Membangun antarmuka terminal (CLI) yang memuat minimal 11 menu utama proyek (Tampilkan alat tersedia, riwayat peminjaman, dll).
* **Integrasi Sistem:** Memanggil dan merakit fungsi-fungsi yang telah dibuat oleh Aksya, Keisha, dan Amel menjadi satu alur aplikasi yang utuh dan bebas *bug*.
* **DevOps & Dokumentasi:** Mengelola penyatuan (merge) *branch* GitHub dari seluruh anggota[cite: 6], serta menyusun struktur file dokumentasi teknis (`README.md`).

## 📂 Struktur Folder dan File Program

Proyek ini menggunakan struktur modular agar mempermudah pengembangan secara kolaboratif dan mencegah *merge conflict*.

```text
📦 sistem-peminjaman-lab
 ┣ 📂 modul/                  # Folder berisi class dan logika program utama
 ┃ ┣ 📜 __init__.py           # Penanda bahwa folder ini adalah package Python
 ┃ ┣ 📜 mahasiswa.py          # Modul Class Mahasiswa (Aksya)
 ┃ ┣ 📜 peralatan.py          # Modul Class Peralatan (Keisha)
 ┃ ┣ 📜 transaksi.py          # Modul Class TransaksiPeminjaman (Amel)
 ┃ ┗ 📜 sistem_lab.py         # Modul Class SistemLaboratorium/Controller (Danang)
 ┃
 ┣ 📂 dokumentasi/            # Folder berisi artefak dokumen sesuai ketentuan
 ┃ ┣ 📜 UML_Final_Kelompok.pdf
 ┃ ┣ 📜 Dokumen_Keputusan_Desain.pdf
 ┃ ┣ 📜 Hasil_Pengujian.pdf
 ┃ ┣ 📜 Hasil_Code_Review.pdf
 ┃ ┗ 📜 Refleksi_dan_Perbaikan.pdf
 ┃
 ┣ 📜 main.py                 # Entry point aplikasi (Menu interaktif CLI)
 ┗ 📜 README.md               # Dokumentasi utama repository
