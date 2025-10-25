import re
from usuario import Usuario
from ListaLeitura import ListaLeitura
from LivrosBaseTestes import livros, get_livro_por_titulo

usuario = Usuario("gabs_bookshop", "gabi@gmail.com")

while True:
        print("\n --- Gerenciar Listas de Leitura ---")
        print("1. Criar ou editar lista")
        print("2. Ver todas as listas")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            print("\nEscolha o nome da lista (ex: 'Quero ler', 'Lendo', 'Lido', 'Favoritos'):")
            nome_lista = input("→ ")

            if nome_lista not in usuario.listas:
                usuario.adicionar_lista(nome_lista, ListaLeitura(nome_lista))
                print(f"Lista '{nome_lista}' criada!")
            else:
                print(f"Editando lista existente: '{nome_lista}'")

            lista = usuario.listas[nome_lista]

            print("\nLivros disponíveis para adicionar:")
            for i, livro in enumerate(livros, 1):
                print(f"{i}. {livro.titulo} — {livro.autor}")

            print("\nDigite os números dos livros que deseja adicionar (separados por vírgula):")
            entrada = input("→ ")
            indices = [int(num.strip()) - 1 for num in entrada.split(",") if num.strip().isdigit()]

            for i in indices:
                if 0 <= i < len(livros):
                    livro_escolhido = livros[i]
                    lista.adicionar(livro_escolhido)
                    print(f"'{livro_escolhido.titulo}' adicionado à lista '{nome_lista}'.")
                else:
                    print(f"Número {i+1} inválido, ignorado.")

        elif opcao == "2":
            print("\n=== Listas do Usuário ===")
            usuario.listar_listas()
        else:
            print("Opção inválida! Tente novamente.")