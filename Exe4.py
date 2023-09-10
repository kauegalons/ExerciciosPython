# Banco de usuários global
banco_usuarios = {}

def cadastrar_usuario(campos_obrigatorios):
    usuario = {}

    # Preenchendo campos obrigatórios
    for campo in campos_obrigatorios:
        valor = input(f"Digite o valor para {campo}: ")
        usuario[campo] = valor

    # Permitindo que o usuário adicione mais campos
    while True:
        novo_campo = input("Digite o nome de um novo campo (ou 'sair' para finalizar): ")

        if novo_campo.lower() == "sair":
            break

        valor = input(f"Digite o valor para {novo_campo}: ")
        usuario[novo_campo] = valor

    # Adicionando usuário ao banco global
    chave = len(banco_usuarios) + 1  # Para simplificar, estou usando uma sequência numérica como chave
    banco_usuarios[chave] = usuario

    return usuario

def imprimir_usuarios(*args, **kwargs):
    if not args and not kwargs:
        # Imprimir todos os usuários
        for chave, usuario in banco_usuarios.items():
            print(f"Usuário {chave}: {usuario}")
    elif args and not kwargs:
        # Filtrar por nomes
        for nome in args:
            for usuario in banco_usuarios.values():
                if usuario.get("nome") == nome:
                    print(usuario)
    elif not args and kwargs:
        # Filtrar por campos
        for usuario in banco_usuarios.values():
            match = True
            for campo, valor in kwargs.items():
                if usuario.get(campo) != valor:
                    match = False
                    break
            if match:
                print(usuario)
    else:
        # Filtrar por nomes e campos
        for nome in args:
            for usuario in banco_usuarios.values():
                if usuario.get("nome") == nome:
                    match = True
                    for campo, valor in kwargs.items():
                        if usuario.get(campo) != valor:
                            match = False
                            break
                    if match:
                        print(usuario)

# Solicitando campos obrigatórios do usuário
campos_obrigatorios = input("Digite os nomes dos campos obrigatórios, separados por vírgula: ").split(",")

while True:
    opcao = input("\n1-Cadastrar Usuario\n2-Imprimir Usuario\n0-Encerrar")

    if opcao == "1":
        cadastrar_usuario(campos_obrigatorios)
    elif opcao == "2":
        opcao_imprimir = input("1 - Imprimir todos\n2 - Filtrar por nomes\n3 - Filtrar por campos\n4 - Filtrar por nomes e campos\n")
        if opcao_imprimir == "1":
            imprimir_usuarios()
        elif opcao_imprimir == "2":
            nomes = input("Digite os nomes, separados por vírgula: ").split(",")
            imprimir_usuarios(*nomes)
        elif opcao_imprimir == "3":
            campos = {}
            while True:
                campo = input("Digite o nome do campo (ou 'sair' para finalizar): ")
                if campo.lower() == "sair":
                    break
                valor = input(f"Digite o valor para o campo {campo}: ")
                campos[campo] = valor
            imprimir_usuarios(**campos)
        else:
            nomes = input("Digite os nomes, separados por vírgula: ").split(",")
            campos = {}
            while True:
                campo = input("Digite o nome do campo (ou 'sair' para finalizar): ")
                if campo.lower() == "sair":
                    break
                valor = input(f"Digite o valor para o campo {campo}: ")
                campos[campo] = valor
            imprimir_usuarios(*nomes, **campos)
    elif opcao == "0":
        break