from database import SessionLocal
from models import Usuario

db = SessionLocal()

def criar_usuario(nome, email, senha):
    # verifica se o email já está cadastrado
    usuario_existente = db.query(Usuario).filter_by(email=email).first()
    if usuario_existente:
        print(" Este email já está cadastrado. Tente outro.")
        return None

    # cria o novo usuário
    usuario = Usuario(nome=nome, email=email, senha=senha)
    db.add(usuario)
    db.commit()
    db.refresh(usuario)
    print(f" Usuário {nome} criado com sucesso!")
    return usuario


def listar_usuarios():
    usuarios = db.query(Usuario).all()
    for u in usuarios:
        print(f"- {u.nome} ({u.email})")


def autenticar(email, senha):
    usuario = db.query(Usuario).filter_by(email=email, senha=senha).first()
    if usuario:
        print(f" Login de {usuario.nome} realizado com sucesso.")
        return usuario
    else:
        print(" Usuário ou senha incorretos.")
        return None
