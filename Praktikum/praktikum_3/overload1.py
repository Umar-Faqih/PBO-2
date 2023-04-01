class Hewan:
    def suara(self):
        pass

class Kucing(Hewan):
    def suara(self):
        return "Meong"

class Anjing(Hewan):
    def suara(self):
        return "Guk Guk"

class Sapi(Hewan):
    def suara(self):
        return "Moo"
    
class Domba(Hewan):
    def suara(self):
        return "Mbeee"



daftar_hewan = [Kucing(), Anjing(), Sapi(), Domba()]
for hewan in daftar_hewan:
    print(hewan.suara())
