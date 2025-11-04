from database import SessionLocal
from models import Acervo, Livro, livros_acervos
from sqlalchemy import insert, select


def add_desejado(usuario_id, livro_id):
    db = SessionLocal()
    acervo = db.query(Acervo).filter(Acervo.usuario_id == usuario_id).first()
    if not acervo:
        print(" Acervo não encontrado para este usuário.")
        db.close()
        return

    stmt = insert(livros_acervos).values(acervo_id=acervo.id, livro_id=livro_id, tipo="Desejado")
    db.execute(stmt)
    db.commit()
    print("✩ Livro adicionado aos desejados com sucesso!")
    db.close()


def add_possuido(usuario_id, livro_id):

    db = SessionLocal()
    acervo = db.query(Acervo).filter(Acervo.usuario_id == usuario_id).first()
    if not acervo:
        print(" Acervo não encontrado para este usuário.")
        db.close()
        return

    stmt = insert(livros_acervos).values(acervo_id=acervo.id, livro_id=livro_id, tipo="Possuído")
    db.execute(stmt)
    db.commit()
    print("✩ Livro adicionado ao acervo de possuídos com sucesso!")
    db.close()

# listar acervo do usuário
def listar_acervo(usuario_id):
    db = SessionLocal()

    acervo = db.query(Acervo).filter(Acervo.usuario_id == usuario_id).first()
    if not acervo:
        print(" Nenhum acervo encontrado para este usuário.")
        db.close()
        return

    # busca livros no acervo
    query = select(livros_acervos.c.tipo, Livro.titulo, Livro.autor, Livro.ano).join(
        Livro, Livro.id == livros_acervos.c.livro_id
    ).where(livros_acervos.c.acervo_id == acervo.id)

    resultados = db.execute(query).fetchall()

    if not resultados:
        print(" Seu acervo ainda está vazio.")
    else:
        print("\n=== Seu Acervo ===")
        for tipo, titulo, autor, ano in resultados:
            icone = "❀" if tipo == "Desejado" else "☁"
            print(f"{icone} [{tipo}] {titulo} — {autor} ({ano})")

    db.close()
