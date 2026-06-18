import customtkinter as ctk
from modele import Tranzactie, Portofel
from stocare import ManagerStocare

# Setări generale pentru un aspect modern
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

class FormularTranzactie(ctk.CTkFrame):
    def __init__ (self, master, functie_adaugare, **kwargs):
        # master = fereastra principala AppMyPocket
        super().__init__(master, **kwargs)
        self.functie_adaugare = functie_adaugare # salvam functia primita la fereastra principala

        # 1. Titlul formularului (.pack() le așază pe ecran unele sub altele, cu o distanță/pady)

        self.label_titlu = ctk.CTkLabel(self, text="Tranzactie noua", font=ctk.CTkFont(size=16, weight="bold"))
        self.label_titlu.pack(pady=15, padx=10)

        # 2. Câmpul de text pentru Sumă. 
        # 'placeholder_text' este textul gri ajutător care dispare când userul începe să tasteze.

        self.entry_suma = ctk.CTkEntry(self, placeholder_text="Suma (ex:46.50)")
        self.entry_suma.pack(pady=10, padx = 15, fill = "x") # fill"x" întinde căsuța pe toată lățimea disponibilă

        # 3. Meniul Dropdown pentru selectarea Tipului (Venit sau Cheltuială)
        