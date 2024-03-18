import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
import sqlite3
from ttkthemes import ThemedTk

class RegistroHospedagem:
    def __init__(self, master):
        self.master = master
        self.master.title("Formulário de Hospedagem")
        self.master.geometry("600x360")
        self.center_window()

        self.create_database_table()
        self.create_widgets()

    
    def create_database_table(self):
        self.conexao = sqlite3.connect("registros.db")
        self.cursor = self.conexao.cursor()

        # Verifica se a tabela existe
        self.cursor.execute('''
            SELECT name FROM sqlite_master WHERE type='table' AND name='hospedagens'
        ''')
        table_exists = self.cursor.fetchone()

        # Se a tabela não existir, cria a tabela
        if not table_exists:
            self.cursor.execute('''
                CREATE TABLE hospedagens (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT,
                    cpf_cnpj TEXT,
                    num_pessoas INTEGER,
                    quarto_escolhido TEXT,
                    forma_pagamento TEXT,
                    pagou_50 BOOLEAN,
                    celular TEXT,
                    total_diaria TEXT,
                    data_entrada TEXT,
                    data_saida REAL
                )
            ''')
            self.conexao.commit()
        else:
            # Verifica se a coluna celular existe na tabela
            self.cursor.execute('PRAGMA table_info(hospedagens)')
            columns = self.cursor.fetchall()
            column_names = [column[1] for column in columns]
            if 'celular' not in column_names:
                # Adiciona a coluna celular à tabela
                self.cursor.execute('ALTER TABLE hospedagens ADD COLUMN celular TEXT')
                self.conexao.commit()

    
    def center_window(self):
        self.master.update_idletasks()
        width = self.master.winfo_width()
        height = self.master.winfo_height()
        x = (self.master.winfo_screenwidth() // 2) - (width // 2)
        y = (self.master.winfo_screenheight() // 2) - (height // 2)
        self.master.geometry(f"{width}x{height}+{x}+{y}")


    def create_widgets(self):
        # Adição de widgets
        self.label_nome = tk.Label(self.master, text="Nome:")
        self.entry_nome_var = tk.StringVar()
        self.entry_nome = tk.Entry(self.master, textvariable=self.entry_nome_var)

        self.label_cpf_cnpj = tk.Label(self.master, text="CPF/CNPJ:")
        self.entry_cpf_cnpj_var = tk.StringVar()
        self.entry_cpf_cnpj = tk.Entry(self.master, textvariable=self.entry_cpf_cnpj_var)

        self.label_num_pessoas = tk.Label(self.master, text="Número de Pessoas:")
        self.entry_num_pessoas_var = tk.StringVar()
        self.entry_num_pessoas = tk.Entry(self.master, textvariable=self.entry_num_pessoas_var)

        self.label_quarto = tk.Label(self.master, text="Quarto Escolhido:")
        self.entry_quarto_var = tk.StringVar()
        self.entry_quarto = tk.Entry(self.master, textvariable=self.entry_quarto_var)

        self.label_forma_pagamento = tk.Label(self.master, text="Forma de Pagamento:")
        self.entry_forma_pagamento_var = tk.StringVar()
        self.entry_forma_pagamento = tk.Entry(self.master, textvariable=self.entry_forma_pagamento_var)

        self.label_pagou_50 = tk.Label(self.master, text="Pagou 50%:")
        self.entry_pagou_50_var = tk.StringVar()
        self.entry_pagou_50 = tk.Entry(self.master, textvariable=self.entry_pagou_50_var)

        # Caixa de texto para o total da diária
        self.label_total_diaria = tk.Label(self.master, text="Total da diária:")
        self.entry_total_diaria_var = tk.StringVar()
        self.entry_total_diaria = tk.Entry(self.master, textvariable=self.entry_total_diaria_var)
        
        # Caixa de texto para o celular
        self.label_celular = tk.Label(self.master, text="Celular:")
        self.entry_celular_var = tk.StringVar()
        self.entry_celular = tk.Entry(self.master, textvariable=self.entry_celular_var)

        self.label_data_entrada = tk.Label(self.master, text="Check-in (DD/MM/AAAA):")
        self.entry_data_entrada_var = tk.StringVar()
        self.entry_data_entrada = tk.Entry(self.master, textvariable=self.entry_data_entrada_var)

        self.label_data_saida = tk.Label(self.master, text="Check-out (DD/MM/AAAA):")
        self.entry_data_saida_var = tk.StringVar()
        self.entry_data_saida = tk.Entry(self.master, textvariable=self.entry_data_saida_var)

        self.botao_imprimir = tk.Button(self.master, text="Imprimir Dados", command=self.imprimir_dados)

        self.resultado = tk.Label(self.master, text="")

        # Lista de nomes dos quartos
        nomes_quartos = ["Rei Alberto", "Camafeu", "Merengue", "Bem casado", "Beijinho de Coco",
                         "Ninho", "Fio De Ovos", "Brigadeiro", "Olho de Sogra"]
        
        formas_pagamento = ["Espécie", "Débito", "Crédito", "Pix", "Faturado"]

        # Layout dos widgets
        self.label_nome.grid(row=0, column=0, padx=90, pady=5, sticky="w")
        self.entry_nome.grid(row=0, column=1, padx=10, pady=5)

        self.label_cpf_cnpj.grid(row=1, column=0, padx=90, pady=5, sticky="w")
        self.entry_cpf_cnpj.grid(row=1, column=1, padx=10, pady=5)

        self.label_num_pessoas.grid(row=2, column=0, padx=90, pady=5, sticky="w")
        self.entry_num_pessoas.grid(row=2, column=1, padx=10, pady=5)

        # Label e Combobox para seleção do quarto
        self.label_quarto.grid(row=3, column=0, padx=90, pady=5, sticky="w")
        self.combo_quarto = ttk.Combobox(self.master, values=nomes_quartos, textvariable=self.entry_quarto_var, width=17)
        self.combo_quarto.grid(row=3, column=1, padx=10, pady=5, sticky="w")

        self.label_forma_pagamento.grid(row=4, column=0, padx=90, pady=5, sticky="w")
        self.combo_forma_pagamento = ttk.Combobox(self.master, values=formas_pagamento, textvariable=self.entry_forma_pagamento_var, width=17)
        self.combo_forma_pagamento.grid(row=4, column=1, padx=10, pady=5, sticky="w")


        self.label_pagou_50.grid(row=5, column=0, padx=90, pady=5, sticky="w")
        self.entry_pagou_50.grid(row=5, column=1, padx=10, pady=5)

        # Layout dos novos widgets
        self.label_total_diaria.grid(row=6, column=0, padx=90, pady=5, sticky="w")
        self.entry_total_diaria.grid(row=6, column=1, padx=10, pady=5)
        
        self.label_celular.grid(row=7, column=0, padx=90, pady=5, sticky="w")
        self.entry_celular.grid(row=7, column=1, padx=10, pady=5)

        self.label_data_entrada.grid(row=8, column=0, padx=90, pady=5, sticky="w")
        self.entry_data_entrada.grid(row=8, column=1, padx=10, pady=5)

        self.label_data_saida.grid(row=9, column=0, padx=90, pady=5, sticky="w")
        self.entry_data_saida.grid(row=9, column=1, padx=10, pady=5)

        self.botao_imprimir.place(relx=0.5, rely=0.97, anchor="s")  # Adiciona place para posicionar no centro inferior

        # Caixa de texto para o total da diária
        self.label_total_diaria = tk.Label(self.master, text="Total da diária:")
        self.entry_total_diaria_var = tk.StringVar()
        self.entry_total_diaria = tk.Entry(self.master, textvariable=self.entry_total_diaria_var)
        
        # Caixa de texto para o celular
        self.label_celular = tk.Label(self.master, text="Celular:")
        self.entry_celular_var = tk.StringVar()
        self.entry_celular = tk.Entry(self.master, textvariable=self.entry_celular_var)
        

        # Configurar eventos <<FocusOut>> para adicionar barras automaticamente
        self.entry_data_entrada_var.trace_add('write', self.adicionar_barras_entrada)
        self.entry_data_saida_var.trace_add('write', self.adicionar_barras_saida)

        # Configurar eventos para limitar o número de caracteres
        self.entry_data_entrada_var.trace_add('write', self.limitar_caracteres_entrada)
        self.entry_data_saida_var.trace_add('write', self.limitar_caracteres_saida)

        # Configurar eventos para validar o nome e as datas
        self.entry_nome_var.trace_add('write', self.validar_nome)
        self.entry_cpf_cnpj_var.trace_add('write', self.validar_cpf_cnpj)
        self.entry_num_pessoas_var.trace_add('write', self.validar_num_pessoas)
        self.entry_quarto_var.trace_add('write', self.validar_quarto)
        self.entry_forma_pagamento_var.trace_add('write', self.validar_forma_pagamento)
        self.entry_pagou_50_var.trace_add('write', self.validar_pagou_50)

        # Configurar eventos para a caixa de texto do celular
        self.entry_celular_var.trace_add('write', self.validar_celular)
    
    def imprimir_dados(self):
        nome = self.entry_nome_var.get()
        cpf_cnpj = self.entry_cpf_cnpj_var.get()
        num_pessoas = self.entry_num_pessoas_var.get()
        quarto_escolhido = self.entry_quarto_var.get()
        forma_pagamento = self.combo_forma_pagamento.get()
        pagou_50 = self.entry_pagou_50_var.get()
        celular = self.entry_celular_var.get()  # Novo campo
        total_diaria = self.entry_total_diaria_var.get()  # Novo campo

        data_entrada = self.entry_data_entrada_var.get()
        data_saida = self.entry_data_saida_var.get()

        try:
            # Verifica se o nome contém apenas letras e espaços
            if not nome.replace(" ", "").isalpha():
                raise ValueError("O nome deve conter apenas letras e espaços.")

            # Remove caracteres especiais e letras das datas
            data_entrada = self.remover_caracteres_especiais(data_entrada)
            data_saida = self.remover_caracteres_especiais(data_saida)

            # Verifica se as datas contêm apenas números e barras
            if not data_entrada.replace("/", "").isdigit() or not data_saida.replace("/", "").isdigit():
                raise ValueError("As datas devem conter apenas números e barras.")

            # Tenta converter as datas para verificar se são válidas
            data_entrada_obj = datetime.strptime(data_entrada, "%d/%m/%Y")
            data_saida_obj = datetime.strptime(data_saida, "%d/%m/%Y")


            # Inserir dados no banco de dados
            self.cursor.execute('''
            INSERT INTO hospedagens (
                nome, cpf_cnpj, num_pessoas, quarto_escolhido,
                forma_pagamento, pagou_50, data_entrada, data_saida,
                celular, total_diaria
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (nome, cpf_cnpj, num_pessoas, quarto_escolhido,
            forma_pagamento, pagou_50, data_entrada, data_saida,
            celular, total_diaria))

            self.conexao.commit()


            # Verifica se a Check-out é maior ou igual à Check-in
            if data_saida_obj >= data_entrada_obj:
                self.resultado.config(text=f"Nome: {nome}\nCPF/CNPJ: {cpf_cnpj}\nNúmero de Pessoas: {num_pessoas}\n"
                                           f"Quarto Escolhido: {quarto_escolhido}\nForma de Pagamento: {forma_pagamento}\n"
                                           f"Pagou 50%: {pagou_50}\n "
                                           f"Total: {total_diaria}\n "
                                           f"Celular: {celular}\n"
                                           f"Entrada: {data_entrada}\nSaída: {data_saida}")
                self.resultado.config(fg="green", font=("Arial", 12, "bold"))
                self.resultado.place(relx=0.5, rely=0.85, anchor="s")
                # Aumenta a altura da janela para exibir o resultado
                self.master.geometry("700x600")
                # Limpa as caixas de entrada
                self.entry_nome_var.set("")
                self.entry_cpf_cnpj_var.set("")
                self.entry_num_pessoas_var.set("")
                self.entry_quarto_var.set("")
                self.entry_forma_pagamento_var.set("")
                self.entry_pagou_50_var.set("")
                self.entry_data_entrada_var.set("")
                self.entry_data_saida_var.set("")
            else:
                raise ValueError("Check-out deve ser após a Check-in.")

        except ValueError as e:
            # Em caso de erro, exibe uma mensagem de erro
            messagebox.showerror("Erro", str(e))

    def adicionar_barras_entrada(self, *args):
        # Adiciona as barras automaticamente após dois caracteres e quatro caracteres
        value = self.entry_data_entrada_var.get()
        if len(value) == 2 and value[1] != '/':
            self.entry_data_entrada_var.set(value[:2] + '/' + value[2:])
            self.entry_data_entrada.delete(0, tk.END)
            self.entry_data_entrada.insert(tk.END, value[:2] + '/' + value[2:])
            self.entry_data_entrada.icursor(tk.END)  # Posiciona o cursor no final
        elif len(value) == 5 and value[4] != '/':
            self.entry_data_entrada_var.set(value[:2] + '/' + value[3:])
            self.entry_data_entrada.delete(0, tk.END)
            self.entry_data_entrada.insert(tk.END, value[:5] + '/' + value[7:])
            self.entry_data_entrada.icursor(tk.END)  # Posiciona o cursor no final

    def adicionar_barras_saida(self, *args):
        # Adiciona as barras automaticamente após dois caracteres e quatro caracteres
        value = self.entry_data_saida_var.get()
        if len(value) == 2 and value[1] != '/':
            self.entry_data_saida_var.set(value[:2] + '/' + value[2:])
            self.entry_data_saida.delete(0, tk.END)
            self.entry_data_saida.insert(tk.END, value[:2] + '/' + value[2:])
            self.entry_data_saida.icursor(tk.END)  # Posiciona o cursor no final
        elif len(value) == 5 and value[4] != '/':
            self.entry_data_saida_var.set(value[:2] + '/' + value[3:])
            self.entry_data_saida.delete(0, tk.END)
            self.entry_data_saida.insert(tk.END, value[:5] + '/' + value[7:])
            self.entry_data_saida.icursor(tk.END)  # Posiciona o cursor no final

    def validar_nome(self, *args):
        nome = self.entry_nome_var.get()
        # Remove caracteres especiais e números
        nome_valido = "".join(c for c in nome if c.isalpha() or c.isspace())
        self.entry_nome_var.set(nome_valido)

    def validar_cpf_cnpj(self, *args):
        cpf_cnpj = self.entry_cpf_cnpj_var.get()
        # Remove caracteres não numéricos
        cpf_cnpj_valido = "".join(c for c in cpf_cnpj if c.isdigit())
        self.entry_cpf_cnpj_var.set(cpf_cnpj_valido)

    def validar_celular(self, *args):
        # Remove caracteres não numéricos ou não "+" da entrada
        celular = self.entry_celular_var.get()
        celular_valido = "".join(c for c in celular if c.isdigit() or c == "+")
        self.entry_celular_var.set(celular_valido)

    def validar_num_pessoas(self, *args):
        num_pessoas = self.entry_num_pessoas_var.get()
        # Remove caracteres não numéricos
        num_pessoas_valido = "".join(c for c in num_pessoas if c.isdigit())
        self.entry_num_pessoas_var.set(num_pessoas_valido)

    def validar_quarto(self, *args):
        quarto = self.entry_quarto_var.get()
        # Sua lógica de validação para o quarto escolhido, pode ser uma lista predefinida, etc.

    def validar_forma_pagamento(self, *args):
        forma_pagamento = self.entry_forma_pagamento_var.get()
        # Sua lógica de validação para a forma de pagamento, pode ser uma lista predefinida, etc.

    def validar_pagou_50(self, *args):
        pagou_50 = self.entry_pagou_50_var.get()
        # Sua lógica de validação para se pagou 50%, pode ser um campo booleano, etc.

    def remover_caracteres_especiais(self, texto):
        return ''.join(c for c in texto if c.isalnum() or c.isspace() or c == '/')

    def limitar_caracteres_entrada(self, *args):
        value = self.entry_data_entrada_var.get()
        if len(value) > 10:
            self.entry_data_entrada_var.set(value[:10])

    def limitar_caracteres_saida(self, *args):
        value = self.entry_data_saida_var.get()
        if len(value) > 10:
            self.entry_data_saida_var.set(value[:10])


if __name__ == "__main__":
    root = tk.Tk()
    root.iconbitmap(r'C:\Users\lipej\Desktop\Faculdade\pousada-sistema\teste\favicon.ico')
    app = RegistroHospedagem(root)
    root.mainloop()
    app.conexao.close()