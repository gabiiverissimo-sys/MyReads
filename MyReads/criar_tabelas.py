from database import Base, engine
from models import Usuario, Livro, ListaLeitura, Acervo, Avaliacao, Comentario

print("Criando tabelas no banco de dados...")
Base.metadata.create_all(bind=engine)
print("Tabelas criadas com sucesso!")
