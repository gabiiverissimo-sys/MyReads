class Comentario:
    def __init__(self, usuario, livro, texto):
        self.usuario = usuario
        self.livro = livro
        self.texto = texto

    def __str__(self):
        return f"\n {self.usuario.nome} comentou sobre '{self.livro.titulo}': {self.texto}"
