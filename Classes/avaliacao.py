class Avaliacao:
    def __init__(self, livro, nota, comentario=""):

        if isinstance(nota, str):
            nota = nota.replace(",", ".")  # troca vírgula por ponto
        try:
            nota = float(nota)
        except ValueError:
            raise ValueError("A nota deve ser um número entre 0 e 5.")
        
        self.livro = livro
        self.nota = nota
        self.comentario = comentario

    def __str__(self):
        return f"{self.livro.titulo} - Nota: {self.nota}/5 | {self.comentario}"
