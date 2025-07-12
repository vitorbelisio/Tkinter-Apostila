import tkinter as tk
from tkinter import messagebox

def mostrar_opcoes():
    estado_check = var_check.get()
    opcao_radio= var_radio.get()

    print(f"checkbox marcado: {bool(estado_check)}")
    print(f"Opção de radio selecionada: {opcao_radio}")

def valor_slider(val):
    print(f"Valor do Slider: {int(float(val))}")
    rotulo_valor.config(text=f"Valor: {int(float(val))}")

#Menu funções
def novo_arquivo():
    messagebox.showinfo("Menu", "Novo arquivo foi criado!")

def abrir_arquivo():
    messagebox.showinfo("Menu", "Abrir arquivo...")

def sair_app():
    if messagebox.askyesno("Sair", "Deseja realmente sair?"):
        janela.quit()

#Funções pop-up (Toplevel)
def abrir_nova_janela():
    nova_janela = tk.Toplevel(janela)
    nova_janela.title("Janela Secundária")
    nova_janela.geometry("300x100")
    tk.Label(nova_janela, text="Esta é uma janela secundária.").pack(pady=20)
    #nova_janela.transient(janela) # Faz com que a nova janela fique acima da janela principal
    nova_janela.grab_set() # Impede interações com a janela  principal (modal)
    janela.wait_window(nova_janela) # Espera a nova janela ser fechada (para diálogos modais)

janela = tk.Tk()
janela.title("widgets úteis")
janela.geometry("400x400")

#Menu
barra_menu = tk.Menu(janela)
janela.config(menu=barra_menu)

#menu arquivo
menu_arquivo = tk.Menu(barra_menu, tearoff=0)
barra_menu.add_cascade(label="Arquivo", menu=menu_arquivo)

#adiciona itens ao menu "Arquivo"
menu_arquivo.add_command(label="Novo", command=novo_arquivo)
menu_arquivo.add_command(label="Abrir", command=abrir_arquivo)
menu_arquivo.add_separator()
menu_arquivo.add_command(label="Sair", command=sair_app)

#Menu ajuda
menu_ajuda = tk.Menu(barra_menu, tearoff=0)
barra_menu.add_cascade(label="Ajuda", menu=menu_ajuda)
menu_ajuda.add_command(label="Sobre", command=lambda: messagebox.showinfo("Sobre", "Aplicação de Exemplo Tkinter"))


#Check button
var_check= tk.IntVar()
check_btn = tk.Checkbutton(janela, text="aceito os termos", variable=var_check, command=mostrar_opcoes)
check_btn.pack(pady=10)

#Radio buttons
var_radio = tk.StringVar()
radio_opt1 = tk.Radiobutton(janela, text="Opção A", value="A", variable=var_radio, command=mostrar_opcoes)
radio_opt1.pack()
radio_opt2 = tk.Radiobutton(janela, text="Opção B", value="B", variable=var_radio, command=mostrar_opcoes)
radio_opt2.pack()
radio_opt3 = tk.Radiobutton(janela, text="Opção C", value="C", variable=var_radio, command=mostrar_opcoes)
radio_opt3.pack()

var_radio.set("A")

#Slider
slider = tk.Scale(janela, from_=0, to=100, orient=tk.VERTICAL, command=valor_slider)
slider.pack(pady=20)

rotulo_valor = tk.Label(janela, text="Valor: 0")
rotulo_valor.pack()

#Botão Top level
botao_abrir = tk.Button(janela, text="Abrir nova janela", command=abrir_nova_janela)
botao_abrir.pack(pady=10)

janela.mainloop()