class Peralatan:
    def __init__(self, kode_alat, nama_alat, kategori, kondisi="baik", status_tersedia=True):
        self.kode_alat = kode_alat
        self.nama_alat = nama_alat
        self.kategori = kategori
        self.kondisi = kondisi 

        # Konversi dari string CSV ("True"/"False") ke tipe boolean
        if isinstance(status_tersedia, bool):
            self.status_tersedia = status_tersedia
        else:
            self.status_tersedia = str(status_tersedia).strip().lower() == "true"


    def update_kondisi(self, kondisi_baru):
        self.kondisi = kondisi_baru.lower()
        # Aturan 5: Jika rusak, otomatis tidak tersedia
        if self.kondisi in ["rusak ringan", "rusak berat"]:
            self.status_tersedia = False
        else:
            self.status_tersedia = True

    def set_ketersediaan(self, status):
        if isinstance(status, bool):
            self.status_tersedia = status
        else:
            self.status_tersedia = str(status).strip().lower() == "true"

