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

        # A variavel "inputs" funciona como um vetor de escolhas

        inputs = [
            self.escolha1.get(),
            self.escolha2.get(),
            self.escolha3.get()
        ]

        # esse jogos serve como um dicionário, onde irá armazenar o rótulo(nome) e o percentual(percentual)

        jogos = {}

        for i in db.jogos:

            soma = 0

            total = 0

            # A variavel nome existe para armazenar o nome do jogo

            nome = i["nome"]

            # armazena as características do dicionário

            caracteristicas = i["caracteristicas"]

            # passa por todos as caracteristicas

            for caracteristica in caracteristicas.keys():

                # Total armazena a caracteristica da caracteristica ou seja o peso
                # a conta é propositalmente feita utilizando o total para que apenas as caracteristicas principais prevaleçam
                # quanto mais genérico for o jogo mais baixa será a sua porcentagem

                total += caracteristicas[caracteristica]

                # Se a caracteristica estiver presente em uma das opções somar todos os pesos

                if caracteristica.upper() in inputs:
                    soma += caracteristicas[caracteristica]

            # Feito por uma regra de três

            percentual = 100 * soma / total

            # NOTA: O percentual não chega a 100%, os percentuais mostrados indicam a porcentagem de similaridade
            # do jogo escolhido com as caracteristicas escolhidas

            # O dicionário irá armazenar o rótulo e o percentual
            # jogos refere ao dicionario criado no codigo main e não no codigo db.py

            jogos[nome] = percentual

        # Jogos.items pega o rótulo e o valor transformando-a em uma matriz,o key=lambda busca o percentual

        jogos = sorted(jogos.items(), key=lambda x: x[1], reverse=True)[0:3]

        # Loopa por todos os jogos e insere os valores em seus devidos lugar buscando o dado pelo tupla

        for jogo in jogos:
            self.tree.insert("", "end", values=(jogo[0], f"{jogo[1]:.2f}%"))

    # Essa função cria a tela e posiciona os elementos na mesma
    def criar_tela(self):

        self.container = ctk.CTkFrame(self.root, fg_color="#2b2b2b", bg_color="#2b2b2b")
        self.container.grid(row=0, column=0, padx=14, pady=14)

        # cria a seleção de menu

        self.escolha1 = ctk.CTkOptionMenu(self.container, values=db.todas_opcoes, )
        self.escolha1.grid(row=0, column=0, padx=20, pady=20)

        # cria a seleção de menu

        self.escolha2 = ctk.CTkOptionMenu(self.container, values=db.todas_opcoes, )
        self.escolha2.grid(row=1, column=0, padx=20, pady=20)

        # cria a seleção de menu

        self.escolha3 = ctk.CTkOptionMenu(self.container, values=db.todas_opcoes, )
        self.escolha3.grid(row=2, column=0, padx=20, pady=20)

        # cria um botão que atualiza a tela de escolha

        self.update_button = ctk.CTkButton(self.container, text="Atualizar", command=self.analisador)
        self.update_button.grid(row=3, column=0, padx=20, pady=20)

        self.treeview()

    # Essa função tem a funcionalidade de criar a tabela branca onde serão mostrados os jogos
    def treeview(self):
        self.tree = ttk.Treeview(self.container)
        self.tree.grid(row=0, column=2, rowspan=4, padx=20, pady=20)

        self.tree["columns"] = ("#1", "#2")
        self.tree.column("#0", width=0, stretch=False)
        self.tree.column("#1", width=100, minwidth=100, stretch=True)
        self.tree.column("#2", width=100, minwidth=100, stretch=True)

        self.tree.heading("#1", text="Nome")
        self.tree.heading("#2", text="Porcentagem")


if __name__ == "__main__":
    root = ctk.CTk()
    Main(root)
