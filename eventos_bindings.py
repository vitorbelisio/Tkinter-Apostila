import tkinter as tk

def clique_mouse(event):
    print(f"Botão do mouse clicado em X={event.x}, Y={event.y}")

def tecla_pressionada(event):
    print(f"Tecla '{event.chair}' presionada. Código: {event.keycode}")

janela = tk.Tk()
janela.title("Eventos")
janela.geometry("400x300")

rotulo = tk.Label(janela, text="Clique ou digite na janela.")
rotulo.pack(expand=True, fill=tk.BOTH)

rotulo.bind("<Button-1>", clique_mouse)
janela.bind("<Key>", tecla_pressionada)

janela.mainloop()