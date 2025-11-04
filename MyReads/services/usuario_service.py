from database import SessionLocal
from models import Usuario

db = SessionLocal()

def criar_usuario(nome, email, senha):
    usuario = Usuario(nome=nome, email=email, senha=senha)
    db.add(usuario)
    db.commit()
    db.refresh(usuario)
    print(f" Usuário {nome} criado com sucesso!")

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
        print("Usuário ou senha incorretos.")
