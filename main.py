import db
import customtkinter as ctk
from tkinter import ttk


class Main:
    def __init__(self, root_parameter):
        self.root = root_parameter
        self.root.geometry("450x300")
        self.root.title("Recomendador de jogos")
        self.root.config(bg="#2b2b2b")
        self.root.resizable(False, False)
        self.criar_tela()
        self.root.mainloop()
    def analisador(self):
        """Esta função faz a analise do jogo e mostra os 3 jogos mais compatíveis passando por uma lista de inputs, que sao as caracteristicas do jogo,cria um dicionario para armazenar o rótulo e o percentual e depois mostra os 3 jogos mais compatíveis"""
        self.tree.delete(*self.tree.get_children())
        inputs = [
            self.escolha1.get(),
            self.escolha2.get(),
            self.escolha3.get()
        ]
        #esse jogos serve como um dicionário, onde irá armazenar o rótulo(nome) e o percentual(percentual)
        jogos = {}
        for i in db.jogos:
            soma = 0
            total = 0
            nome = i["nome"]
            #acessa as características do dicionário
            caracteristicas = i["caracteristicas"]
            #passa por todos os pesos 
            for caracteristica in caracteristicas.keys():
                total += caracteristicas[caracteristica]
                #se a caracteristica estiver presente em uma das opções somar todos os pesos
                if caracteristica.upper() in inputs:
                    soma += caracteristicas[caracteristica]
            percentual = 100*soma/total
            #o dicionário irá armazenar o rótulo e o percentual
            jogos[nome] = percentual

        jogos= sorted(jogos.items(), key=lambda x: x[1], reverse=True)[0:3]

        for jogo in jogos:
            self.tree.insert("", "end", values=(jogo[0], f"{jogo[1]:.2f}%"))

#Essa função cria a tela e poosiciona os elementos na mesma
    def criar_tela(self):

        self.container = ctk.CTkFrame(self.root)
        self.container.grid(row=0, column=0, padx=13.5, pady=13.4)
#cria a seleção de menu
        self.escolha1 = ctk.CTkOptionMenu(self.container,values=db.todas_opcoes,)
        self.escolha1.grid(row=0, column=0, padx=20, pady=20)
#cria a seleção de menu
        self.escolha2 = ctk.CTkOptionMenu(self.container, values=db.todas_opcoes, )
        self.escolha2.grid(row=1, column=0, padx=20, pady=20)
#cria a seleção de menu
        self.escolha3 = ctk.CTkOptionMenu(self.container, values=db.todas_opcoes, )
        self.escolha3.grid(row=2, column=0, padx=20, pady=20)
#cria um botão que atualiza a tela de escolha
        self.update_button = ctk.CTkButton(self.container, text="Atualizar", command=self.analisador)
        self.update_button.grid(row=3, column=0, padx=20, pady=20)

        self.treeview()
#Essa função tem a funcionalidade de criar a tabela branca onde serão mostrados os jogos
    def treeview(self):
        self.tree = ttk.Treeview(self.container)
        self.tree.grid(row=0, column=2,rowspan=4, padx=20, pady=20)

        self.tree["columns"] = ("#1", "#2")
        self.tree.column("#0", width=0, stretch=False)
        self.tree.column("#1", width=100, minwidth=100, stretch=True)
        self.tree.column("#2", width=100, minwidth=100, stretch=True)

        self.tree.heading("#1", text="Nome")
        self.tree.heading("#2", text="Porcentagem")





if __name__ == "__main__":
    root = ctk.CTk()
    Main(root)
