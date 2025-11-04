from services.usuario_service import criar_usuario, autenticar, listar_usuarios
from services.livro_service import adicionar_livro, listar_livros, mudar_status
from services.avaliacao_service import avaliar_livro
from services.lista_service import criar_lista, adicionar_livro_na_lista, listar_listas_do_usuario
from services.acervo_service import add_possuido, add_desejado, listar_acervo



#terminal
print("\n📚 Seja bem-vindo(a) ao MyReads!")

usuario_logado = None

while True:
    if not usuario_logado:
        print("\n=== MENU INICIAL ===")
        print("1. Criar conta")
        print("2. Login")
        print("3. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome: ")
            email = input("Email: ")
            senha = input("Senha: ")
            criar_usuario(nome, email, senha)

        elif opcao == "2":
            email = input("Email: ")
            senha = input("Senha: ")
            usuario_logado = autenticar(email, senha)

        elif opcao == "3":
            print("Até logo! 👋")
            break
        else:
            print("Opção inválida.")
    else:
        print(f"\n✨ Olá, {usuario_logado.nome}! O que deseja fazer?")
        print("1. Gerenciar livros")
        print("2. Criar e gerenciar listas")
        print("3. Gerenciar acervo")
        print("4. Avaliar livro")
        print("5. Logout")
        escolha = input("→ ")

        if escolha == "1":
            print("\n1. Adicionar livro\n2. Listar livros\n3. Mudar status")
            op = input("→ ")

            if op == "1":
                titulo = input("Título: ")
                autor = input("Autor: ")
                genero = input("Gênero: ")
                ano = int(input("Ano: "))
                modelo = input("Modelo (Físico/Digital): ")
                adicionar_livro(titulo, autor, genero, ano, modelo)
            elif op == "2":
                listar_livros()
            elif op == "3":
                listar_livros()
                id_livro = int(input("Digite o ID do livro: "))
                novo_status = input("Novo status (Quero ler / Lendo / Lido / Desisti): ")
                mudar_status(id_livro, novo_status)

        elif escolha == "2":
            print("\n1. Criar lista\n2. Adicionar livro em lista\n3. Ver listas")
            op = input("→ ")
            if op == "1":
                nome_lista = input("Nome da lista: ")
                criar_lista(usuario_logado.id, nome_lista)
            elif op == "2":
                listar_livros()
                id_livro = int(input("ID do livro: "))
                listar_listas_do_usuario(usuario_logado.id)
                id_lista = int(input("ID da lista: "))
                adicionar_livro_na_lista(id_lista, id_livro)
            elif op == "3":
                listar_listas_do_usuario(usuario_logado.id)

        elif escolha == "3":
            print("\n1. Adicionar desejado\n2. Adicionar possuído\n3. Ver acervo")
            op = input("→ ")
            if op == "1":
                listar_livros()
                id_livro = int(input("ID do livro: "))
                add_desejado(usuario_logado.id, id_livro)
            elif op == "2":
                listar_livros()
                id_livro = int(input("ID do livro: "))
                add_possuido(usuario_logado.id, id_livro)
            elif op == "3":
                listar_acervo(usuario_logado.id)

        elif escolha == "4":
            listar_livros()
            livro_id = int(input("ID do livro: "))
            nota = float(input("Nota (0-5): "))
            comentario = input("Comentário (opcional): ")
            avaliar_livro(usuario_logado.id, livro_id, nota, comentario)

        elif escolha == "5":
            print("Saindo da conta...")
            usuario_logado = None
        else:
            print("Opção inválida.")
