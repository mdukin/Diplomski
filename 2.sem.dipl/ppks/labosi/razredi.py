from abc import ABC, abstractmethod

class Vozilo(ABC):
    def __init__(self, marka, model, godina) -> None:
        self.marka = marka
        self.model = model
        self.godina = godina
        self.spremnik = 0

    @abstractmethod
    def trubi(self):
        pass
    
    def vozi(self,n_km):
        potroseno_l = self.potrosnja * (n_km / 100)
        self.spremnik = 0 if self.spremnik <= potroseno_l else self.spremnik - potroseno_l   

    def natoci(self, l_goriva):
        self.spremnik += l_goriva

    def __str__(self) -> str:
        return self.marka + "," + self.model + ","+ str(self.godina)

    def srednja_vrijednost_godina(vozila):
        if not vozila:
            return 0  
        ukupno_godina = sum(vozilo.godina for vozilo in vozila)
        return ukupno_godina / len(vozila)
    
    def rangiraj_po_godinama(vozila):
        return sorted(vozila, key=lambda x: x.godina) 
    
class Auto(Vozilo): # nasljeđivanje

    def __init__(self, marka, model, godina,) -> None:
        super().__init__(marka, model, godina)
        self.potrosnja = 8 
    
    def trubi(self):
        print ("honk honk")


class Kamion(Vozilo): # nasljeđivanje
    def __init__(self, marka, model, godina,) -> None:
        super().__init__(marka, model, godina)
        self.potrosnja = 30
        self.teret = 0

    def trubi(self):
        print("Beeeep")

    def utovari_teret(self, kg):
        self.teret += kg
    def istovari_teret(self):
        self.teret = 0

class Motor(Vozilo): # nasljeđivanje
    def __init__(self, marka, model, godina, sjedalo_za_suvozaca) -> None:
        super().__init__(marka, model, godina)
        self.potrosnja = 5
        self.sjedalo_za_suvozaca = sjedalo_za_suvozaca
    
    def trubi(self):
        print("Vroooom")

    def pokupi_prijatelja(self):
        if not self.sjedalo_za_suvozaca :
            print("nemam mjesta")
        else: print("skoci gore")








    