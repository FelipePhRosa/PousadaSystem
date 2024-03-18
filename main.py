import tkinter as tk
from tkinter import ttk
from registro import RegistroHospedagem  # Importa a classe RegistroHospedagem do registro.py
from visualizar import VisualizarHospedagens

class MainApplication:
    def __init__(self, master):
        self.master = master
        self.master.title("Pousada Krolow - Sistema de Hospedagem")
        self.master.geometry("400x300")
        self.center_window()

        label_titulo = ttk.Label(self.master, text="Bem-vindo à Pousada Krolow", font=("Arial", 16, "bold"))
        label_titulo.pack(pady=20)

        botao_registrar_hospedagem = ttk.Button(self.master, text="Registrar Hospedagem", command=self.abrir_registrar_hospedagem)
        botao_registrar_hospedagem.pack(pady=10)

        botao_visualizar_hospedagens = ttk.Button(self.master, text="Visualizar Hospedagens", command=self.abrir_visualizar_hospedagens)
        botao_visualizar_hospedagens.pack(pady=10)

        botao_quartos_disponiveis = ttk.Button(self.master, text="Quartos Disponíveis", command=self.abrir_quartos_disponiveis)
        botao_quartos_disponiveis.pack(pady=10)

        botao_sair = ttk.Button(self.master, text="Sair", command=self.master.destroy)
        botao_sair.pack(pady=10)

    def center_window(self):
        self.master.update_idletasks()
        width = self.master.winfo_width()
        height = self.master.winfo_height()
        x = (self.master.winfo_screenwidth() // 2) - (width // 2)
        y = (self.master.winfo_screenheight() // 2) - (height // 2)
        self.master.geometry(f"{width}x{height}+{x}+{y}")

    def abrir_registrar_hospedagem(self):
        root_registro = tk.Toplevel(self.master)
        app_registro = RegistroHospedagem(root_registro)
        self.center_window(root_registro)

    def abrir_visualizar_hospedagens(self):
        root_visualizar = tk.Toplevel(self.master)
        app_visualizar = VisualizarHospedagens(root_visualizar)
        self.center_window(root_visualizar)

    def abrir_quartos_disponiveis(self):
        print("Abrir tela de quartos disponíveis")


if __name__ == "__main__":
    root = tk.Tk()
    root.iconbitmap(r'C:\Users\lipej\Desktop\Faculdade\pousada-sistema\teste\favicon.ico')
    app = MainApplication(root)
    root.mainloop()

