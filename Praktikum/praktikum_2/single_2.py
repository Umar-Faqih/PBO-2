class Manusia:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur
    def operasi(self):
        print(f"{self.nama} sedang operasi.")
class Dokter(Manusia):
    def __init__(self, nama, umur, spesialis):
        super().__init__(nama, umur)
        self.spesialis = spesialis
    def mengajar(self):
        print(f"{self.nama} dengan Spesialis {self.spesialis} sedang Mengoperasi.")
dokterA = Dokter("harry", 39, "bedah")
dokterA.operasi()
dokterA.mengajar()
