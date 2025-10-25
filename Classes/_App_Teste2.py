import re
from usuario import Usuario
from ListaLeitura import ListaLeitura
from LivrosBaseTestes import livros, get_livro_por_titulo
from avaliacao import Avaliacao
from Comentario import Comentario
from ColecaoDeLivros import ColecaoDeLivros


# simulação de banco (não oficial)
usuarios_registrados = []

def cadastrar_usuario():
    print("\n--- Crie sua Conta ---")
    while True:
        nome = input("Digite o seu nome de usuário: ")
        email = input("Digite o seu e-mail: ")
        senha = input("Crie uma senha: ")

        try:
            novo_usuario = Usuario(nome, email, senha)
            usuarios_registrados.append(novo_usuario)
            print("\n ✏︎ Conta criada com sucesso!")
            print(novo_usuario)
            return novo_usuario
        except ValueError as erro:
            print(f"{erro}. Tente novamente.\n")

# Função para login
def fazer_login():
    print("\n--- Login ---")
    while True:
        nome_login = input("Usuário: ")
        senha_login = input("Senha: ")

        for u in usuarios_registrados:
            if u.nome == nome_login and u.verificar_senha(senha_login):
                print(f"\n ✏︎ Bem-vindo(a) de volta, {u.nome}!")
                return u
        print("Usuário ou senha incorretos. Tente novamente.\n")

# menu de início do app
usuario = None
while True:
    print("\n  Seja bem-vindo(a) ao MyReads! ")
    print("1. Criar nova conta")
    print("2. Fazer login")
    print("3. Sair")
    escolha_inicial = input("Escolha uma opção: ")

    if escolha_inicial == "1":
        usuario = cadastrar_usuario()
        break
    elif escolha_inicial == "2":
        if not usuarios_registrados:
            print("Nenhum usuário cadastrado ainda. Crie uma conta primeiro.\n")
        else:
            usuario = fazer_login()
            break
    elif escolha_inicial == "3":
        print("Encerrando o programa... Até logo!")
        exit()
    else:
        print("Opção inválida. Tente novamente.\n")

# -globals
avaliacoes_realizadas = []
comentarios_realizados = []

def gerenciar_listas(usuario):
    while True:
        print("\n--- Gerenciar Listas de Leitura ---")
        print("1. Criar ou editar lista")
        print("2. Ver todas as listas")
        print("3. Voltar")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            print("\nEscolha o nome da lista (ex: 'Quero ler', 'Lendo', 'Lido'):")
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

            entrada = input("\nDigite os números dos livros (separados por vírgula): ")
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
        print("2. Ver lista de desejos")
        print("3. Voltar")

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
                    print(f" Número {i+1} inválido, ignorado.")

        elif opcao == "2":
            usuario.acervo.listar_desejados()

        elif opcao == "3":
            print(" ▶ Voltando ao menu principal...")
            break
        else:
            print(" ▶ Opção inválida! Tente novamente.")


def avaliar_livro(usuario):
    global avaliacoes_realizadas, comentarios_realizados

    print("\n--- Avaliar Livro ---")
    titulo = input("Digite o título do livro que deseja avaliar: ")
    livro = get_livro_por_titulo(titulo)

    if not livro:
        print("Livro não encontrado.")
        return

    nota = input("✩ Dê uma nota de 0 a 5: ")
    if not nota.isdigit() or not (0 <= int(nota) <= 5):
        print("⚠ Digite apenas números entre 0 e 5.")
        return

    comentario_texto = input("✏︎ Digite um comentário (ou deixe em branco): ")

    avaliacao = Avaliacao(livro, int(nota), comentario_texto)
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
        print("\n=== Comentários dos usuários ===")
        for c in comentarios_realizados:
            print(c)

# Exemplo de polimorfismo
def demonstrar_polimorfismo():
    colecoes = [ColecaoDeLivros(), ListaLeitura("Favoritos")]
    print("\n--- 🌀 Demonstração de Polimorfismo ---")
    for c in colecoes:
        if hasattr(c, "nome"):
            print(f"→ {c.exibir_info() if hasattr(c, 'exibir_info') else f'Lista: {c.nome}'}")
        else:
            print("→ Coleção genérica de livros.")


# MENU PRINCIPAL
while True:
    print("\n~~~~ Menu Principal ~~~~")
    print("1. Gerenciar Listas de Leitura")
    print("2. Gerenciar Acervo")
    print("3. Avaliar Livro")
    print("4. Ver Avaliações e Comentários")
    print("5. Demonstrar Polimorfismo")
    print("6. Sair")

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
        demonstrar_polimorfismo()
    elif escolha == "6":
        print("\n Até logo! Obrigado por usar o MyReads!")
        break
    else:
        print(" Opção inválida, tente novamente.")
