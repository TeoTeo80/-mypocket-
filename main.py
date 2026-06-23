from modele import Portofel
from stocare import ManagerStocare
from interfata import MeniuInterfata

def main():
    #1 Initializam manaerul de fisiere
    manager_stocare = ManagerStocare()

    # 2. Creăm portofelul și încărcăm datele vechi (dacă există)
    portofel = Portofel()
    portofel.tranzactii = manager_stocare.incarca()
    print(f"[Sistem] S-au încărcat {len(portofel.tranzactii)} tranzacții din baza de date.")

    # 3. Pornim meniul interactiv
    interfata = MeniuInterfata(portofel, manager_stocare)
    interfata.porneste()

if __name__ == "__main__":
    main()