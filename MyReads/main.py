from services.usuario_service import criar_usuario, autenticar
from services.lista_service import criar_lista, adicionar_livro_na_lista, listar_listas_do_usuario
from services.acervo_service import add_possuido, add_desejado, listar_acervo
from services.avaliacao_service import avaliar_livro
from services.comentario_service import listar_comentarios_livro
from database import SessionLocal
from models import Livro
import re


# menus
def menu_inicial():
    print("\n=== MyReads ===")
    print("1. Criar conta")
    print("2. Fazer login")
    print("3. Sair")


def menu_principal(usuario):
    print(f"\n Bem-vindo(a) de volta, {usuario.nome}!")
    print("1. Catálogo de Livros")
    print("2. Listas de leitura")
    print("3. Acervo")
    print("4. Avaliar / Comentar")
    print("5. Ver comentários de um livro")
    print("6. Logout")


# buscas auxiliares
def buscar_livro_por_titulo_unico(titulo):
    db = SessionLocal()
    livro = db.query(Livro).filter(Livro.titulo.ilike(f"%{titulo}%")).first()
    db.close()
    return livro


def buscar_varios_livros(titulos):
    
    db = SessionLocal()
    livros_encontrados = []
    for t in [t.strip() for t in titulos.split(",") if t.strip()]:
        livro = db.query(Livro).filter(Livro.titulo.ilike(f"%{t}%")).first()
        if livro:
            livros_encontrados.append(livro)
        else:
            print(f" Livro '{t}' não encontrado no catálogo.")
    db.close()
    return livros_encontrados


def main():
    usuario_logado = None

    while True:
        if not usuario_logado:
            menu_inicial()
            opcao = input("→ ")

            if opcao == "1":
                nome = input("➤Nome: ")
                while True:
                    email = input("➤Email: ").strip()
                    if re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", email):
                        break
                    else:
                        print("Email inválido! Exemplo correto: nome@dominio.com")

                senha = input("➤Senha: ").strip()
                criar_usuario(nome, email, senha)

            elif opcao == "2":
                email = input("➤Email: ").strip()
                senha = input("➤Senha: ").strip()
                usuario_logado = autenticar(email, senha)

            elif opcao == "3":
                print("Encerrando o MyReads. Até logo!")
                break

            else:
                print("Opção inválida.")

        else:
            menu_principal(usuario_logado)
            escolha = input("→ ")

            # catalogo de livros
            if escolha == "1":
                while True:
                    print("\n ≡≡≡≡≡ Catálogo de Livros ≡≡≡≡≡")
                    print("1. Buscar livro por título")
                    print("2. Mudar status de leitura")
                    print("0. Voltar ao menu principal")
                    op = input("→ ")

                    if op == "1":
                        termo = input("♡ Digite parte do título do livro: ").strip()
                        db = SessionLocal()
                        resultados = db.query(Livro).filter(Livro.titulo.ilike(f"%{termo}%")).all()
                        if resultados:
                            print("\n Resultados encontrados:")
                            for l in resultados:
                                print(f"- {l.titulo} ({l.autor}, {l.ano})")
                        else:
                            print(" Nenhum livro encontrado.")
                        db.close()

                    elif op == "2":
                        titulo = input("♡ Digite o título do livro: ").strip()
                        livro = buscar_livro_por_titulo_unico(titulo)
                        if livro:
                            novo_status = input("Novo status (Quero ler / Lendo / Lido / Desisti): ")
                            from services.livro_service import mudar_status
                            mudar_status(livro.id, novo_status)
                        else:
                            print(" Livro não encontrado no catálogo.")

                    elif op == "0":
                        break
                    else:
                        print(" Opção inválida.")

            # listas de leitura
            elif escolha == "2":
                while True:
                    print("\n=== Listas de Leitura ===")
                    print("1. Criar lista")
                    print("2. Adicionar livro(s) em lista")
                    print("3. Ver listas do usuário")
                    print("0. Voltar ao menu principal")
                    op = input("→ ")

                    if op == "1":
                        nome_lista = input("Nome da lista: ")
                        criar_lista(usuario_logado.id, nome_lista)

                    elif op == "2":
                        titulos = input("♡ Digite os títulos (separados por vírgula): ")
                        livros = buscar_varios_livros(titulos)
                        if livros:
                            listar_listas_do_usuario(usuario_logado.id)
                            id_lista = int(input("ID da lista: "))
                            for livro in livros:
                                adicionar_livro_na_lista(id_lista, livro.id)
                            print(" ✩ Livros adicionados à lista com sucesso!")

                    elif op == "3":
                        print("\n✩ Suas listas:")
                        listar_listas_do_usuario(usuario_logado.id)

                    elif op == "0":
                        break
                    else:
                        print(" Opção inválida.")

            # acervo pessoal
            elif escolha == "3":
                while True:
                    print("\n=== Acervo Pessoal ===")
                    print("1. Adicionar livro(s) desejado(s)")
                    print("2. Adicionar livro(s) possuído(s)")
                    print("3. Ver acervo")
                    print("0. Voltar ao menu principal")
                    op = input("→ ")

                    if op == "1":
                        titulos = input("♡ Digite os títulos (separados por vírgula): ")
                        livros = buscar_varios_livros(titulos)
                        if livros:
                            for livro in livros:
                                add_desejado(usuario_logado.id, livro.id)
                            print("✩ Livros adicionados à lista de desejos!")
                    elif op == "2":
                        titulos = input("♡ Digite os títulos (separados por vírgula): ")
                        livros = buscar_varios_livros(titulos)
                        if livros:
                            for livro in livros:
                                add_possuido(usuario_logado.id, livro.id)
                            print(" ✩ Livros adicionados ao acervo de possuídos!")
                    elif op == "3":
                        listar_acervo(usuario_logado.id)
                    elif op == "0":
                        break
                    else:
                        print(" Opção inválida.")

            # avaliações e comentários
            elif escolha == "4":
                while True:
                    print("\n=== Avaliar / Comentar ===")
                    print("1. Avaliar livro")
                    print("2. Ver avaliações de um livro")
                    print("0. Voltar ao menu principal")
                    op = input("→ ")

                    if op == "1":
                        titulo = input("♡ Digite o título do livro: ").strip()
                        livro = buscar_livro_por_titulo_unico(titulo)
                        if not livro:
                            print(" Livro não encontrado no catálogo.")
                        else:
                             nota_input = input("✩ Nota: ").replace(",", ".").strip()
                        try:
                            nota = float(nota_input)
                            if 0 <= nota <= 5:
                                comentario = input("✎ Comentário: ").strip()
                                avaliar_livro(usuario_logado.id, livro.id, nota, comentario)
                            else:
                                print(" A nota deve estar entre 0 e 5.")
                        except ValueError:
                            print(" Valor de nota inválido.")

                    elif op == "2":
                        from services.avaliacao_service import listar_avaliacoes_livro
                        titulo = input("♡ Digite o título do livro: ").strip()
                        livro = buscar_livro_por_titulo_unico(titulo)
                        if livro:
                            listar_avaliacoes_livro(livro.id)
                        else:
                            print(" Livro não encontrado no catálogo.")

                    elif op == "0":
                        break
                    else:
                        print(" Opção inválida.")


            # comentários
            elif escolha == "5":
                while True:
                    print("\n=== Comentários ===")
                    print("1. Ver comentários de um livro")
                    print("0. Voltar ao menu principal")
                    op = input("→ ")

                    if op == "1":
                        titulo = input("♡ Digite o título do livro: ").strip()
                        livro = buscar_livro_por_titulo_unico(titulo)
                        if livro:
                            listar_comentarios_livro(livro.id)
                        else:
                            print(" Livro não encontrado no catálogo.")
                    elif op == "0":
                        break
                    else:
                        print(" Opção inválida.")

            # saída
            elif escolha == "6":
                print(f" Até logo, {usuario_logado.nome}!")
                usuario_logado = None
            else:
                print(" Opção inválida.")


if __name__ == "__main__":
    main()
