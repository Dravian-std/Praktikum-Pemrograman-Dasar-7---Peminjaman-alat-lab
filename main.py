from modul.sistem_lab import SistemLaboratorium

def main():
    sistem = SistemLaboratorium()
    
    # Data Dummy Awal agar mudah dites
    sistem.tambah_mahasiswa("M01", "Budi", "0811")
    sistem.tambah_mahasiswa("M02", "Siti", "0822")
    sistem.tambah_alat("A01", "Kamera DSLR", "Multimedia")
    sistem.tambah_alat("A02", "Tripod", "Multimedia")
    sistem.tambah_alat("A03", "Kabel LAN", "Jaringan")

    while True:
        print("\n=== SISTEM LABORATORIUM ===")
        print("1. Kelola Mahasiswa")
        print("2. Kelola Peralatan")
        print("3. Buat Transaksi Peminjaman")
        print("4. Tampilkan Semua Transaksi")
        print("5. Proses Pengembalian Alat")
        print("6. Cari Riwayat Transaksi Mahasiswa")
        print("7. Tampilkan Alat Tersedia")
        print("8. Tampilkan Alat Sedang Dipinjam")
        print("9. Tampilkan Alat Rusak")
        print("10. Keluar Program")
        
        pilihan = input("Pilih menu (1-10): ")

        if pilihan == "1":
            print("\n-- KELOLA MAHASISWA --")
            print("1. Tambah | 2. Edit | 3. Hapus | 4. Cari")
            sub = input("Pilih aksi: ")
            nim = input("Masukkan NIM: ")
            if sub == "1":
                sistem.tambah_mahasiswa(nim, input("Nama: "), input("No HP: "))
            elif sub == "2":
                sistem.edit_mahasiswa(nim, input("Nama Baru: "), input("No HP Baru: "))
            elif sub == "3":
                sistem.hapus_mahasiswa(nim)
            elif sub == "4":
                sistem.cari_mahasiswa(nim)

        elif pilihan == "2":
            print("\n-- KELOLA PERALATAN --")
            print("1. Tambah | 2. Edit | 3. Hapus | 4. Cari")
            sub = input("Pilih aksi: ")
            kode = input("Masukkan Kode Alat: ")
            if sub == "1":
                sistem.tambah_alat(kode, input("Nama Alat: "), input("Kategori: "))
            elif sub == "2":
                sistem.edit_alat(kode, input("Nama Baru: "), input("Kategori Baru: "))
            elif sub == "3":
                sistem.hapus_alat(kode)
            elif sub == "4":
                sistem.cari_alat(kode)

        elif pilihan == "3":
            nim = input("NIM Peminjam: ")
            # Input dipisah spasi (misal: A01 A02 A03)
            kodes = input("Masukkan Kode Alat (pisahkan dengan spasi): ").split()
            sistem.buat_transaksi(nim, kodes)

        elif pilihan == "4":
            sistem.tampilkan_transaksi()

        elif pilihan == "5":
            id_trx = input("Masukkan ID Transaksi (contoh: TRX001): ")
            kode_alat = input("Masukkan Kode Alat yang dikembalikan: ")
            print("Kondisi: 1. baik | 2. rusak ringan | 3. rusak berat")
            pilih_kondisi = input("Pilih kondisi (1/2/3): ")
            kondisi = "baik"
            if pilih_kondisi == "2": kondisi = "rusak ringan"
            elif pilih_kondisi == "3": kondisi = "rusak berat"
            
            sistem.proses_pengembalian(id_trx, kode_alat, kondisi)

        elif pilihan == "6":
            sistem.riwayat_peminjaman(input("Masukkan NIM Mahasiswa: "))

        elif pilihan == "7":
            sistem.tampilkan_alat_tersedia()

        elif pilihan == "8":
            sistem.tampilkan_alat_dipinjam()

        elif pilihan == "9":
            sistem.tampilkan_alat_rusak()

        elif pilihan == "10":
            print("Program dihentikan. Terima kasih!")
            break
        else:
            print("Pilihan tidak valid.")

if _name_ == "_main_":
    main()
