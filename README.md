# Sistem Pengelolaan Peminjaman Peralatan Laboratorium

Aplikasi berbasis Python ini dikembangkan untuk mengelola proses pencatatan peminjaman peralatan oleh mahasiswa di lingkungan laboratorium universitas[cite: 1]. Sistem ini dibangun murni menggunakan pendekatan *Object-Oriented Programming* (OOP) dan memanfaatkan struktur data dinamis bawaan Python (seperti *List* dan *Dictionary*) sebagai media penyimpanan data selama program berjalan[cite: 1, 5].

## 👥 Anggota Kelompok

Proyek ini dikerjakan secara kolaboratif oleh 4 anggota dengan rincian peran sebagai berikut:

| No | Nama Lengkap | NIM | Peran / Kontribusi Utama | Profil GitHub |
|:---:|:---|:---:|:---|:---|
| 1 | Aksya Nayla Fitriana | K3525047 | Manajer Data Mahasiswa (Modul `mahasiswa.py` & fungsi CRUD di `sistem_lab.py`) | [@aksyanayla-cpu](https://github.com/aksyanayla-cpu) |
| 2 | Sekar Hanny Keisha A | K3525041 | Manajer Data Peralatan (Modul `peralatan.py` & fungsi inventaris di `sistem_lab.py`) | [@keskesiaw](https://github.com/keskesiaw) |
| 3 | Amelia Pinasti N | K3525049 | Manajer Transaksi (Modul `transaksi.py` & fungsi operasional di `sistem_lab.py`) | [@ameliapinasti38-prog](https://github.com/ameliapinasti38-prog) |
| 4 | Danang Rafli Juvianto | K3525054 | Integrator Sistem (Menggabungkan `sistem_lab.py` & UI CLI di `main.py`) | [@dravian-std](https://github.com/dravian-std) |

---

## 🚀 Fitur Utama Program

Aplikasi ini menyediakan 11 fitur menu interaktif utama sesuai dengan spesifikasi kebutuhan proyek[cite: 4]:

1. **Kelola data mahasiswa** (tambah, edit, hapus, cari)[cite: 4].
2. **Kelola data alat** (tambah, edit, hapus, cari)[cite: 4].
3. **Buat transaksi peminjaman** (mendukung peminjaman banyak alat sekaligus dalam satu transaksi)[cite: 3, 4].
4. **Tampilkan seluruh transaksi** yang tercatat di sistem[cite: 4].
5. **Proses pengembalian alat** (mendukung pembaruan kondisi alat dan pengembalian sebagian)[cite: 4].
6. **Cari transaksi** berdasarkan NIM mahasiswa[cite: 4].
7. **Tampilkan alat yang tersedia** (stok dalam kondisi baik dan siap dipinjam)[cite: 4].
8. **Tampilkan alat yang sedang dipinjam** (melacak posisi alat)[cite: 4].
9. **Tampilkan alat yang rusak** (daftar alat yang rusak ringan maupun rusak berat)[cite: 4].
10. **Tampilkan riwayat peminjaman mahasiswa**[cite: 4].
11. **Keluar dari program**[cite: 4].

---

## 🛠️ Pembagian Kontribusi & Aturan Bisnis

Pengembangan dilakukan menggunakan paradigma *Modular Programming*. Setiap anggota memegang tanggung jawab spesifik untuk mencegah *merge conflict* pada repository:

### 1. Aksya - *Student Data Manager*
* **Modul:** Merancang Class `Mahasiswa` pada `mahasiswa.py` dan fungsi pengelolaannya di `sistem_lab.py`[cite: 2, 5].
* **Aturan Bisnis:** 
  * Menerapkan validasi **Aturan 2** (Batas Peminjaman): Memastikan mahasiswa maksimal hanya memiliki 2 transaksi aktif[cite: 3].
  * Menerapkan validasi **Aturan 6** (Penghapusan Data): Memblokir penghapusan mahasiswa jika masih memiliki transaksi aktif[cite: 4].

### 2. Keisha - *Equipment Data Manager*
* **Modul:** Merancang Class `Peralatan` (mendukung kategori dinamis) pada `peralatan.py` dan fungsinya di `sistem_lab.py`[cite: 2, 5].
* **Aturan Bisnis:**
  * Menerapkan **Aturan 1** (Ketersediaan Alat): Menolak peminjaman jika alat tidak tersedia[cite: 3].
  * Menerapkan **Aturan 5** (Kondisi Alat): Mengubah status ketersediaan (*unavailable*) secara otomatis jika alat dikembalikan dalam kondisi rusak ringan/berat[cite: 4].

### 3. Amel - *Transaction Controller*
* **Modul:** Merancang Class `TransaksiPeminjaman` pada `transaksi.py` dan fungsi proses operasional di `sistem_lab.py`[cite: 2, 5].
* **Aturan Bisnis:**
  * Menerapkan **Aturan 3** (Isi Transaksi): Memanfaatkan *List* agar satu transaksi bisa berisi banyak jenis alat[cite: 3, 4].
  * Menerapkan **Aturan 4** (Pengembalian Sebagian): Membuat logika agar transaksi tetap berstatus "aktif" sampai seluruh alat dikembalikan[cite: 4].

### 4. Danang - *System Integrator & UI Developer*
* **Modul:** Merancang *Controller Utama* (`sistem_lab.py`) dan *Entry Point* antarmuka (`main.py`)[cite: 4, 5].
* **Tanggung Jawab:** Merakit fungsi bawaan Aksya, Keisha, dan Amel menjadi *loop* CLI interaktif, mengelola penggabungan (*merge branch*) GitHub anggota[cite: 6], serta menyusun dokumentasi proyek ini[cite: 7].

---

## 📂 Struktur Folder dan File Program

```text
📦 sistem-peminjaman-lab
 ┣ 📂 modul/                  # Folder berisi class dan logika program utama
 ┃ ┣ 📜 __init__.py           
 ┃ ┣ 📜 mahasiswa.py          # Modul entitas Mahasiswa (Aksya)
 ┃ ┣ 📜 peralatan.py          # Modul entitas Peralatan (Keisha)
 ┃ ┣ 📜 transaksi.py          # Modul entitas Transaksi (Amel)
 ┃ ┗ 📜 sistem_lab.py         # Modul Controller CRUD Utama (Dikerjakan bersama, digabung Danang)
 ┃
 ┣ 📂 dokumentasi/            # Folder artefak evaluasi
 ┃ ┣ 📜 UML_Final_Kelompok.pdf
 ┃ ┣ 📜 Dokumen_Keputusan_Desain.pdf
 ┃ ┣ 📜 Hasil_Pengujian.pdf
 ┃ ┣ 📜 Hasil_Code_Review.pdf
 ┃ ┗ 📜 Refleksi_dan_Perbaikan.pdf
 ┃
 ┣ 📜 main.py                 # File utama untuk menjalankan aplikasi
 ┗ 📜 README.md               # Dokumentasi repository
