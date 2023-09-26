import tkinter as tk
from tkinter import ttk
from datetime import datetime, timedelta
import pandas as pd

class DiasUteisBrasileiros:
    def __init__(self, root):
        self.root = root
        self.root.title("Dias Úteis Brasileiros")
        
        self.label_inicio = ttk.Label(root, text="Data Inicial (dd/mm/yyyy):")
        self.label_inicio.pack()
        
        self.entry_inicio = ttk.Entry(root)
        self.entry_inicio.pack()
        
        self.label_fim = ttk.Label(root, text="Data Final (dd/mm/yyyy):")
        self.label_fim.pack()
        
        self.entry_fim = ttk.Entry(root)
        self.entry_fim.pack()
        
        self.calc_button = ttk.Button(root, text="Calcular", command=self.calcular_dias_uteis)
        self.calc_button.pack()
        
        self.result_label = ttk.Label(root, text="")
        self.result_label.pack()
        
    def calcular_dias_uteis(self):
        data_inicio_str = self.entry_inicio.get()
        data_fim_str = self.entry_fim.get()
        
        try:
            data_inicio = datetime.strptime(data_inicio_str, "%d/%m/%Y")
            data_fim = datetime.strptime(data_fim_str, "%d/%m/%Y")
        except ValueError:
            self.result_label.config(text="Formato de data inválido!")
            return
        
        feriados = self.obter_feriados()
        
        dias_uteis = 0
        dia = data_inicio
        while dia <= data_fim:
            if dia.weekday() < 5 and dia not in feriados:
                dias_uteis += 1
            dia += timedelta(days=1)
        
        self.result_label.config(text=f"Dias úteis no intervalo: {dias_uteis}")
        
    def obter_feriados(self):
        # Aqui você pode adicionar feriados brasileiros, por exemplo:
        feriados = [
            datetime(datetime.now().year, 1, 1),   # Ano Novo
            datetime(datetime.now().year, 4, 21),  # Tiradentes
            datetime(datetime.now().year, 5, 1),   # Dia do Trabalho
            datetime(datetime.now().year, 9, 7),   # Independência do Brasil
            datetime(datetime.now().year, 10, 12), # Nossa Senhora Aparecida (Padroeira do Brasil)
            datetime(datetime.now().year, 11, 2),  # Dia de Finados
            datetime(datetime.now().year, 12, 25), # Natal
            # Adicione mais feriados aqui
        ]
        # Carnaval (data variável - 47 dias antes da Páscoa)
        pascoa = datetime(datetime.now().year, 4, 4)  # Data da Páscoa (Exemplo para o ano atual)
        carnaval = pascoa - timedelta(days=47)       # Carnaval é 47 dias antes da Páscoa
        feriados.append(carnaval)

        # Sexta-feira Santa (data variável - 2 dias antes da Páscoa)
        sexta_feira_santa = pascoa - timedelta(days=2) # Sexta-feira Santa é 2 dias antes da Páscoa
        feriados.append(sexta_feira_santa)

        # Corpus Christi (data variável - 60 dias após a Páscoa)
        corpus_christi = pascoa + timedelta(days=60)   # Corpus Christi é 60 dias após a Páscoa
        feriados.append(corpus_christi)
        return feriados

if __name__ == "__main__":
    root = tk.Tk()
    app = DiasUteisBrasileiros(root)
    root.mainloop()
