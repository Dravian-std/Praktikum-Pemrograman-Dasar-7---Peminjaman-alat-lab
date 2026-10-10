from modul.Mahasiswa import Mahasiswa
from modul.Peralatan import Peralatan
from modul.Transaksi import TransaksiPeminjaman

class SistemLaboratorium:
    def __init__(self):
        self.daftar_mahasiswa = {}
        self.daftar_peralatan = {}
        self.daftar_transaksi = []
        self.counter_trx = 1

    # ==========================================
    # WILAYAH AKSYA (KELOLA MAHASISWA)
    # ==========================================
    def tambah_mahasiswa(self, nim, nama, no_hp):
        if nim not in self.daftar_mahasiswa:
            self.daftar_mahasiswa[nim] = Mahasiswa(nim, nama, no_hp)
            print("Mahasiswa berhasil ditambahkan.")
        else:
            print("Gagal! NIM sudah terdaftar.")

    def edit_mahasiswa(self, nim, nama_baru, no_hp_baru):
        if nim in self.daftar_mahasiswa:
            self.daftar_mahasiswa[nim].nama = nama_baru
            self.daftar_mahasiswa[nim].no_hp = no_hp_baru
            print("Data mahasiswa berhasil diperbarui.")
        else:
            print("Mahasiswa tidak ditemukan.")

    def hapus_mahasiswa(self, nim):
        if nim in self.daftar_mahasiswa:
            if self.daftar_mahasiswa[nim].jumlah_transaksi_aktif > 0:
                print("Gagal! Mahasiswa memiliki transaksi aktif.")
            else:
                del self.daftar_mahasiswa[nim]
                print("Mahasiswa berhasil dihapus.")
        else:
            print("Mahasiswa tidak ditemukan.")

    def cari_mahasiswa(self, nim):
        if nim in self.daftar_mahasiswa:
            mhs = self.daftar_mahasiswa[nim]
            print(f"NIM: {mhs.nim} | Nama: {mhs.nama} | No HP: {mhs.no_hp} | Transaksi Aktif: {mhs.jumlah_transaksi_aktif}")
        else:
            print("Mahasiswa tidak ditemukan.")

    # ==========================================
    # WILAYAH KEISHA (KELOLA PERALATAN)
    def tambah_alat(self, kode, nama, kategori):
        if kode not in self.daftar_peralatan:
            self.daftar_peralatan[kode] = Peralatan(kode, nama, kategori)
            print("Alat berhasil ditambahkan.")
        else:
            print("Gagal! Kode alat sudah terdaftar.")

    def edit_alat(self, kode, nama_baru, kategori_baru):
        if kode in self.daftar_peralatan:
            self.daftar_peralatan[kode].nama_alat = nama_baru
            self.daftar_peralatan[kode].kategori = kategori_baru
            print("Data alat berhasil diperbarui.")
        else:
            print("Alat tidak ditemukan.")

    def hapus_alat(self, kode):
        if kode in self.daftar_peralatan:
            alat = self.daftar_peralatan[kode]
            if not alat.status_tersedia and alat.kondisi == "baik":
                print("Gagal! Alat sedang dalam status dipinjam.")
            else:
                del self.daftar_peralatan[kode]
                print("Alat berhasil dihapus.")
        else:
            print("Alat tidak ditemukan.")

    def cari_alat(self, kode):
        if kode in self.daftar_peralatan:
            alat = self.daftar_peralatan[kode]
            print(f"Kode: {alat.kode_alat} | Nama: {alat.nama_alat} | Kat: {alat.kategori} | Kondisi: {alat.kondisi} | Tersedia: {alat.status_tersedia}")
        else:
            print("Alat tidak ditemukan.")

    def tampilkan_alat_tersedia(self):
        print("--- Alat Tersedia ---")
        for alat in self.daftar_peralatan.values():
            if alat.status_tersedia:
                print(f"{alat.kode_alat} | {alat.nama_alat} | {alat.kategori}")

    def tampilkan_alat_rusak(self):
        print("--- Daftar Alat Rusak ---")
        for alat in self.daftar_peralatan.values():
            if alat.kondisi in ["rusak ringan", "rusak berat"]:
                print(f"{alat.kode_alat} | {alat.nama_alat} | Kondisi: {alat.kondisi}")
    # ==========================================
    

    # ==========================================
    # WILAYAH AMEL (KELOLA TRANSAKSI)
    # ==========================================
