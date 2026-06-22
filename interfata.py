from modele import Tranzactie

class MeniuInterfata:
    def __init__(self, portofel, manager_stocare):
        self.portofel = portofel
        self.manager_stocare = manager_stocare
    
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

    def adauga_tranzactie(self,tip):
        print(f"\n----Adaugare{tip.capitalize()}----")
        try:
            suma = float(input("Introdu suma:"))
            if suma <= 0:
                print("Suma trebuie sa fie un nr pozitiv!")
                return
            
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
        print("/n ---- Istoric tranzactii ----")
        if not self.portofel.tranzactii:
            print("Nu exista tranzactii inregistrate!")
            return
        
        for idx, t in enumerate(self.portofel.tranzactii, 1):
            simbol = "+" if t.tip.lower() == "Venit" else "-"
            print(f"{idx}. [{t.tip.upper()}] {t.categorie}:{simbol}{t.suma} RON")
    
    def porneste(self):
        while True:
            self.afiseaza_meniu()
            optiune = input("Alege o optiune:").strip()

            if optiune == "1":
                self.adauga_tranzactie_utilizator("Venit")
            elif optiune == "2":
                self.adauga_tranzactie_utilizator("cheltuiala")
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
                