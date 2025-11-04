from MyReads.services.ColecaoDeLivros import ColecaoDeLivros

class ListaLeitura(ColecaoDeLivros):
    def __init__(self, nome):
        super().__init__()  # chama aa superclasse
        self.nome = nome
