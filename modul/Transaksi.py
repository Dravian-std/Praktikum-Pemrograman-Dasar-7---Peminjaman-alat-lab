from datetime import date, timedelta

class TransaksiPeminjaman:
    def __init__(self, id_transaksi, mahasiswa, daftar_alat):
        self.id_transaksi = id_transaksi
        self.mahasiswa = mahasiswa
        self.daftar_alat_dipinjam = daftar_alat  # List dinamis (Aturan 3)[cite: 2, 3, 4]
        self.daftar_alat_dikembalikan = []
        self.tgl_peminjaman = date.today()
        self.batas_waktu = self.tgl_peminjaman + timedelta(days=7)  # Maks 7 hari[cite: 2]
        self.status_transaksi = "dipinjam"  # dipinjam / sebagian dikembalikan / selesai[cite: 3]

    def proses_pengembalian_alat(self, kode_alat, kondisi_baru):
        alat_ditemukan = None
        for alat in self.daftar_alat_dipinjam:
            if alat.kode_alat == kode_alat and alat not in self.daftar_alat_dikembalikan:
                alat_ditemukan = alat
                break
        
        if alat_ditemukan:
            alat_ditemukan.update_kondisi(kondisi_baru)
            if alat_ditemukan.kondisi == "baik":
                alat_ditemukan.set_ketersediaan(True)
            
            self.daftar_alat_dikembalikan.append(alat_ditemukan)
            self.update_status()
            return True
        return False

    def update_status(self):
        # Aturan 4: Pengembalian sebagian
        if len(self.daftar_alat_dikembalikan) == len(self.daftar_alat_dipinjam):
            self.status_transaksi = "selesai"
            self.mahasiswa.kurangi_transaksi()
        elif len(self.daftar_alat_dikembalikan) > 0:
            self.status_transaksi = "sebagian dikembalikan"