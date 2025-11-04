# livros_base.py

from MyReads.services.livro import Livro
from MyReads.services.acervo import Acervo

acervo_global = Acervo()

# Lista de livros disponíveis para rodar os testes
livros = [
    Livro("Mil Bejios de Garoto", "Tillie Cole", "Romance", 2017, "Físico"),
    Livro("Pássaro & Serpente", "Shelby Mahurin", "Fantasia", 2021, "Digital"),
    Livro("O Pequeno Príncipe", "Antoine de Saint-Exupéry", "Fábula", 1943, "Físico"),
    Livro("Capitães da Areia", "Jorge Amado", "Romance", 1937, "Físico"),
    Livro("Três Coroas Negras", "Kendare Blake", "Jovem Adulto", 2017, "Físico"),
    Livro("Amor de Todas as Formas", "Tatiana Amaral", "Romance", 2017, "Digital"),
    Livro("Harry Potter e o Cálice de Fogo", "J.K. Rowling", "Fantasia", 2000, "Físico"),
    Livro("Suicidas", "Raphael Montes", "Suspense Policial", 2012, "Físico"),
    Livro("Verity", "Colleen Hoover", "Thriller Psicológico", 2018, "Digital"),
    Livro("A Hora da Estrela", "Clarice Lispector", "Drama", 1977, "Físico"),
    Livro("A Canção de Aquiles", "Madeline Miller", "Mitologia / Romance", 2011, "Digital"),
    Livro("O Erro", "Elle Kennedy", "Romance New Adult", 2015, "Digital"),
]

if __name__ == "__main__":
    # add os livros à lista de desejos do acervo
    for livro in livros:
        acervo_global.add_desejado(livro)

# auxiliar para busca por título
def get_livro_por_titulo(titulo):
    for livro in livros:
        if livro.titulo.lower() == titulo.lower():
            return livro
    return None

if __name__ == "__main__":
    print("\n Lista de livros carregada para testes:")
    for i, livro in enumerate(livros, 1):
        print(f"{i}. {livro.titulo} — {livro.autor}")
