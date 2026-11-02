# Sistem Pengelolaan Peminjaman Peralatan Laboratorium (Proyek 2 - File Persistence)

Aplikasi berbasis Python ini dikembangkan untuk mengelola proses pencatatan peminjaman peralatan oleh mahasiswa di lingkungan laboratorium universitas. Pada Proyek 2 ini, sistem telah ditingkatkan menggunakan pendekatan **Object-Oriented Programming (OOP)** yang terintegrasi dengan **File Handling / File Persistence (`.csv` dan `.txt`)**, sehingga seluruh data tersimpan secara permanen dan tidak hilang saat program ditutup.

## 🌟 Fitur Utama & Pembaharuan Proyek 2

1. **File Persistence (Penyimpanan Permanen)**:

  * Data otomatis dimuat (*read*) saat program dibuka dan disimpan (*write*) secara otomatis setiap ada manipulasi data serta saat keluar dari program.
  * **`mahasiswa.csv`**: Menyimpan data identitas mahasiswa dan jumlah transaksi aktif.
  * **`peralatan.csv`**: Menyimpan data ketersediaan, kategori, dan kondisi peralatan lab.
  * **`transaksi.csv`**: Menyimpan riwayat peminjaman dan status pengembalian barang.
  * **`log_aktivitas.txt`**: Menyimpan riwayat aktivitas sistem beserta *timestamp*.
2. **Tantangan A (Pencarian Fleksibel)**:

  * Fitur pencarian alat serbaguna yang dapat mencocokkan kata kunci berdasarkan kode alat, sebagian nama alat, maupun kategori secara *case-insensitive*.
3. **Tantangan D (Log Activities)**:

  * Seluruh transaksi, penambahan/perubahan data, dan pengembalian dicatat secara *real-time* lengkap dengan jam dan tanggal, lalu tersimpan ke dalam file `log_aktivitas.txt`.

## 👥 Anggota Kelompok

Proyek ini dikerjakan secara kolaboratif oleh 4 anggota dengan rincian peran sebagai berikut:

| No | Nama Lengkap | NIM | Peran / Kontribusi Utama | Profil GitHub |
|:---:|:---|:---:|:---|:---|
| 1 | Aksya Nayla Fitriana | K3525047 | Manajer Data Mahasiswa (Modul `Mahasiswa.py` & fungsi CRUD/Persistence Mahasiswa di `sistem_lab.py`) | [@aksyanayla-cpu](https://github.com/aksyanayla-cpu) |
| 2 | Sekar Hanny Keisha A | K3525041 | Manajer Data Peralatan & Pengembang Tantangan A (Modul `Peralatan.py` & CRUD/Persistence pencarian fleksibel di `sistem_lab.py`) | [@keskesiaw](https://github.com/keskesiaw) |
| 3 | Amelia Pinasti N | K3525049 | Manajer Transaksi (Modul `Transaksi.py` & fungsi operasional/Persistence Transaksi di `sistem_lab.py`) | [@ameliapinasti38-prog](https://github.com/ameliapinasti38-prog) |
| 4 | Danang Rafli Juvianto | K3525054 | Integrator Sistem, File Handing & Pengembang Tantangan D (`main.py`, `modul/__init__.py`, `simpan_data`/`muat_data` &amp; Log Aktivitas di `sistem_lab.py`) | [@dravian-std](https://github.com/dravian-std) |

---

## 🚀 Menu Program (CLI Interface)

Aplikasi menyediakan 11 pilihan menu pada antarmuka *Command Line Interface*:

1. **Kelola Mahasiswa**: Tambah, Edit, Hapus, dan Cari data mahasiswa.
2. **Kelola Peralatan**: Tambah, Edit, Hapus, dan Cari alat (Pencarian Fleksibel).
3. **Buat Transaksi Peminjaman**: Peminjaman banyak alat sekaligus per transaksi.
4. **Tampilkan Semua Transaksi**: Menampilkan seluruh status transaksi yang tercatat.
5. **Proses Pengembalian Alat**: Mengembalikan alat per item beserta pembaruan kondisi alat.
6. **Cari Riwayat Transaksi Mahasiswa**: Menampilkan riwayat peminjaman berdasarkan NIM.
7. **Tampilkan Alat Tersedia**: Menampilkan stok alat yang siap dipinjam.
8. **Tampilkan Alat Sedang Dipinjam**: Melacak peralatan yang masih di tangan peminjam.
9. **Tampilkan Alat Rusak**: Menampilkan daftar alat kondisi rusak ringan/berat.
10. **Tampilkan Log Aktivitas**: Melihat riwayat aktivitas sistem secara *real-time*.
11. **Keluar Program**: Menyimpan seluruh data ke file fisik dan menghentikan aplikasi.

---

## ▶️ Cara Menjalankan Aplikasi

1. Pastikan Python 3 sudah terpasang di komputer Anda.
2. Buka terminal / command prompt pada direktori utama proyek.
3. Jalankan perintah berikut:

```
python main.py

```

&gt; **Catatan Pembacaan Data**: Pada saat pertama kali dijalankan (jika berkas `.csv` belum ada), sistem akan membuatkan data contoh awal (*dummy data*) secara otomatis dan membentuk berkas `mahasiswa.csv`, `peralatan.csv`, `transaksi.csv`, serta `log_aktivitas.txt`. Pada penggunaan selanjutnya, sistem akan membaca data lama secara otomatis dari berkas-berkas tersebut.
---

## 🛠️ Aturan Bisnis Sistem

* **Aturan 1 (Ketersediaan Alat)**: Peminjaman dibatalkan jika ada alat yang tidak ditemukan atau sedang tidak tersedia.
* **Aturan 2 (Batas Transaksi)**: Setiap mahasiswa maksimal hanya boleh memiliki 2 transaksi peminjaman aktif.
* **Aturan 3 (Kapasitas Transaksi)**: Satu transaksi peminjaman dapat memuat lebih dari satu jenis alat.
* **Aturan 4 (Pengembalian Sebagian)**: Status transaksi otomatis berubah menjadi `sebagian dikembalikan` hingga seluruh alat dalam transaksi tersebut dikembalikan secara lengkap (`selesai`).
* **Aturan 5 (Kondisi Alat Rusak)**: Jika alat dikembalikan dalam kondisi `rusak ringan` atau `rusak berat`, status ketersediaan alat otomatis diubah menjadi tidak tersedia (`False`).
* **Aturan 6 (Validasi Hapus Data)**: Mahasiswa atau alat yang sedang terikat transaksi aktif tidak dapat dihapus dari sistem.

---

## 📂 Struktur Folder dan File Program

```text
📦 Praktikum-Pemrograman-Dasar-7---Peminjaman-alat-lab
 ┣ 📂 modul/                  # Folder berisi class dan logika program utama
 ┃ ┣ 📜 __init__.py
 ┃ ┣ 📜 Mahasiswa.py          # Modul entitas Mahasiswa (Aksya)
 ┃ ┣ 📜 Peralatan.py          # Modul entitas Peralatan (Keisha)
 ┃ ┣ 📜 Transaksi.py          # Modul entitas Transaksi (Amel)
 ┃ ┗ 📜 sistem_lab.py         # Controller Utama, Logic & File Handling (dikerjakan bersama, digabung Danang)
 ┃
 ┣ 📜 mahasiswa.csv           # File data permanen Mahasiswa
 ┣ 📜 peralatan.csv           # File data permanen Peralatan
 ┣ 📜 transaksi.csv           # File data permanen Transaksi Peminjaman
 ┣ 📜 log\_aktivitas.txt      # File log riwayat aktivitas sistem
 ┃
 ┣ 📂 folder.dokumentasi/     # Folder artefak evaluasi
 ┃ ┣ 📜 uml final kelompok.pdf
 ┃ ┗ 📜 Dokumen Keputusan Desain Kelompok-7.pdf
 ┃
 ┣ 📜 main.py                 # File utama untuk menjalankan aplikasi
 ┗ 📜 README.md               # Dokumentasi repository
```
