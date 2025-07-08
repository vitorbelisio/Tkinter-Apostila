import tkinter as tk

# FUNÇÕES
def exibir_texto():
    texto_digitado = entrada.get()
    rotulo_saida.config(text=f"você digitou: {texto_digitado}")

# JANELA
janela = tk.Tk()
janela.title("minha primeira janela")
janela.geometry("400x200")

# LABEL instrução
rotulo_instrucao = tk.Label(janela, text="olá tkinter", font=("Arial", 16))
rotulo_instrucao.pack(pady=20)

# ENTRADA
entrada = tk.Entry(janela, width=40)
entrada.pack(pady=5)

# BUTTON
botao = tk.Button(janela, text="Clique aqui", command=exibir_texto)
botao.pack(pady=5)

# LABEL saida
rotulo_saida = tk.Label(janela, text="")
rotulo_saida.pack(pady=5)

# JANELA LOOPING
janela.mainloop()