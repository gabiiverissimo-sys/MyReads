class Acervo:
    def __init__(self):
        self.lista_desejos = []
        self.lista_possuidos  = []
 

    def add_possuido(self, livro):
        if livro not in self.lista_possuidos:
            self.lista_possuidos.append(livro)
            print(f"'{livro.titulo}' foi adicionado à sua lista de possuídos.")
        else:
            print(f"'{livro.titulo}' já está no acervo.")


    def add_desejado(self, livro):
        if livro not in self.lista_desejos:
            self.lista_desejos.append(livro)
            print(f"'{livro.titulo}' foi adicionado à sua lista de desejos.")
        else:
            print(f"'{livro.titulo}' já está na sua lista de desejos.")


    def listar_possuidos(self):
        print("\n ☆Livros Possuídos☆")
        if not self.lista_possuidos:
            print("Nenhum livro no acervo.")
        else:
            for livro in self.lista_possuidos:
                print(f" - {livro.titulo}")

    def listar_desejados(self):
        print("\n ☆Lista de Desejos☆")
        if not self.lista_desejos:
            print("Nenhum livro na lista de desejos.")
        else:
            for livro in self.lista_desejos:
                print(f" - {livro.titulo}")

    def esta_acervo(self, livro):
        return livro in self.lista_possuidos or livro in self.lista_desejos
