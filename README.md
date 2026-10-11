# Sistem Pengelolaan Peminjaman Peralatan Laboratorium

Aplikasi berbasis Python ini dikembangkan untuk mengelola proses pencatatan peminjaman peralatan oleh mahasiswa di lingkungan laboratorium universitas. Sistem ini dibangun murni menggunakan pendekatan *Object-Oriented Programming* (OOP) dan memanfaatkan struktur data dinamis bawaan Python (seperti *List* dan *Dictionary*) sebagai media penyimpanan data selama program berjalan.

## 👥 Anggota Kelompok

Proyek ini dikerjakan secara kolaboratif oleh 4 anggota dengan rincian peran sebagai berikut:

| No | Nama Lengkap | NIM | Peran / Kontribusi Utama | Profil GitHub |
|:---:|:---|:---:|:---|:---|
| 1 | Aksya Nayla Fitriana | K3525047 | Manajer Data Mahasiswa (Modul `Mahasiswa.py` & fungsi CRUD di `sistem_lab.py`) | [@aksyanayla-cpu](https://github.com/aksyanayla-cpu) |
| 2 | Sekar Hanny Keisha A | K3525041 | Manajer Data Peralatan (Modul `Peralatan.py` & fungsi inventaris di `sistem_lab.py`) | [@keskesiaw](https://github.com/keskesiaw) |
| 3 | Amelia Pinasti N | K3525049 | Manajer Transaksi (Modul `Transaksi.py` & fungsi operasional di `sistem_lab.py`) | [@ameliapinasti38-prog](https://github.com/ameliapinasti38-prog) |
| 4 | Danang Rafli Juvianto | K3525054 | Integrator Sistem (Menggabungkan `sistem_lab.py` & UI CLI di `main.py`) | [@dravian-std](https://github.com/dravian-std) |

---

## 🚀 Fitur Utama Program

Aplikasi ini menyediakan 10 menu interaktif pada antarmuka *command line* (CLI):

1. **Kelola data mahasiswa** (tambah, edit, hapus, cari).
2. **Kelola data alat** (tambah, edit, hapus, cari).
3. **Buat transaksi peminjaman** (mendukung peminjaman banyak alat sekaligus dalam satu transaksi).
4. **Tampilkan seluruh transaksi** yang tercatat di sistem.
5. **Proses pengembalian alat** (mendukung pembaruan kondisi alat dan pengembalian sebagian).
6. **Cari riwayat transaksi mahasiswa** berdasarkan NIM.
7. **Tampilkan alat yang tersedia** (stok dalam kondisi baik dan siap dipinjam).
8. **Tampilkan alat yang sedang dipinjam** (melacak posisi alat).
9. **Tampilkan alat yang rusak** (daftar alat yang rusak ringan maupun rusak berat).
10. **Keluar dari program**.

---

## ▶️ Cara Menjalankan

Pastikan Python 3 sudah terpasang, lalu jalankan dari folder utama repository:

```bash
python main.py
```

Program menyertakan data contoh awal (2 mahasiswa dan 3 alat) agar mudah dicoba. Data hanya disimpan selama program berjalan dan akan hilang saat program ditutup.

---

## 🛠️ Pembagian Kontribusi & Aturan Bisnis

Pengembangan dilakukan menggunakan paradigma *Modular Programming*. Setiap anggota memegang tanggung jawab spesifik untuk mencegah *merge conflict* pada repository:

### 1. Aksya - *Student Data Manager*
* **Modul:** Merancang Class `Mahasiswa` pada `Mahasiswa.py` dan fungsi pengelolaannya di `sistem_lab.py`.
* **Aturan Bisnis:**
  * Menerapkan validasi **Aturan 2** (Batas Peminjaman): Memastikan mahasiswa maksimal hanya memiliki 2 transaksi aktif.
  * Menerapkan validasi **Aturan 6** (Penghapusan Data): Memblokir penghapusan mahasiswa jika masih memiliki transaksi aktif.

### 2. Keisha - *Equipment Data Manager*
* **Modul:** Merancang Class `Peralatan` (mendukung kategori dinamis) pada `Peralatan.py` dan fungsinya di `sistem_lab.py`.
* **Aturan Bisnis:**
  * Menerapkan **Aturan 1** (Ketersediaan Alat): Menolak peminjaman jika alat tidak tersedia.
  * Menerapkan **Aturan 5** (Kondisi Alat): Mengubah status ketersediaan (*unavailable*) secara otomatis jika alat dikembalikan dalam kondisi rusak ringan/berat.

### 3. Amel - *Transaction Controller*
* **Modul:** Merancang Class `TransaksiPeminjaman` pada `Transaksi.py` dan fungsi proses operasional di `sistem_lab.py`.
* **Aturan Bisnis:**
  * Menerapkan **Aturan 3** (Isi Transaksi): Memanfaatkan *List* agar satu transaksi bisa berisi banyak jenis alat.
  * Menerapkan **Aturan 4** (Pengembalian Sebagian): Status transaksi menjadi `sebagian dikembalikan` selama masih ada alat yang belum kembali, dan menjadi `selesai` setelah seluruh alat dikembalikan.

### 4. Danang - *System Integrator & UI Developer*
* **Modul:** Merancang *Controller Utama* (`sistem_lab.py`) dan *Entry Point* antarmuka (`main.py`).
* **Tanggung Jawab:** Merakit fungsi bawaan Aksya, Keisha, dan Amel menjadi *loop* CLI interaktif, mengelola penggabungan (*merge branch*) GitHub anggota, serta menyusun dokumentasi proyek ini.

---

## 📂 Struktur Folder dan File Program

```text
📦 Praktikum-Pemrograman-Dasar-7---Peminjaman-alat-lab
 ┣ 📂 modul/                  # Folder berisi class dan logika program utama
 ┃ ┣ 📜 __init__.py
 ┃ ┣ 📜 Mahasiswa.py          # Modul entitas Mahasiswa (Aksya)
 ┃ ┣ 📜 Peralatan.py          # Modul entitas Peralatan (Keisha)
 ┃ ┣ 📜 Transaksi.py          # Modul entitas Transaksi (Amel)
 ┃ ┗ 📜 sistem_lab.py         # Modul Controller Utama (dikerjakan bersama, digabung Danang)
 ┃
 ┣ 📂 folder.dokumentasi/     # Folder artefak evaluasi
 ┃ ┣ 📜 uml final kelompok.pdf
 ┃ ┗ 📜 Dokumen Keputusan Desain Kelompok-7.pdf
 ┃
 ┣ 📜 main.py                 # File utama untuk menjalankan aplikasi
 ┗ 📜 README.md               # Dokumentasi repository
```
