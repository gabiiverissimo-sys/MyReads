from sqlalchemy import Column, Integer, String, Float, ForeignKey, Text, Table
from sqlalchemy.orm import relationship
from database import Base


# tabelas auxiliares
livros_listas = Table(
    "livros_listas",
    Base.metadata,
    Column("lista_id", Integer, ForeignKey("listas.id"), primary_key=True),
    Column("livro_id", Integer, ForeignKey("livros.id"), primary_key=True)
)

livros_acervos = Table(
    "livros_acervos",
    Base.metadata,
    Column("acervo_id", Integer, ForeignKey("acervos.id"), primary_key=True),
    Column("livro_id", Integer, ForeignKey("livros.id"), primary_key=True),
    Column("tipo", String, nullable=False)  # "possuido" ou "desejado"
)

# modelos de dados
class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    senha = Column(String, nullable=False)

    # Relações
    listas = relationship("ListaLeitura", back_populates="usuario", cascade="all, delete-orphan")
    acervo = relationship("Acervo", uselist=False, back_populates="usuario", cascade="all, delete-orphan")
    avaliacoes = relationship("Avaliacao", back_populates="usuario", cascade="all, delete-orphan")
    comentarios = relationship("Comentario", back_populates="usuario", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Usuario(nome='{self.nome}', email='{self.email}')>"


class Livro(Base):
    __tablename__ = "livros"

    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String, nullable=False)
    autor = Column(String, nullable=False)
    genero = Column(String)
    ano = Column(Integer)
    modelo = Column(String)  # físico ou digital
    isbn = Column(String, unique=True)
    nota_media = Column(Float, default=0)

    # Relações
    avaliacoes = relationship("Avaliacao", back_populates="livro", cascade="all, delete-orphan")
    comentarios = relationship("Comentario", back_populates="livro", cascade="all, delete-orphan")
    listas = relationship("ListaLeitura", secondary=livros_listas, back_populates="livros")
    acervos = relationship("Acervo", secondary=livros_acervos, back_populates="livros")

    def __repr__(self):
        return f"<Livro(titulo='{self.titulo}', autor='{self.autor}')>"


class ListaLeitura(Base):
    __tablename__ = "listas"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)

    usuario_id = Column(Integer, ForeignKey("usuarios.id"))
    usuario = relationship("Usuario", back_populates="listas")

    livros = relationship("Livro", secondary=livros_listas, back_populates="listas")

    def __repr__(self):
        return f"<ListaLeitura(nome='{self.nome}')>"


class Acervo(Base):
    __tablename__ = "acervos"

    id = Column(Integer, primary_key=True, index=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"))

    usuario = relationship("Usuario", back_populates="acervo")
    livros = relationship("Livro", secondary=livros_acervos, back_populates="acervos")

    def __repr__(self):
        return f"<Acervo(usuario='{self.usuario.nome}')>"


class Avaliacao(Base):
    __tablename__ = "avaliacoes"

    id = Column(Integer, primary_key=True, index=True)
    nota = Column(Float, nullable=False)
    comentario = Column(Text)

    usuario_id = Column(Integer, ForeignKey("usuarios.id"))
    livro_id = Column(Integer, ForeignKey("livros.id"))

    usuario = relationship("Usuario", back_populates="avaliacoes")
    livro = relationship("Livro", back_populates="avaliacoes")

    def __repr__(self):
        return f"<Avaliacao(livro='{self.livro.titulo}', nota={self.nota})>"


class Comentario(Base):
    __tablename__ = "comentarios"

    id = Column(Integer, primary_key=True, index=True)
    texto = Column(Text, nullable=False)

    usuario_id = Column(Integer, ForeignKey("usuarios.id"))
    livro_id = Column(Integer, ForeignKey("livros.id"))

    usuario = relationship("Usuario", back_populates="comentarios")
    livro = relationship("Livro", back_populates="comentarios")

    def __repr__(self):
        return f"<Comentario(usuario='{self.usuario.nome}', livro='{self.livro.titulo}')>"
