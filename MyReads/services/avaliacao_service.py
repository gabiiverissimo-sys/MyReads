from database import SessionLocal
from models import Avaliacao, Livro, Usuario

def listar_avaliacoes_livro(livro_id):
    db = SessionLocal()
    livro = db.query(Livro).filter(Livro.id == livro_id).first()

    if not livro:
        print(" Livro não encontrado.")
        db.close()
        return

    avaliacoes = db.query(Avaliacao, Usuario).join(Usuario, Usuario.id == Avaliacao.usuario_id).filter(Avaliacao.livro_id == livro_id).all()

    print(f"\n=== Avaliações de '{livro.titulo}' ===")
    if not avaliacoes:
        print(" Nenhuma avaliação encontrada para este livro.")
    else:
        for av, user in avaliacoes:
            estrelas = "☆" * int(av.nota)
            print(f"{user.nome} — Nota: {av.nota:.1f} {estrelas}")
            if av.comentario:
                print(f"✎ {av.comentario}")
            print("-" * 40)

    db.close()
