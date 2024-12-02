a_45_bar = 5.3
a_45_bar = "ala ma kota"
a_45_bar = [
    34,23,"sdfg", 56
]

print(a_45_bar[3])
a_45_bar[3]="ala ma kota"

# Słownik/ Dictonaries
a_45_bar = {
    "a" : 45,
    "ala ma kota" : 567,
    34 : [
        34,45,67
    ]
}

def nazwa_funkcji(a,b,c,d):
    a_45_bar = 5.3
    a_45_bar = "ala ma kota"
    a_45_bar = [
        34,
        23,
        "sdfg", 
        56]
    return a+b+c+d

class ProstaKlasa():
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def sum(self):
        return self.a + self.b
    
sumator = ProstaKlasa(45,36)
print(sumator.sum())