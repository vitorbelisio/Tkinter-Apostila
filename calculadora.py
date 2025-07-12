import tkinter as tk

class Calculadora:
    def __init__(self, master):
        self.master = master
        master.title("minha primeira calculadora")
        master.geometry("280x350")

        self.expressao = ""
        self.entrada_texto = tk.StringVar()

        self.display = tk.Entry(master, textvariable=self.entrada_texto, font=("Arial", 20), bd=5, relief="sunken", justify="right")
        self.display.grid(row=0, column=0, columnspan=4, padx=5, pady=5, sticky="nsew")

        botoes = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            'C', '0', '=', '+'
        ]

        #criar e posicionar botões com grid
        linha = 1
        coluna = 0

        for botao in botoes:
            comando = lambda b=botao: self.clicar_botao(b)
            if botao == '=':
                comando = self.calcular
            elif botao == 'C':
                comando = self.limpar_display

            tk.Button(master, text=botao, font=("Arial", 18), width=5, height=2, command=comando, bg="lightgray").grid(row=linha, column=coluna, padx=3, pady=3, sticky="nsew")

            coluna += 1
            if coluna > 3:
                coluna = 0
                linha += 1
        
        #redimensionar e expandir botões
        for i in range(5):
            master.grid_rowconfigure(i, weight=1)
        for i in range(4):
            master.grid_columnconfigure(i, weight=1)
    
    def clicar_botao(self, caractere):
        """Adiciona o caractere clicado à expressão."""
        self.expressao += str(caractere)
        self.entrada_texto.set(self.expressao)

    def limpar_display(self):
        """Limpa a expressão e o display."""
        self.expressao = ""
        self.entrada_texto.set("")

    def calcular(self):
        """Avaliaa expressão e exibe o resultado."""
        try:
            resultado = str(eval(self.expressao))
            self.entrada_texto.set(resultado)
            self.expressao = resultado
        except Exception as e:
            self.entrada_texto.set("Erro")
            self.expressao = ""

if __name__ == "__main__":
    root = tk.Tk()
    calc = Calculadora(root)
    root.mainloop()
            