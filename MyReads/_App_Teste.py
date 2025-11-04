import re
from usuario import Usuario
from ListaLeitura import ListaLeitura
from LivrosBaseTestes import livros, get_livro_por_titulo
from avaliacao import Avaliacao
from Comentario import Comentario

print("\n Seja bem-vindo(a) ao MyReads! ")

# correção globals 
avaliacoes_realizadas = []
comentarios_realizados = []

# cadastro
print("\n--- Crie sua conta ---")
while True:
    nome = input("Digite o seu username: ")
    email = input("Digite o seu email: ")
    senha = input("Crie uma senha: ")

    try:
        usuario = Usuario(nome, email, senha) 
        print("\n Usuário cadastrado com sucesso!")
        print(usuario)
        break
    except ValueError as erro:
        print(f"{erro}. Tente novamente.\n")


# funções auxiliares
def gerenciar_listas(usuario):
    while True:
        print("\n--- Gerenciar Listas de Leitura ---")
        print("1. Criar ou editar lista")
        print("2. Ver todas as listas")
        print("3. Voltar")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            print("\nEscolha o nome da lista (ex: 'Quero ler', 'Lendo', 'Lido', 'Favoritos'):")
            nome_lista = input("→ ")

            if nome_lista not in usuario.listas:
                usuario.adicionar_lista(nome_lista, ListaLeitura(nome_lista))
                print(f"Lista '{nome_lista}' criada!")
            else:
                print(f" ✏ Editando lista existente: '{nome_lista}'")

            lista = usuario.listas[nome_lista]

            print("\n Livros disponíveis para adicionar:")
            for i, livro in enumerate(livros, 1):
                print(f"{i}. {livro.titulo} — {livro.autor}")

            print("\n Digite os números dos livros que deseja adicionar (separados por vírgula):")
            entrada = input("→ ")
            indices = [int(num.strip()) - 1 for num in entrada.split(",") if num.strip().isdigit()]

            for i in indices:
                if 0 <= i < len(livros):
                    livro_escolhido = livros[i]
                    lista.adicionar(livro_escolhido)
                    print(f" ☆ '{livro_escolhido.titulo}' adicionado à lista '{nome_lista}'.")
                else:
                    print(f"▶ Número {i+1} inválido, ignorado.")

        elif opcao == "2":
            print("\n ♡ Listas do Usuário ♡")
            usuario.listar_listas()
        elif opcao == "3":
            print("▶ Voltando ao menu principal...")
            break
        else:
            print("▶ Opção inválida! Tente novamente.")


def gerenciar_acervo(usuario):
    while True:
        print("\n--- Gerenciar Acervo ---")
        print("1. Adicionar livros à lista de desejos")
        print("2. Adicionar livros à lista de possuídos")
        print("3. Ver listas")
        print("4. Voltar")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            print("\nLivros disponíveis para adicionar na lista de desejos:")
            for i, livro in enumerate(livros, 1):
                print(f"{i}. {livro.titulo} — {livro.autor}")

            entrada = input("\nDigite os números dos livros (separados por vírgula): ")
            indices = [int(num.strip()) - 1 for num in entrada.split(",") if num.strip().isdigit()]

            for i in indices:
                if 0 <= i < len(livros):
                    livro_escolhido = livros[i]
                    usuario.acervo.add_desejado(livro_escolhido)
                else:
                    print(f"▶ Número {i+1} inválido, ignorado.")

        elif opcao == "2":
            print("\nLivros disponíveis para adicionar na lista de possídos:")
            for i, livro in enumerate(livros, 1):
                print(f"{i}. {livro.titulo} — {livro.autor}")

            entrada = input("\nDigite os números dos livros (separados por vírgula): ")
            indices = [int(num.strip()) - 1 for num in entrada.split(",") if num.strip().isdigit()]

            for i in indices:
                if 0 <= i < len(livros):
                    livro_escolhido = livros[i]
                    usuario.acervo.add_possuido(livro_escolhido)
                else:
                    print(f"▶ Número {i+1} inválido, ignorado.")

        elif opcao == "3":
            usuario.acervo.listar_desejados()
            usuario.acervo.listar_possuidos()
        elif opcao == "4":
            print("▶ Voltando ao menu principal...")
            break
        else:
            print("▶ Opção inválida! Tente novamente.")
        


def avaliar_livro(usuario):
    global avaliacoes_realizadas, comentarios_realizados  # <-- ADICIONE ISSO

    print("\n--- Avaliar Livro ---")
    titulo = input("Digite o título do livro que deseja avaliar: ")
    livro = get_livro_por_titulo(titulo)

    if not livro:
        print(" Livro não encontrado.")
        return

    nota = input("✏ Dê uma nota de 0 a 5: ").replace(",", ".")
    try:
        nota_float = float(nota)
        if not (0 <= nota_float <= 5):
            print("Digite apenas números entre 0 e 5.")
            return
    except ValueError:
        print("Entrada inválida. Digite um número entre 0 e 5.")

    comentario_texto = input("✏ Digite um comentário sobre o livro (ou deixe em branco): ")

    avaliacao = Avaliacao(livro, float(nota), comentario_texto)
    avaliacoes_realizadas.append(avaliacao)

    if comentario_texto.strip():
        comentario = Comentario(usuario, livro, comentario_texto)
        comentarios_realizados.append(comentario)

    print("\n♡ Avaliação registrada com sucesso!")
    print(avaliacao)


def ver_avaliacoes():
    global avaliacoes_realizadas, comentarios_realizados

    if not avaliacoes_realizadas:
        print("\n Nenhuma avaliação feita ainda.")
        return

    print("\n=== Avaliações Realizadas ===")
    for a in avaliacoes_realizadas:
        print(f"- {a}")

    if comentarios_realizados:
        print("\n ===Comentários dos usuários ===")
        for c in comentarios_realizados:
            print(c)
    if not avaliacoes_realizadas:
        print("\n Nenhuma avaliação feita ainda.")
        return


# menu
while True:
    print("\n=== Menu Principal ===")
    print("1. Gerenciar Listas de Leitura")
    print("2. Gerenciar Acervo")
    print("3. Avaliar Livro")
    print("4. Ver Avaliações e Comentários")
    print("5. Sair")

    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        gerenciar_listas(usuario)
    elif escolha == "2":
        gerenciar_acervo(usuario)
    elif escolha == "3":
        avaliar_livro(usuario)
    elif escolha == "4":
        ver_avaliacoes()
    elif escolha == "5":
        print("\n Até logo! Obrigado por usar o MyReads!")
        break
    else:
        print(" Opção inválida, tente novamente.")
