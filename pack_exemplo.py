import tkinter as tk

janela = tk.Tk()
janela.title("exemplo de Pack")
janela.geometry("300x200")

rotulo_1 = tk.Label(janela, text="Topo", bg="lightblue")
rotulo_1.pack(side=tk.TOP, fill=tk.X, pady=5, padx=5)

rotulo_2 = tk.Label(janela, text="Base", bg="lightgreen")
rotulo_2.pack(side=tk.BOTTOM, fill=tk.X, pady=5, padx=5)

rotulo_3 = tk.Label(janela, text="Esquerda", bg="lightcoral")
rotulo_3.pack(side=tk.LEFT, fill=tk.Y, padx=5)

rotulo_4 = tk.Label(janela, text="Direita", bg="lightyellow")
rotulo_4.pack(side=tk.RIGHT, fill=tk.Y, padx=5)

janela.mainloop()