from modele import Tranzactie, Portofel
from stocare import ManagerStocare

class MeniuInterfata:
    # Folosim type hinting pentru a specifica tipul claselor primite ca argument
    def __init__(self, portofel: Portofel, manager_stocare: ManagerStocare):
        self.portofel = portofel
        self.stocare = manager_stocare
    
    def afiseaza_meniu(self):
        print("\n" + "="*30)
        print("   MY POCKET MENIU.  ")
        print("="*30)
        print("1.Adauga Venit")
        print("2.Adauga Cheltuiala")
        print("3.Afiseaza Balanta Totala")
        print("4.Afiseaza Toate Tranzactiile")
        print("0.Iesire")
        print("="*30)

    # Specificăm că parametrul 'tip' trebuie să fie un string (str)
    def adauga_tranzactie(self, tip:str):
        print(f"\n----Adaugare{tip.capitalize()}----")
        try:
            suma = float(input("Introdu suma:"))
            if suma <= 0:
                print("Suma trebuie sa fie un nr pozitiv!")
                return
            
            # --- LOGICA DE BLOCARE SOLD NEGATIV ---

            if tip == "cheltuiala":
                balanta_curenta = self.portofel.calculeaza_balanta()
                if balanta_curenta - suma <= 0:
                    print(f"TRANZACTIE RESPINSA!")
                    print(f"Fonduri insuficiente. Balanța actuală este de {balanta_curenta} RON, iar cheltuiala este de {suma} RON.")
                    print(f"Îți lipsesc {abs(balanta_curenta - suma)} RON pentru a efectua această tranzacție.")
                    return
            
            # --------

            categorie = input("Introdu categoria ").strip()
            if not categorie:
                print("Categoria nu poate fi goala!")
                return
            
            noua_tranzactie = Tranzactie(suma, tip, categorie)
            self.portofel.adauga_tranzactie(noua_tranzactie)

            # Salvăm automat în JSON după fiecare adăugare
            self.stocare.salveaza(self.portofel.tranzactii) 
            print("----TRANZACTIE SALVATA CU SUCCES----")

        except ValueError:
            print("Eroare: Introdu un nr valid pt suma!")

    def afiseaza_tranzactii(self):
        print("\n ---- Istoric tranzactii ----")
        if not self.portofel.tranzactii:
            print("Nu exista tranzactii inregistrate!")
            return
        
        for idx, t in enumerate(self.portofel.tranzactii, 1):
            simbol = "+" if t.tip.lower() == "venit" else "-"
            print(f"{idx}. [{t.tip.upper()}] {t.categorie}:{simbol}{t.suma} RON")
    
    def porneste(self):
        while True:
            self.afiseaza_meniu()
            optiune = input("Alege o optiune:").strip()

            if optiune == "1":
                self.adauga_tranzactie("venit")
            elif optiune == "2":
                self.adauga_tranzactie("cheltuiala")
            elif optiune == "3":
                balanta = self.portofel.calculeaza_balanta()
                print(f"\n[BALANȚĂ] Disponibil: {balanta} RON")
            elif optiune == "4":
                self.afiseaza_tranzactii()
            elif optiune == "0":
                print("\nLa revedere!")
                break
            else:
                print("Optiune nevalida!")
                