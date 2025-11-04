from database import SessionLocal
from models import Acervo, Livro, Usuario

db = SessionLocal()

def add_possuido(usuario_id, livro_id):
    usuario = db.query(Usuario).get(usuario_id)
    if not usuario.acervo:
        usuario.acervo = Acervo(usuario_id=usuario.id)
        db.commit()
    livro = db.query(Livro).get(livro_id)
    usuario.acervo.livros.append(livro)
    db.commit()
    print(f"📗 '{livro.titulo}' adicionado aos possuídos.")

def add_desejado(usuario_id, livro_id):
    usuario = db.query(Usuario).get(usuario_id)
    if not usuario.acervo:
        usuario.acervo = Acervo(usuario_id=usuario.id)
        db.commit()
    livro = db.query(Livro).get(livro_id)
    usuario.acervo.livros.append(livro)
    db.commit()
    print(f"💭 '{livro.titulo}' adicionado aos desejados.")

def listar_acervo(usuario_id):
    usuario = db.query(Usuario).get(usuario_id)
    if usuario.acervo and usuario.acervo.livros:
        print("\n📚 Seu acervo:")
        for l in usuario.acervo.livros:
            print(f"- {l.titulo} ({l.autor})")
    else:
        print("Nenhum livro no acervo.")
