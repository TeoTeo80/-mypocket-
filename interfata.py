from modele import Tranzactie, Portofel, FonduriInsuficienteError
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
            

            categorie = input("Introdu categoria ").strip()
            if not categorie:
                print("Categoria nu poate fi goala!")
                return
            
            noua_tranzactie = Tranzactie(suma, tip, categorie)
            
            # Încercăm să adăugăm tranzacția. Dacă portofelul dă raise, codul sare direct la block-ul except de jos
            self.portofel.adauga_tranzactie(noua_tranzactie)

            # Salvăm doar dacă nu s-a aruncat nicio excepție
            self.stocare.salveaza(self.portofel.tranzactii) 
            print("---- TRANZACTIE SALVATA CU SUCCES ----")

        except FonduriInsuficienteError as e:
            # Aici prindem eroarea generată de Portofel și afișăm mesajul ei
            print(f"\n TRANZACTIE RESPINSA!")
            print(e)
            
        except ValueError:
            # Aici prindem doar dacă utilizatorul scrie litere în loc de cifre la sumă
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
                