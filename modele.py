from typing import Type

class Tranzactie:
    def __init__(self, suma, tip, categorie):
        self.suma = float(suma) 
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

    def adauga_tranzactie(self, tranzactie):
    # --- LOGICA DE BLOCARE SOLD NEGATIV ---
        if tranzactie.tip.lower() == "cheltuiala":  
            balanta_curenta = self.calculeaza_balanta()
            if balanta_curenta - tranzactie.suma <= 0:
                print("TRANZACTIE RESPINSA!")
                print(f"Fonduri insuficiente. Balanța actuală este de {balanta_curenta} RON, iar cheltuiala este de {tranzactie.suma} RON.")
                print(f"Îți lipsesc {abs(balanta_curenta - tranzactie.suma)} RON pentru a efectua această tranzacție.")
                return False  # Returnăm False pentru că tranzacția a eșuat
            
        # Dacă este Venit sau dacă sunt destule fonduri, adăugăm tranzacția
        self.tranzactii.append(tranzactie)
        return True
  
    
    def calculeaza_balanta(self):
        balanta = 0.0
        for t in self.tranzactii:
            if t.tip == "Venit":
                balanta += t.suma
            else:
                balanta -= t.suma
        return balanta

# =====================================================================
# DEMONSTRAȚIE TYPE HINTING (Sursă: StackOverflow)
# =====================================================================
# 1. Când cerem o INSTANȚĂ a clasei (un obiect creat, cu date în el)
def exemplu_instanta(arg: Tranzactie):
    # ^ arg este un obiect de tip Tranzactie (ex: t = Tranzactie(100, "venit", "salariu"))
    pass

# 2. Când cerem CLASA ÎN SINE (obiectul clasă) folosind Type
def exemplu_clasa(arg: type[Tranzactie]):
    # ^ arg este clasa Tranzactie însăși, nu un obiect creat din ea
    pass

a = 3           # a are tipul 'int' (o instanță a clasei int)
b = int         # b are tipul 'Type[int]' (este chiar clasa int)
c = type(a)     # c are tot tipul 'Type[int]' (returnează clasa din care a fost creat 'a')
    