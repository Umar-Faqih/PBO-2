class Penulis:
    def __init__(self, nama, alamat):
        self.nama = nama
        self.alamat = alamat
        self.buku = []
    
    def tambah_buku(self, judul):
        self.buku.append(Buku(judul))
        
    def info(self):
        print(f"Nama Penulis: {self.nama}")
        print(f"Alamat: {self.alamat}")
        print("Buku yang ditulis:")
        for buku in self.buku:
            print("- " + buku.judul)
        print()
        

class Buku:
    def __init__(self, judul):
        self.judul = judul
    
    def info(self):
        print(f"Judul Buku: {self.judul}")



penulis1 = Penulis("Chairil", "Indonesia")
penulis2 = Penulis("Anwar", "Indonesia")
penulis3 = Penulis("Raditya Dika", "Indonesia")


penulis1.tambah_buku("Tiga Menguak Takdir")
penulis1.tambah_buku("Hukum Adat Indonesia")
penulis1.tambah_buku("Aku")
penulis2.tambah_buku("Derul Campur Debu")
penulis3.tambah_buku("Ubur Ubur Lembur")


penulis1.info()
penulis2.info()
penulis3.info()