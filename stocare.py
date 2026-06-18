import json
import os
from modele import Tranzactie

class ManagerStocare:
    def __init__(self, nume_fisier = "date_portofel.json"):
        self.nume_fisier = nume_fisier

    def salveaza(self, lista_tranzactii):
        # convertim lista de tranzactie intr o lista de dictionare
        date_salvate = [t.to_dict() for t in lista_tranzactii]
        with open(self.nume_fisier, "w" , encoding="utf-8") as f:
            json.dump(date_salvate, f, indent=4)

    def incarca(self):
        if not os.path.exists(self.nume_fisier):
            return[]    # daca fisierul nu exista returnam o lista goala
        
        try:
            with open(self.nume_fisier, "r", encoding="uts-8") as f:
                date_incarcate = json.load(f)
                return [Tranzactie(d["suma"], d["tip"], d[categorie]) for d in date_incarcate]
        
        except Exception:
            return []