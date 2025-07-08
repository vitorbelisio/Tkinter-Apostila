import tkinter as tk

def enviar_dados():
    nome = entrada_nome.get()
    email = entrada_email.get()
    print(f"Nome: {nome}, Email: {email}")
    rotulo_status.config(text="dados enviados!", fg="green")

janela = tk.Tk()
janela.title("GRID")
janela.geometry("300x200")

rotulo_nome = tk.Label(janela, text="Nome:")
rotulo_nome.grid(row=0, column=0, padx=5, pady=5, sticky="w")

entrada_nome = tk.Entry(janela, width=30)
entrada_nome.grid(row=0, column=1, padx=5, pady=5)

rotulo_email = tk.Label(janela, text="Email:")
rotulo_email.grid(row=1, column=0, padx=5, pady=5, sticky="w")

entrada_email = tk.Entry(janela, width=30)
entrada_email.grid(row=1, column=1, padx=5, pady=5)

botao_enviar = tk.Button(janela, text="Enviar", command=enviar_dados)
botao_enviar.grid(row=2, column=0, columnspan=2, pady=10)

rotulo_status = tk.Label(janela, text="")
rotulo_status.grid(row=3, column=0, columnspan=2)

janela.mainloop()