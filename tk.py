import tkinter as tk
from tkinter import messagebox

class FaitsUtilisateur:
    def __init__(self):
        self.faits = []

    def ajouter_fait(self, fait):
        self.faits.append(fait)

    def supprimer_fait(self, fait):
        self.faits.remove(fait)

    def vider(self):
        self.faits = []

class Expert:
    def __init__(self, username, password):
        self.username = username
        self.password = password

class SystemeExpert:
    def __init__(self):
        self.base_de_regles = []
        self.faits_utilisateur = FaitsUtilisateur()
        self.expert = Expert("gg", "gg")

    def authentifier_expert(self, username, password):
        return username == self.expert.username and password == self.expert.password

    def ajouter_regle_expert(self, regle):
        self.base_de_regles.append(regle)
        regle_string = ""
        for i, condition in enumerate(regle.conditions):
            if i != len(regle.conditions)-1:
                regle_string += condition + ","
            else:
                regle_string += condition
        regle_string += ":"
        regle_string += regle.organe_en_panne
        with open("base.txt", 'a') as f:
            f.write(regle_string+"\n")
            


    def modifier_regle_expert(self, index, nouvelle_regle):
        self.base_de_regles[index] = nouvelle_regle

    def supprimer_regle_expert(self, index):
        del self.base_de_regles[index]

    def ajouter_fait_utilisateur(self, fait):
        self.faits_utilisateur.ajouter_fait(fait)

    def supprimer_fait_utilisateur(self, fait):
        self.faits_utilisateur.supprimer_fait(fait)

    def vider_faits_utilisateur(self):
        self.faits_utilisateur.vider()

    def raisonner(self):
        organes_en_panne = set()
        for regle in self.base_de_regles:
            print("regle", regle)
            if regle.satisfait(self.faits_utilisateur.faits):
                organes_en_panne.add(regle.organe_en_panne)
        return organes_en_panne

class Regle:
    def __init__(self, conditions, organe_en_panne):
        self.conditions = conditions
        self.organe_en_panne = organe_en_panne

    def satisfait(self, faits_utilisateur):
        return any(set(self.conditions).issubset(set(fait)) for fait in faits_utilisateur)

class App:
    def __init__(self, master):
        self.master = master
        self.master.title("Systeme Expert - Diagnostic PC")
        self.systeme_expert = SystemeExpert()

        self.login_frame = tk.Frame(self.master)
        self.login_frame.pack(padx=20, pady=20)

        self.username_label = tk.Label(self.login_frame, text="Username:")
        self.username_label.grid(row=0, column=0, sticky=tk.E)

        self.username_entry = tk.Entry(self.login_frame)
        self.username_entry.grid(row=0, column=1)

        self.password_label = tk.Label(self.login_frame, text="Password:")
        self.password_label.grid(row=1, column=0, sticky=tk.E)

        self.password_entry = tk.Entry(self.login_frame, show="*")
        self.password_entry.grid(row=1, column=1)

        self.login_button = tk.Button(self.login_frame, text="Login", command=self.authenticate)
        self.login_button.grid(row=2, column=0, columnspan=2, pady=10)

        self.diagnostic_frame = tk.Frame(self.master)
        self.diagnostic_frame.pack(padx=20, pady=20)

        self.result_label = tk.Label(self.diagnostic_frame, text="")
        self.result_label.grid(row=3, column=0, columnspan=2, pady=10)

        self.symptoms_label = tk.Label(self.diagnostic_frame, text="Liste des symptômes :")
        self.symptoms_label.grid(row=0, column=0, columnspan=2)

        self.set_up_regle_base()

        self.symptoms_listbox = tk.Listbox(self.diagnostic_frame, selectmode=tk.MULTIPLE)
        for i, regle in enumerate(self.systeme_expert.base_de_regles, start=1):
            self.symptoms_listbox.insert(tk.END, f"{i}. {', '.join(regle.conditions)}")
        self.symptoms_listbox.grid(row=1, column=0, columnspan=2, pady=10)

        self.diagnose_button = tk.Button(self.diagnostic_frame, text="Faire un diagnostic", command=self.diagnose)
        self.diagnose_button.grid(row=2, column=0, columnspan=2, pady=10)

    def set_up_regle_base(self):
        with open("base.txt", 'r') as f:
            data = f.readlines()
    
        for line in data:
            regle = line.split(":")
            conditions = regle[0].split(",")
            organe = regle[1].strip("\n")
            new_regle = Regle(conditions, organe)
            self.systeme_expert.base_de_regles.append(new_regle)

    def authenticate(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if self.systeme_expert.authentifier_expert(username, password):
            messagebox.showinfo("Authentication", "Authentication successful!")
            self.login_frame.destroy()
            self.setup_expert_session()
        else:
            messagebox.showerror("Authentication", "Authentication failed. Please try again.")

    def setup_expert_session(self):
        self.expert_frame = tk.Frame(self.master)
        self.expert_frame.pack(padx=20, pady=20)

        self.add_rule_button = tk.Button(self.expert_frame, text="Ajouter une nouvelle règle", command=self.show_add_rule_dialog)
        self.add_rule_button.grid(row=0, column=0, columnspan=2, pady=10)

    def show_add_rule_dialog(self):
        add_rule_dialog = tk.Toplevel(self.expert_frame)
        add_rule_dialog.title("Ajouter une nouvelle règle")

        conditions_label = tk.Label(add_rule_dialog, text="Conditions (séparées par des virgules):")
        conditions_label.grid(row=0, column=0, sticky=tk.E)

        conditions_entry = tk.Entry(add_rule_dialog)
        conditions_entry.grid(row=0, column=1)

        organ_label = tk.Label(add_rule_dialog, text="Organe en panne:")
        organ_label.grid(row=1, column=0, sticky=tk.E)

        organ_entry = tk.Entry(add_rule_dialog)
        organ_entry.grid(row=1, column=1)

        add_button = tk.Button(add_rule_dialog, text="Ajouter", command=lambda: self.add_rule_from_dialog(conditions_entry.get(), organ_entry.get(), add_rule_dialog))
        add_button.grid(row=2, column=0, columnspan=2, pady=10)

    def add_rule_from_dialog(self, conditions, organ, dialog):
        if conditions and organ:
            new_rule = Regle(conditions.split(", "), organ)
            self.systeme_expert.ajouter_regle_expert(new_rule)
            self.symptoms_listbox.insert(tk.END, f"{len(self.systeme_expert.base_de_regles)}. {', '.join(new_rule.conditions)}")
            messagebox.showinfo("Nouvelle règle", "Nouvelle règle ajoutée avec succès!")
            dialog.destroy()
        else:
            messagebox.showwarning("Erreur", "Veuillez remplir tous les champs.")

    def add_rule(self):
        pass

    def add_faulty_organ(self):
        pass

    def diagnose(self):
        selected_indices = self.symptoms_listbox.curselection()
    

        if not selected_indices:
            messagebox.showwarning("Diagnosis", "Veuillez sélectionner au moins un symptôme.")
            return

        faits_utilisateur = [regle.conditions for i, regle in enumerate(self.systeme_expert.base_de_regles) if i in selected_indices]

        for fait_utilisateur in faits_utilisateur:
            self.systeme_expert.ajouter_fait_utilisateur(fait_utilisateur)  
    

        organes_en_panne = self.systeme_expert.raisonner()

        if organes_en_panne:
            result_text = f"Les organes potentiellement en panne sont : {', '.join(organes_en_panne)}"
        else:
            result_text = "Aucun organe en panne détecté."

        self.systeme_expert.vider_faits_utilisateur()

        self.result_label.config(text=result_text)

if __name__ == "__main__":
            
    root = tk.Tk()
    app = App(root)
    root.mainloop()
