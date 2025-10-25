
class ColecaoDeLivros:
    def __init__(self):
        self.livros = []

    def buscar(self, titulo):
        return [livro for livro in self.livros if titulo.lower() in livro.titulo.lower()]


    def adicionar(self, livro):
        if livro not in self.livros:
            self.livros.append(livro)
        else:
            print(f"O livro '{livro.titulo}' já está nesta lista.")

    def remover(self, livro):
        if livro in self.livros:
            self.livros.remove(livro)
        else:
            print(f"O livro '{livro.titulo}' não está nesta lista.")

    def listar(self):
        if not self.livros:
            print("A lista está vazia.")
        else:
            print("Livros na lista:")
            for livro in self.livros:
                print(f" - {livro.titulo} ({livro.autor})")
