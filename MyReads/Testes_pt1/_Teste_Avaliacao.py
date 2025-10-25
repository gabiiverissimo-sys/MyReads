from usuario import Usuario
from LivrosBaseTestes import get_livro_por_titulo
from avaliacao import Avaliacao
from Comentario import Comentario

usuario = Usuario("gabs_bookshop", "gabi@gmail.com")

avaliacoes_realizadas = []
comentarios_realizados = []

print("\n--- Avaliar Livro ---")

while True:

    titulo = input("Digite o título do livro que deseja avaliar (ou 'sair' para encerrar): ")

    if titulo.lower() == "sair":
        break

    livro = get_livro_por_titulo(titulo)

    if not livro:
        print(" Livro não encontrado. Tente novamente.")
        continue

    nota = input("☆ Dê uma nota de 0 a 5 (use vírgula ou ponto): ")
    comentario_texto = input("✏ Digite um comentário sobre o livro (ou deixe em branco): ")

    try:
        avaliacao = Avaliacao(livro, nota, comentario_texto)
        avaliacoes_realizadas.append(avaliacao)

        if comentario_texto.strip():
            comentario = Comentario(usuario, livro, comentario_texto)
            comentarios_realizados.append(comentario)

        print("\n Avaliação registrada com sucesso!")
        print(avaliacao)

    except ValueError as e:
        print(" Erro:", e)

# todas as avaliações feitas -
if not avaliacoes_realizadas:
    print("\n Nenhuma avaliação feita.")
else:
    print("\n===  Avaliações Realizadas ===")
    for a in avaliacoes_realizadas:
        print(f"- {a}")

    if comentarios_realizados:
        print("\n Comentários dos usuários:")
        for c in comentarios_realizados:
            print(c)

print("\n Fim das avaliações. Obrigado por usar o sistema!")
