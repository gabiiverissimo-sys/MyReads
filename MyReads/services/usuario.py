import re
from MyReads.services.acervo import Acervo

class Usuario:
    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.__senha = senha  # atributo privado
        self.listas = {}
        self.acervo = Acervo()

        # validação de e-mail
        padrao_email = r"^[\w\.-]+@[\w\.-]+\.\w+$"
        if not re.match(padrao_email, email):
            raise ValueError("Email inválido. Formato esperado: exemplo@dominio.com")

    def verificar_senha(self, senha):
        return self.__senha == senha

    def alterar_senha(self, senha_antiga, nova_senha):
        if self.verificar_senha(senha_antiga):
            self.__senha = nova_senha
            print("Senha alterada com sucesso!")
        else:
            print("Senha incorreta.")

    def adicionar_lista(self, nomeLista, lista):
        self.listas[nomeLista] = lista

    def listar_listas(self):
        if not self.listas:
            print("Nenhuma lista criada ainda.")
        else:
            for nome, lista in self.listas.items():
                print(f"- {nome} ({len(lista.livros)} livros)")

    def __str__(self):
        return f"Usuário: {self.nome} | Email: {self.email}"
