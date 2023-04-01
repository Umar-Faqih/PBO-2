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

def panggil_suara(hewan):
    print(hewan.suara())

kucing = Kucing()
anjing = Anjing()
sapi = Sapi()
domba = Domba()

panggil_suara(kucing)
panggil_suara(anjing)
panggil_suara(sapi)
panggil_suara(domba)