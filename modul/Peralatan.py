class Peralatan:
    def __init__(self, kode_alat, nama_alat, kategori):
        self.kode_alat = kode_alat
        self.nama_alat = nama_alat
        self.kategori = kategori
        self.kondisi = "baik" 
        self.status_tersedia = True  # True jika bisa dipinjam[cite: 2, 3]

    def update_kondisi(self, kondisi_baru):
        self.kondisi = kondisi_baru.lower()
        # Aturan 5: Jika rusak, otomatis tidak tersedia
        if self.kondisi in ["rusak ringan", "rusak berat"]:
            self.status_tersedia = False
        else:
            self.status_tersedia = True

    def set_ketersediaan(self, status):
        self.status_tersedia = status
