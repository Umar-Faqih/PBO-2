# Nama    : Umar Faqih
# NIM     : 210511066
# Kelas   : R2(B)
 
#fahrenheit      
class Fahrenheit:
    def __init__(self, fahrenheit):
        self.fahrenheit = fahrenheit
    
    def to_celcius(self):
        return (self.fahrenheit - 32) * 5/9
    
    def to_reamur(self):
        return (self.fahrenheit - 32) * 4/9
    
    def to_kelvin(self):
        return (self.fahrenheit + 459.67) * 5/9
    
#reamur
class Reamur:
    def __init__(self, reamur):
        self.reamur = reamur
    
    def to_celcius(self):
        return self.reamur * 5/4
    
    def to_fahrenheit(self):
        return self.reamur * 9/4 + 32
    
    def to_kelvin(self):
        return self.reamur * 5/4 + 273.15

#kelvin
class Kelvin:
    def __init__(self, kelvin):
        self.kelvin = kelvin
    
    def to_celcius(self):
        return self.kelvin - 273.15
    
    def to_fahrenheit(self):
        return self.kelvin * 9/5 - 459.67
    
    def to_reamur(self):
        return (self.kelvin - 273.15) * 4/5

#===========================
#untuk konversikan fahrenheit
# suhu = Fahrenheit(60)
# celcius = suhu.to_celcius()
# reamur = suhu.to_reamur()
# kelvin = suhu.to_kelvin()

# print(f"{suhu.fahrenheit} derajat fahrenheit = {kelvin} derajat Kelvin")
# print(f"{suhu.fahrenheit} derajat fahrenheit = {reamur} derajat reamur")
# print(f"{suhu.fahrenheit} derajat fahrenheit = {celcius} derajat Celcius") 



#=============================
#untuk mengkonversikan reamur

# suhu = Reamur(60)
# celcius = suhu.to_celcius()
# fahrenheit = suhu.to_fahrenheit()
# kelvin = suhu.to_kelvin()

# print(f"{suhu.reamur} derajat reamur = {kelvin} derajat Kelvin")
# print(f"{suhu.reamur} derajat reamur = {fahrenheit} derajat fahrenheit")
# print(f"{suhu.reamur} derajat reamur = {celcius} derajat Celcius")   


#===========================
#untuk konversikan kelvin

# suhu = Kelvin(60)
# celcius = suhu.to_celcius()
# reamur = suhu.to_reamur()
# fahrenheit = suhu.to_fahrenheit()


# print(f"{suhu.kelvin} derajat kelvin = {reamur} derajat reamur")
# print(f"{suhu.kelvin} derajat kelvin = {celcius} derajat Celcius")
# print(f"{suhu.kelvin} derajat kelvin = {fahrenheit} derajat fahrenheit")
