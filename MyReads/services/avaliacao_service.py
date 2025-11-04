from database import SessionLocal
from models import Avaliacao, Livro, Usuario

def avaliar_livro(usuario_id, livro_id, nota, comentario=None):

    db = SessionLocal()
    livro = db.query(Livro).filter(Livro.id == livro_id).first()

    if not livro:
        print(" Livro não encontrado.")
        db.close()
        return

    avaliacao_existente = db.query(Avaliacao).filter(
        Avaliacao.usuario_id == usuario_id,
        Avaliacao.livro_id == livro_id
    ).first()

    if avaliacao_existente:
        avaliacao_existente.nota = nota
        avaliacao_existente.comentario = comentario
        print(" Avaliação atualizada com sucesso!")
    else:
        nova_avaliacao = Avaliacao(
            usuario_id=usuario_id,
            livro_id=livro_id,
            nota=nota,
            comentario=comentario
        )
        db.add(nova_avaliacao)
        print(" Avaliação registrada com sucesso!")

    db.commit()
    db.close()


def listar_avaliacoes_livro(livro_id):
    """Lista todas as avaliações feitas para um livro específico."""
    db = SessionLocal()
    livro = db.query(Livro).filter(Livro.id == livro_id).first()

    if not livro:
        print(" Livro não encontrado.")
        db.close()
        return

    avaliacoes = db.query(Avaliacao, Usuario).join(
        Usuario, Usuario.id == Avaliacao.usuario_id
    ).filter(Avaliacao.livro_id == livro_id).all()

    print(f"\n===  Avaliações de '{livro.titulo}' ===")
    if not avaliacoes:
        print(" Nenhuma avaliação encontrada para este livro.")
    else:
        for av, user in avaliacoes:
            estrelas = "⭐" * int(round(av.nota))
            print(f"{user.nome} — Nota: {av.nota:.1f} {estrelas}")
            if av.comentario:
                print(f" {av.comentario}")
            print("-" * 40)

    db.close()
