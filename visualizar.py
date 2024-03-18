import tkinter as tk
from tkinter import ttk
import sqlite3
from datetime import datetime

class VisualizarHospedagens:
    def __init__(self, master):
        self.master = master
        self.master.title("Visualizar Hospedagens")
        self.master.geometry("1200x400")
        self.center_window()

        self.create_widgets()

        self.load_records()

    def center_window(self):
        self.master.update_idletasks()
        width = self.master.winfo_width()
        height = self.master.winfo_height()
        x = (self.master.winfo_screenwidth() // 2) - (width // 2)
        y = (self.master.winfo_screenheight() // 2) - (height // 2)
        self.master.geometry(f"{width}x{height}+{x}+{y}")

    def create_widgets(self):
        self.tree = ttk.Treeview(self.master, columns=("ID", "Nome", "CPF/CNPJ", "Número Pessoas",
                                                        "Quarto Escolhido", "Forma Pagamento", "50%",
                                                        "Check-in", "Check-out", "Celular", "Total Diária"),
                                 selectmode="browse", show="headings")

        self.tree.heading("ID", text="ID", anchor=tk.CENTER)
        self.tree.heading("Nome", text="Nome", anchor=tk.CENTER)
        self.tree.heading("CPF/CNPJ", text="CPF/CNPJ", anchor=tk.CENTER)
        self.tree.heading("Número Pessoas", text="Número Pessoas", anchor=tk.CENTER)
        self.tree.heading("Quarto Escolhido", text="Quarto Escolhido", anchor=tk.CENTER)
        self.tree.heading("Forma Pagamento", text="Forma Pagamento", anchor=tk.CENTER)
        self.tree.heading("50%", text="50%", anchor=tk.CENTER)
        self.tree.heading("Check-in", text="Check-in", anchor=tk.CENTER)
        self.tree.heading("Check-out", text="Check-out", anchor=tk.CENTER)
        self.tree.heading("Celular", text="Celular", anchor=tk.CENTER)
        self.tree.heading("Total Diária", text="Total Diária", anchor=tk.CENTER)

        self.tree.column("ID", width=50, anchor=tk.CENTER)
        self.tree.column("Nome", width=150, anchor=tk.CENTER)
        self.tree.column("CPF/CNPJ", width=120, anchor=tk.CENTER)
        self.tree.column("Número Pessoas", width=100, anchor=tk.CENTER)
        self.tree.column("Quarto Escolhido", width=120, anchor=tk.CENTER)
        self.tree.column("Forma Pagamento", width=150, anchor=tk.CENTER)
        self.tree.column("50%", width=80, anchor=tk.CENTER)
        self.tree.column("Check-in", width=100, anchor=tk.CENTER)
        self.tree.column("Check-out", width=100, anchor=tk.CENTER)
        self.tree.column("Celular", width=100, anchor=tk.CENTER)
        self.tree.column("Total Diária", width=120, anchor=tk.CENTER)

        self.tree.pack(fill="both", expand=True)

    def load_records(self):
        self.tree.delete(*self.tree.get_children())  # Limpa os registros existentes

        # Conectar ao banco de dados e recuperar os registros
        conn = sqlite3.connect("registros.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM hospedagens ORDER BY ID DESC")
        records = cursor.fetchall()

        for record in records:
            self.tree.insert("", "end", values=record)

        conn.close()

if __name__ == "__main__":
    root = tk.Tk()
    root.iconbitmap(r'C:\Users\lipej\Desktop\Faculdade\pousada-sistema\teste\favicon.ico')
    app = VisualizarHospedagens(root)
    root.mainloop()
