def solicitar_senha():
    senha = input("Digite a senha: ")
    if senha == "jordaodocu":
        confirmacao = input("Confirme a senha: ")
        if confirmacao == "admin":
            print("Acesso permitido")
        else:
            print("Senha incorreta")
    else:
        print("Senha incorreta")

solicitar_senha()

