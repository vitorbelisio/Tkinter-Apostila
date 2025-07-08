import tkinter as tk
from tkinter import messagebox

class AplicacaoTarefas:
    def __init__(self, master):

        self.master = master
        master.title("Gerenciador de Tarefas")
        master.geometry("400x300")

        self.tarefas = []

        self.frame_superior = tk.Frame(master)
        self.frame_superior.pack(pady=10)

        self.rotulo_nova_tarefa = tk.Label(self.frame_superior, text="Nova tarefa")
        self.rotulo_nova_tarefa.pack(side=tk.LEFT, padx=5)

        self.entrada_tarefa = tk.Entry(self.frame_superior, width=30)
        self.entrada_tarefa.pack(side=tk.LEFT, padx=5)

        self.botao_adicionar = tk.Button(self.frame_superior, text="Adicionar", command=self.adicionar_tarefa)
        self.botao_adicionar.pack(side=tk.LEFT,padx=5)

        self.lista_tarefas = tk.Listbox(master, width=50, height=10)
        self.lista_tarefas.pack(pady=10)

        self.frame_botoes = tk.Frame(master)
        self.frame_botoes.pack(pady=5)

        self.botao_remover = tk.Button(self.frame_botoes, text="Remover", command=self.remover_tarefa)
        self.botao_remover.pack(side=tk.LEFT, padx=5)

        self.botao_limpar = tk.Button(self.frame_botoes, text="Limpar", command=self.limpar_tarefas)
        self.botao_limpar.pack(side=tk.LEFT, padx=5)

    def adicionar_tarefa(self):
        tarefa = self.entrada_tarefa.get()
        if tarefa:
            self.tarefas.append(tarefa)
            self.lista_tarefas.insert(tk.END, tarefa)
            self.entrada_tarefa.delete(0, tk.END)
        else:
            messagebox.showwarning("Aviso", "Por favor, digite uma tarefa.")

    def remover_tarefa(self):
        del self.tarefas[-1]
        self.lista_tarefas.delete(0, tk.END)
        for i in self.tarefas:
            self.lista_tarefas.insert(tk.END, i)


    def limpar_tarefas(self):
        if messagebox.askyesno("Confirmar", "Tem certeza que deseja limpar todas as tarefas?"):
            self.lista_tarefas.delete(0, tk.END)
            self.tarefas.clear()
    
if __name__=="__main__":
    root = tk.Tk()
    app = AplicacaoTarefas(root)
    root.mainloop()