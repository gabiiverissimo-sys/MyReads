from database import SessionLocal
from models import Livro

db = SessionLocal()

# catalago inicial
livros_iniciais = [
    ("O Senhor dos Anéis", "J.R.R. Tolkien", "Fantasia", 1954, "Físico"),
    ("Harry Potter e a Pedra Filosofal", "J.K. Rowling", "Fantasia", 1997, "Digital"),
    ("Dom Casmurro", "Machado de Assis", "Romance", 1899, "Físico"),
    ("A Menina que Roubava Livros", "Markus Zusak", "Drama", 2005, "Digital"),
    ("O Pequeno Príncipe", "Antoine de Saint-Exupéry", "Infantil", 1943, "Físico"),
    ("1984", "George Orwell", "Distopia", 1949, "Digital"),
    ("O Código Da Vinci", "Dan Brown", "Mistério", 2003, "Físico"),
    ("A Culpa é das Estrelas", "John Green", "Romance", 2012, "Digital"),
    ("Mil Bejios de Garoto", "Tillie Cole", "Romance", 2017, "Físico"),
    ("Pássaro & Serpente", "Shelby Mahurin", "Fantasia", 2021, "Digital"),
    ("Capitães da Areia", "Jorge Amado", "Romance", 1937, "Físico"),
    ("Três Coroas Negras", "Kendare Blake", "Jovem Adulto", 2017, "Físico"),
    ("Amor de Todas as Formas", "Tatiana Amaral", "Romance", 2017, "Digital"),
    ("Harry Potter e o Cálice de Fogo", "J.K. Rowling", "Fantasia", 2000, "Físico"),
    ("Suicidas", "Raphael Montes", "Suspense Policial", 2012, "Físico"),
    ("Verity", "Colleen Hoover", "Thriller Psicológico", 2018, "Digital"),
    ("A Hora da Estrela", "Clarice Lispector", "Drama", 1977, "Físico"),
    ("A Canção de Aquiles", "Madeline Miller", "Mitologia / Romance", 2011, "Digital"),
    ("O Erro", "Elle Kennedy", "Romance New Adult", 2015, "Digital"),
]

for titulo, autor, genero, ano, modelo in livros_iniciais:
    existente = db.query(Livro).filter_by(titulo=titulo).first()
    if not existente:
        livro = Livro(titulo=titulo, autor=autor, genero=genero, ano=ano, modelo=modelo)
        db.add(livro)
        print(f" Adicionado: {titulo}")
    else:
        print(f" Já existia: {titulo}")

db.commit()
print(" Catálogo inicial de livros inserido com sucesso!")
