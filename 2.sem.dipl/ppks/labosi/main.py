
from razredi import Vozilo, Auto, Kamion, Motor

# Stvaranje pet objekata klase Auto
auti = [
    Auto("Volkswagen", "Golf", 2015),
    Auto("Toyota", "Corolla", 2018),
    Auto("Ford", "Focus", 2017),
    Auto("BMW", "3 Series", 2020),
    Auto("Audi", "A4", 2019)
]

# Testiranje funkcionalnosti klase Auto

srednja_vrijednost = Vozilo.srednja_vrijednost_godina(auti)
rangirani = Vozilo.rangiraj_po_godinama(auti)

print(srednja_vrijednost)
for v in rangirani:
    print(v)
print()

for auto in auti:
    auto.natoci(100)  # Natoci spremnik goriva
    auto.vozi(50)   # Vozi automobil 100 km
    auto.trubi()     # Svaki automobil trubi


print()
# Stvaranje pet objekata klase Kamion
kamioni = [
    Kamion("MAN", "TGX", 2016),
    Kamion("Scania", "R-Series", 2017),
    Kamion("Volvo", "FH", 2019),
    Kamion("Mercedes-Benz", "Actros", 2018),
    Kamion("Iveco", "Stralis", 2020)
]

srednja_vrijednost = Vozilo.srednja_vrijednost_godina(kamioni)
rangirani = Vozilo.rangiraj_po_godinama(kamioni)

print(srednja_vrijednost)
for v in rangirani:
    print(v)

print()

for kamion in kamioni:
    kamion.natoci(200)  # Natoci spremnik goriva
    kamion.utovari_teret(1000)
    kamion.vozi(100)    # Vozi kamion 200 km
    kamion.trubi()      # Svaki kamion trubi
    kamion.istovari_teret()

print()

# Stvaranje pet objekata klase Motor
motori = [
    Motor("Honda", "CBR600RR", 2015, True),
    Motor("Kawasaki", "Ninja ZX-10R", 2017, False),
    Motor("Yamaha", "YZF-R6", 2018, True),
    Motor("Suzuki", "GSX-R1000", 2019, False),
    Motor("Ducati", "Panigale V4", 2020, True)
]

srednja_vrijednost = Vozilo.srednja_vrijednost_godina(motori)
rangirani = Vozilo.rangiraj_po_godinama(motori)

print(srednja_vrijednost)
for v in rangirani:
    print(v)
print()

# Testiranje funkcionalnosti klase Motor
for motor in motori:
    motor.natoci(20)   # Natoci spremnik goriva
    motor.pokupi_prijatelja()
    motor.vozi(50)     # Vozi motor 50 km
    motor.trubi()      # Svaki motor trubi


v1:Vozilo = Auto("Volkswagen", "Golf", 2015)
v2:Vozilo =  Kamion("MAN", "TGX", 2016)
v3:Vozilo = Motor("Honda", "CBR600RR", 2015, True)

print()
#polimorfizam

v1.trubi() 
v2.trubi() 
v3.trubi() 





