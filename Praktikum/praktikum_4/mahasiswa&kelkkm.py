class Mahasiswa:
    def __init__(self, nama, nim):
        self.nama = nama
        self.nim = nim
    
    def info(self):
        print(f"Nama: {self.nama}")
        print(f"NIM: {self.nim}")
        

class Kelompok:
    def __init__(self, nomor, anggota=[]):
        self.nomor = nomor
        self.anggota = anggota
        
    def tambah_anggota(self, mhs):
        self.anggota.append(mhs)
        
    def info(self):
        print(f"Kelompok {self.nomor}")
        print("Daftar Anggota:")
        for mhs in self.anggota:
            mhs.info()
        print()


mhs1 = Mahasiswa("Desta", "20051100")
mhs2 = Mahasiswa("Faqih", "20051101")
mhs3 = Mahasiswa("Deni", "20051102")
mhs4 = Mahasiswa("Anwar", "19051103")



kel1 = Kelompok("KKM 1")
kel1.tambah_anggota(mhs1)
kel1.tambah_anggota(mhs2)

kel2 = Kelompok("KKM 2")
kel2.tambah_anggota(mhs3)
kel2.tambah_anggota(mhs4)


kel1.info()
kel2.info()