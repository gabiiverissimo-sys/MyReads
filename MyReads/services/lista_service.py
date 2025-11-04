from database import SessionLocal
from models import ListaLeitura, Livro, Usuario

db = SessionLocal()

def criar_lista(usuario_id, nome):
    lista = ListaLeitura(nome=nome, usuario_id=usuario_id)
    db.add(lista)
    db.commit()
    print(f" Lista '{nome}' criada com sucesso!")

def adicionar_livro_na_lista(lista_id, livro_id):
    lista = db.query(ListaLeitura).get(lista_id)
    livro = db.query(Livro).get(livro_id)
    if lista and livro:
        lista.livros.append(livro)
        db.commit()
        print(f" '{livro.titulo}' adicionado à lista '{lista.nome}'.")

def listar_listas_do_usuario(usuario_id):
    listas = db.query(ListaLeitura).filter_by(usuario_id=usuario_id).all()
    for l in listas:
        print(f"- ID {l.id}: {l.nome} ({len(l.livros)} livros)")
