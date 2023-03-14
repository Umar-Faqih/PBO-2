# Nama : Umar Faqih
# Kelas : R2(B)
# Nim : 210511066


class Suhu:
    @staticmethod
    def celcius_to_fahrenheit(c):
        f = (9/5) * c + 32
        return f

    @staticmethod
    def celcius_to_reamur(c):
        r = (4/5) * c
        return r

    @staticmethod
    def celcius_to_kelvin(c):
        k = c + 273.15
        return k

# Contoh penggunaan
C = 75
F = Suhu.celcius_to_fahrenheit(C)
R = Suhu.celcius_to_reamur(C)
K = Suhu.celcius_to_kelvin(C)

print("Konversi", C, "celcius")
print(F,"frenheit")
print(R,"reamur")
print(K,"kelvin")