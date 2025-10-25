from usuario import Usuario
from ListaLeitura import ListaLeitura
from LivrosBaseTestes import livros
from avaliacao import Avaliacao
from Comentario import Comentario

def exibir_menu():
    print("\n===== MENU PRINCIPAL =====")
    print("1 - Criar uma lista de leitura")
    print("2 - Adicionar livro à lista")
    print("3 - Avaliar um livro")
    print("4 - Comentar sobre um livro")
    print("5 - Adicionar livro ao acervo")
    print("6 - Mostrar acervo e listas")
    print("0 - Sair")
    return input("Escolha uma opção: ")

def main():
    print("===== SISTEMA DE LEITURA - DEMONSTRAÇÃO ORIENTADA A OBJETOS =====\n")

    # 1. Criação do usuário
    nome = input("Digite seu user: ")
    email = input("Digite seu e-mail: ")
    try:
        usuario = Usuario(nome, email)
    except ValueError as e:
        print("❌ Erro:", e)
        return

    print(f"\n✅ Usuário criado com sucesso: {usuario.nome} ({usuario.email})")

    listas = {}
    while True:
        opcao = exibir_menu()

        if opcao == "1":
            nome_lista = input("\nDigite o nome da nova lista: ")
            lista = ListaLeitura(nome_lista)
            usuario.adicionar_lista(nome_lista, lista)
            listas[nome_lista] = lista
            print(f"✔ Lista '{nome_lista}' criada com sucesso!")

        elif opcao == "2":
            if not listas:
                print("⚠ Crie uma lista primeiro!")
                continue

            print("\nListas disponíveis:")
            for nome in listas:
                print(f" - {nome}")
            nome_lista = input("Escolha uma lista: ")

            if nome_lista not in listas:
                print("❌ Lista não encontrada.")
                continue

            print("\nLivros disponíveis:")
            for i, livro in enumerate(livros, 1):
                print(f"{i}. {livro.titulo} ({livro.autor})")

            entrada = input("Digite o(s) número(s) do(s) livro(s) que deseja adicionar (separe por vírgula): ")

            numeros = [n.strip() for n in entrada.split(",")]

            adicionados = []
            invalidos = []

            for n in numeros:
                if n.isdigit():
                    indice = int(n)
                if 1 <= indice <= len(livros):
                    listas[nome_lista].adicionar(livros[indice - 1])
                    adicionados.append(livros[indice - 1].titulo)
                else:
                    invalidos.append(n)
                
    else:
                    invalidos.append(n)

# feedback amigável
                if adicionados:
                    print(f"✔ Livros adicionados à lista '{nome_lista}': {', '.join(adicionados)}")
                if invalidos:
                    print(f"⚠ Números inválidos ignorados: {', '.join(invalidos)}")


        elif opcao == "3":
            print("\nEscolha um livro para avaliar:")
            for i, livro in enumerate(livros, 1):
                print(f"{i}. {livro.titulo}")
            escolha = int(input("Número do livro: "))
            if 1 <= escolha <= len(livros):
                nota = input("Digite uma nota de 0 a 5: ")
                comentario = input("Escreva um breve comentário: ")
                avaliacao = Avaliacao(livros[escolha - 1], nota, comentario)
                print("\n💬 Avaliação registrada:", avaliacao)
            else:
                print("❌ Livro inválido.")

        elif opcao == "4":
            titulo = input("\nDigite o título do livro para comentar: ")
            encontrados = [l for l in livros if titulo.lower() in l.titulo.lower()]
            if not encontrados:
                print("Livro não encontrado.")
                continue
            comentario_texto = input("Digite seu comentário: ")
            comentario = Comentario(usuario, encontrados[0], comentario_texto)
            print("💭 Comentário registrado com sucesso!")
            print(comentario)

        elif opcao == "5":
            print("\n1 - Adicionar livro possuído")
            print("2 - Adicionar livro desejado")
            tipo = input("Escolha: ")

            for i, livro in enumerate(livros, 1):
                print(f"{i}. {livro.titulo}")

            escolha = int(input("Número do livro: "))
            if 1 <= escolha <= len(livros):
                livro_escolhido = livros[escolha - 1]
                if tipo == "1":
                    usuario.acervo.add_possuido(livro_escolhido)
                elif tipo == "2":
                    usuario.acervo.add_desejado(livro_escolhido)
                else:
                    print("❌ Opção inválida.")
            else:
                print("❌ Número inválido.")

        elif opcao == "6":
            print("\n📚 Suas Listas de Leitura:")
            usuario.listar_listas()
            usuario.acervo.listar_possuidos()
            usuario.acervo.listar_desejados()

        elif opcao == "0":
            print("\n👋 Encerrando o programa. Até a próxima!")
            break
        else:
            print("❌ Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
