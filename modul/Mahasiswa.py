class Mahasiswa:
    def __init__(self, nim, nama, no_hp):
        self.nim = nim
        self.nama = nama
        self.no_hp = no_hp
        self.jumlah_transaksi_aktif = 0  # Aturan 2: Melacak batas transaksi[cite: 2, 3]

    def tambah_transaksi(self):
        self.jumlah_transaksi_aktif += 1

    def kurangi_transaksi(self):
        if self.jumlah_transaksi_aktif > 0:
            self.jumlah_transaksi_aktif -= 1

    def bisa_meminjam(self):
        # Aturan 2: Maksimal 2 transaksi aktif[cite: 3]
        return self.jumlah_transaksi_aktif < 2
