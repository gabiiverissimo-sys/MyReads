from database import SessionLocal
from models import Avaliacao, Comentario

db = SessionLocal()

def avaliar_livro(usuario_id, livro_id, nota, texto=None):
    avaliacao = Avaliacao(usuario_id=usuario_id, livro_id=livro_id, nota=nota, comentario=texto)
    db.add(avaliacao)
    db.commit()
    print("✅ Avaliação registrada com sucesso!")

    if texto:
        comentario = Comentario(usuario_id=usuario_id, livro_id=livro_id, texto=texto)
        db.add(comentario)
        db.commit()
        print("💬 Comentário adicionado!")
