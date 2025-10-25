from usuario import Usuario
import re 

print("\n --- Crie sua conta ---")

while True:
        nome = input("Digite o seu username: ")
        email = input("Digite o seu email: ")

        try:
            usuario = Usuario(nome, email)
            print("\n Usuário cadastrado com sucesso!")
            print(usuario)
            break  
        except ValueError as erro:
            print(f"{erro}. Tente novamente.\n")  