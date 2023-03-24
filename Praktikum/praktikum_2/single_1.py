class Mobil:
    def __init__(self, merk, warna):
        self.merk = merk
        self.warna = warna
    def mobil(self):
        print(self.merk, "mobil")
class Kucing(Mobil):
    def __init__(self, merk, warna, jenis_mobil):
        super().__init__(merk, warna)
        self.jenis_mobil = jenis_mobil
    def torsi(self):
        print("1000cc!")
kucingA = Kucing("honda", "kuning", "sedan")
kucingA.mobil()
kucingA.torsi()