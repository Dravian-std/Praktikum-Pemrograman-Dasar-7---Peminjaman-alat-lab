# Praktikum-Pemrograman-Dasar-7---Peminjaman-alat-lab
## 👥 Pembagian Kontribusi Anggota

Proyek ini dikembangkan secara kolaboratif menggunakan pendekatan *Modular Programming* dan *Object-Oriented Programming* (OOP)[cite: 5]. Untuk mencegah terjadinya *merge conflict* pada repository, tugas dibagi secara spesifik per modul (file) sebagai berikut:

### 1. Aksya - *Student Data Manager* (`mahasiswa.py`)
Bertanggung jawab atas pengelolaan entitas dan struktur data mahasiswa pengguna laboratorium[cite: 2].
* **Implementasi Class:** Merancang Class `Mahasiswa` beserta enkapsulasi atributnya (NIM, Nama, No HP, Status Aktif Peminjaman)[cite: 2].
* **Fitur CRUD Mahasiswa:** Mengembangkan fungsi untuk menambah, mengedit, mencari, dan menghapus data mahasiswa[cite: 4].
* **Implementasi Aturan Bisnis:** 
  * Menerapkan validasi **Aturan 2** (Batas Peminjaman): Memastikan satu mahasiswa tidak dapat memiliki lebih dari dua transaksi peminjaman aktif[cite: 3].
  * Menerapkan validasi **Aturan 6** (Penghapusan Data): Memblokir penghapusan data mahasiswa apabila masih terdapat transaksi yang belum diselesaikan (status aktif)[cite: 4].

### 2. Keisha - *Equipment Data Manager* (`peralatan.py`)
Bertanggung jawab atas inventarisasi alat laboratorium dan pemantauan kondisi barang[cite: 2].
* **Implementasi Class:** Merancang Class `Peralatan` dengan atribut dinamis untuk mendukung penambahan kategori baru (kode, nama, kategori, kondisi, dan status ketersediaan)[cite: 2].
* **Fitur CRUD Peralatan:** Mengembangkan fungsi untuk menambah, mengedit, mencari, dan menghapus data peralatan laboratorium[cite: 4].
* **Implementasi Aturan Bisnis:**
  * Menerapkan validasi **Aturan 1** (Ketersediaan Alat): Memastikan alat yang sedang dipinjam atau rusak tidak dapat dipinjam kembali[cite: 3].
  * Menerapkan logika **Aturan 5** (Kondisi Alat): Mengubah ketersediaan alat menjadi tidak tersedia (*unavailable*) secara otomatis apabila alat dikembalikan dalam kondisi "rusak ringan" atau "rusak berat"[cite: 4].

### 3. Amel - *Transaction Controller* (`transaksi.py`)
Bertanggung jawab atas inti sistem operasional peminjaman dan pengembalian alat laboratorium[cite: 2].
* **Implementasi Class:** Merancang Class `TransaksiPeminjaman` dan `Pengembalian`[cite: 2].
* **Integrasi Entitas:** Menghubungkan objek dari Class `Mahasiswa` dengan objek dari Class `Peralatan` di dalam sebuah transaksi[cite: 2].
* **Implementasi Aturan Bisnis:**
  * Menerapkan **Aturan 3** (Isi Transaksi): Menggunakan struktur data *List* dinamis agar satu transaksi dapat menampung banyak alat sekaligus tanpa menggunakan variabel yang terpisah[cite: 3, 4].
  * Menerapkan **Aturan 4** (Pengembalian Sebagian): Membuat algoritma pengecekan di mana status transaksi tetap "aktif" atau "sebagian dikembalikan" sampai semua alat dalam id transaksi tersebut lunas dikembalikan[cite: 4].

### 4. Danang - *System Integrator & UI Developer* (`main.py` & `SistemLaboratorium.py`)
Bertanggung jawab atas perakitan modul, struktur data utama, dan antarmuka pengguna di *command-line/terminal*[cite: 4].
* **Implementasi Class Utama:** Merancang Class Controller `SistemLaboratorium` yang mengelola *Dictionary* dan *List* utama sistem (menggantikan fungsi database)[cite: 1, 5].
* **Menu Interaktif:** Membangun antarmuka terminal (CLI) yang memuat minimal 11 menu utama proyek (Tampilkan alat tersedia, riwayat peminjaman, dll)[cite: 4].
* **Integrasi Sistem:** Memanggil dan merakit fungsi-fungsi yang telah dibuat oleh Aksya, Keisha, dan Amel menjadi satu alur aplikasi yang utuh dan bebas *bug*[cite: 4].
* **DevOps & Dokumentasi:** Mengelola penyatuan (merge) *branch* GitHub dari seluruh anggota[cite: 6], serta menyusun struktur file dokumentasi teknis (`README.md`).
