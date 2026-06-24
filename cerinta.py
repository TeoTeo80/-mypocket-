# FIȘA PROIECTULUI
# 1. Numele Proiectului:
# mypocket

# 2. Descrierea ideii și Obiective:
# Aplicația este un utilitar în linie de comandă (CLI) care ajută utilizatorul să își gestioneze veniturile și cheltuielile zilnice. 
# Scopul ei este să ofere o imagine clară asupra bugetului disponibil și să salveze datele pentru a nu fi pierdute la închiderea programului.
# Funcționalități principale:
# Adăugarea de tranzacții (Venituri și Cheltuieli) cu sumă, categorie și dată.
# Calcularea automată a balanței totale (Venituri - Cheltuieli).
# Setarea unui buget lunar pe categorii (de ex. "Mâncare", "Transport") și alertarea utilizatorului când depășește limita.
# Salvarea și încărcarea datelor dintr-un fișier text JSON

# 3. Arhitectura OOP (Clase estimate):
# Pentru a organiza codul curat, vom folosi următoarele clase:
# Clasa Tranzactie: Reprezintă o singură operațiune financiară. 
# Proprietăți: suma, tip (venit/cheltuială), categorie, data.
# Clasa Portofel: Gestionează lista de tranzacții și bugetele. 
# Are metode precum adauga_tranzactie(), calculeaza_balanta() și verifica_buget().
# Clasa ManagerFisiere: Se ocupă strict de salvarea și citirea datelor de pe disc (salvare în JSON).
# Clasa MeniuInterfata: Gestionează interacțiunea cu utilizatorul (afișarea meniului text, citirea tastaturii).

# 4. Structura Fișierelor:
# Proiectul va fi împărțit în 4 fișiere separate pentru a respecta cerința de modularizare:
# main.py – Punctul de pornire al aplicației. Inițializează componentele și pornește bucla principală a meniului.
# modele.py – Conține logica pură de business: clasa Tranzactie și clasa Portofel.
# stocare.py – Conține clasa ManagerFisiere (responsabilă doar de citire/scriere pe hard disk).
# interfata.py – Conține clasa MeniuInterfata (print-urile în consolă și input-urile de la utilizator).

# 5. Primul pas concret în implementare:
# Definirea clasei Tranzactie în modele.py și crearea unei liste simple în care să pot adăuga manual 2-3 tranzacții de test, 
# afișându-le apoi în consolă pentru a verifica dacă logica de bază funcționează.