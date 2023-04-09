class Peneliti:
    def __init__(self, nama, judul, tahun):
        self.nama = nama
        self.judul = judul
        self.tahun = tahun
    def penelitian(self):
        print(f"{self.nama} sedang melakukan penelitian {self.judul} di tahun {self.tahun}")

class Jurnalis:
    def __init__(self, nama, judul, tahun):
        self.nama = nama
        self.judul = judul
        self.tahun = tahun
    def liputan(self):
        print(f"{self.nama} sedang melakukan liputan {self.judul} di tahun {self.tahun}")

def compose(*functions):
    def composed():
        for f in functions:
            f()
    return composed

peneliti1 = Peneliti("Andi", "limbah", 2020)
jurnalis1 = Jurnalis("Budi", "sepak bola", 2023)
peneliti_jurnalis = compose(peneliti1.penelitian, jurnalis1.liputan)
peneliti_jurnalis()

