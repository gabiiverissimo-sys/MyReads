from database import SessionLocal
from models import Usuario, Acervo


def criar_usuario(nome, email, senha):
    db = SessionLocal()

    try:
        # verifica se o email já está cadastrado
        usuario_existente = db.query(Usuario).filter_by(email=email).first()
        if usuario_existente:
            print(" Este email já está cadastrado. Tente outro.")
            db.close()
            return None

        # cria o novo usuário
        usuario = Usuario(nome=nome, email=email, senha=senha)
        db.add(usuario)
        db.commit()
        db.refresh(usuario)

        # cria automaticamente o acervo do usuário
        acervo = Acervo(usuario_id=usuario.id)
        db.add(acervo)
        db.commit()

        print(f" Usuário {nome} criado com sucesso!")
        return usuario

    except Exception as e:
        print(f" Erro ao criar usuário: {e}")
        db.rollback()
        return None

    finally:
        db.close()


def listar_usuarios():
    db = SessionLocal()
    usuarios = db.query(Usuario).all()
    if usuarios:
        print("\n=== Usuários Cadastrados ===")
        for u in usuarios:
            print(f"- {u.nome} ({u.email})")
    else:
        print("Nenhum usuário encontrado.")
    db.close()


def autenticar(email, senha):
    db = SessionLocal()
    usuario = db.query(Usuario).filter_by(email=email, senha=senha).first()
    if usuario:
        print(f" Login de {usuario.nome} realizado com sucesso.")
        db.close()
        return usuario
    else:
        print(" Usuário ou senha incorretos.")
        db.close()
        return None
