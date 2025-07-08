import tkinter as tk

janela = tk.Tk()
janela.title("place exemplo")
janela.geometry("300x200")

botao1 = tk.Button(janela, text="Botão 1")
botao1.place(x=50, y=50, width=100, height=30)

botao2 = tk.Button(janela, text="Botão 2")
botao2.place(relx=0.7, rely=0.7, anchor=tk.CENTER)

janela.mainloop()