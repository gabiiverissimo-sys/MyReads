from database import SessionLocal
from models import Livro

db = SessionLocal()

def adicionar_livro(titulo, autor, genero, ano, modelo, isbn=None):
    livro = Livro(titulo=titulo, autor=autor, genero=genero, ano=ano, modelo=modelo, isbn=isbn)
    db.add(livro)
    db.commit()
    print(f"✅ Livro '{titulo}' adicionado com sucesso!")

def listar_livros():
    livros = db.query(Livro).all()
    for l in livros:
        print(f"- {l.titulo} ({l.autor}) [{l.status}]")

def mudar_status(livro_id, novo_status):
    livro = db.query(Livro).get(livro_id)
    if livro:
        livro.status = novo_status
        db.commit()
        print(f"🔄 Status do livro '{livro.titulo}' alterado para '{novo_status}'.")
