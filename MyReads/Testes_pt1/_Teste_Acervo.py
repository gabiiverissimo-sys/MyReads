import re
from usuario import Usuario
from ListaLeitura import ListaLeitura
from LivrosBaseTestes import livros, get_livro_por_titulo

usuario = Usuario("gabs_bookshop", "gabi@gmail.com")

while True:
        print("\n--- Gerenciar Acervo ---")
        print("1. Adicionar livros à lista de desejos")
        print("2. Adicionar livros à lista de possuídos")
        print("3. Ver listas")

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
        else:
            print(" ▶ Opção inválida! Tente novamente.")
