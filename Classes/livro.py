class Livro:
    def __init__(self, titulo, autor, genero, ano, modelo, isbn=None):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.ano = ano
        self.modelo = modelo #fisico ou digital
        self.isbn = isbn
        self.nota = None #nota do usario
        self.status = "Quero ler"


    def avaliar(self, nota):
        if 0 <= nota <= 5:
            self.nota = nota
            print(f"\n Nota do livro '{self.titulo}': {self.nota}/5")
        else:
            print("A nota deve estar entre 0 e 5!")
    
    def __str__(self):
        texto = f"{self.titulo} — {self.autor} ({self.ano}) | Modelo: {self.modelo}"
        if self.nota is not None:
            texto += f" | Nota: {self.nota}/5"
        return texto
    
    def mudarStatus(self, novoStatus):
        if novoStatus in ["Quero ler", "Lendo", "Lido", "Desisti"]:
            self.status = novoStatus

        else:
            print("Status inválido.")

