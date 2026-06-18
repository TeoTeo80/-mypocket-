# FIȘA PROIECTULUI
# 1. Numele Proiectului:
# mypocket (GUI Edition)

# 2. Descrierea ideii și Obiective:
# Aplicația este un manager de finanțe personale cu o interfață grafică modernă (GUI) 
# construită în CustomTkinter.
#  Ajută utilizatorul să își monitorizeze vizual bugetul, 
# oferind ferestre și formulare interactive pentru introducerea datelor și 
# grafice simple (sau bare de progres) pentru bugete.

# Funcționalități principale:
# Interfață grafică modernă cu suport pentru Dark/Light mode.
# Formular grafic pentru adăugarea rapidă de tranzacții (câmpuri de text pentru sumă, meniuri dropdown pentru categorii).
# Afișarea tranzacțiilor într-un tabel sau listă scrollabilă direct în fereastră.
# Salvarea automată a datelor într-un fișier JSON la închiderea aplicației.

# 3. Arhitectura OOP (Clase estimate):
# CustomTkinter se bazează foarte mult pe OOP, deoarece fiecare fereastră sau componentă mare devine o clasă care moștenește din librărie:
# Clasa Tranzactie: (Rămâne neschimbată) Modelul de date pentru o tranzacție (suma, tip, categorie, data).
# Clasa Portofel: Logica din spate care calculează totalurile (venituri, cheltuieli, balanță).
# Clasa AppMypocket (moștenește customtkinter.CTk): Fereastra principală a aplicației. 
# Ea coordonează tot ce se afișează pe ecran și pornește interfața.
# Clasa FormularTranzactie (moștenește customtkinter.CTkFrame): 
# O zonă specială din fereastră (un panou) care conține butoanele, textul și meniurile unde utilizatorul introduce o tranzacție nouă.
# Clasa ManagerStocare: Salvează și încarcă datele din JSON (nu are legătură cu grafica, se ocupă doar de fișiere).

# 4. Structura Fișierelor:
# Pentru a păstra codul curat și modular, împărțim proiectul astfel:
# main.py – Punctul de pornire. Doar importă clasa ferestrei principale și o lansează în execuție.
# modele.py – Conține doar datele și calculele matematice (clasele Tranzactie și Portofel). Fără grafică aici.
# stocare.py – Conține clasa ManagerStocare pentru salvarea datelor în fișier.
# gui.py – Aici va sta tot codul greu de CustomTkinter (clasa AppMypocket și FormularTranzactie). 
# Acest fișier se va ocupa de design, butoane și culori.

# 5. Primul pas concret în implementare:
# Instalarea librăriei (pip install customtkinter) și crearea unei ferestre goale de bază în gui.py cu un singur buton ("Apasă-mă") și titlul "mypocket",
#  pentru a ne asigura că librăria grafică se încarcă și funcționează corect.