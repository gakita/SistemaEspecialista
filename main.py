import db
import customtkinter as ctk


class Main:
    def __init__(self, root_parameter):
        self.root = root_parameter
        self.root.geometry("500x500")
        self.root.title("Recomendador de jogos")
        self.analisador()
        self.root.mainloop()
    def analisador(self):
        input1 = ("Escreva uma característica")
        input2 = ("Escreva uma característica")
        input3 = ("Escreva uma característica")
        for i in db.jogos:
            nome = i["nome"]
            caracteristicas = i["caracteristicas"]
            if input1 in caracteristicas:



if __name__ == "__main__":
    root = ctk.CTk()
    Main(root)