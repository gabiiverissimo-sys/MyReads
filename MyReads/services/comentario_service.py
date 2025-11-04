from database import SessionLocal
from models import Comentario, Livro, Usuario

db = SessionLocal()

def listar_comentarios_livro(livro_id):
    comentarios = db.query(Comentario).filter_by(livro_id=livro_id).all()
    if comentarios:
        print(f"\n💬 Comentários sobre o livro ID {livro_id}:")
        for c in comentarios:
            print(f"- {c.usuario.nome}: {c.texto}")
    else:
        print("Nenhum comentário para este livro.")

def listar_comentarios_usuario(usuario_id):
    comentarios = db.query(Comentario).filter_by(usuario_id=usuario_id).all()
    if comentarios:
        print(f"\n🗣️ Comentários feitos por este usuário:")
        for c in comentarios:
            print(f"- Livro: {c.livro.titulo} → {c.texto}")
    else:
        print("O usuário ainda não comentou nenhum livro.")

def excluir_comentario(comentario_id):
    comentario = db.query(Comentario).get(comentario_id)
    if comentario:
        db.delete(comentario)
        db.commit()
        print("🗑️ Comentário excluído com sucesso.")
    else:
        print("Comentário não encontrado.")
