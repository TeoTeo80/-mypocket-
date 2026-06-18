class Tranzactie:
    def __init__(self, suama, tip, categorie):
        self.suma = float(self.suma)
        self.tip = tip # venit sau cheltuiala
        self.categorie = categorie
    
    def to_dict(self):
        return {
            "suma": self.suma,
            "tip": self.tip,
            "categorie": self.categorie

        }

class Portofel:
    def __init__(self):
        self.tranzactii = []

    def adauga_tranzactie(self, trenzactie):
        self.tranzactii.append(trenzactie)

    def calculeaza_balanta(self):
        balanta = 0.0
        for t in self.tranzactii:
            if t.tip == "Venit":
                balanta += t.suma
            else:
                balanta -= t.suma
        return balanta
    