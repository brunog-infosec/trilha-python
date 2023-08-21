import textwrap

def menu():

    menu = """
    ============================== MENU ==============================

    [nu]\tNovo usuário
    [nc]\tNova conta corrente
    [lc]\tListar Contas existentes\n
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [q]\tSair

    ==================================================================
    => """
    return input(textwrap.dedent(menu))

def criar_usuario(lista_usuarios):

    cpf = input("Digite o seu CPF (Somente números): ")
    verificar = filtrar_usuarios(cpf, lista_usuarios)
    
    if verificar:
        print("Usuário já existe com esse CPF!\n")
        return
    
    nome = input("Digite o seu Nome: ")
    data_nascimento = input("Digite sua Data de Nascimento (dd-mm-aaaa): ")
    endereco = input("Digite o seu endereço no formato (Logradouro, Nº - bairro - cidade / sigla estado): ")

    lista_usuarios.append({'nome': nome, 'data_nascimento': data_nascimento, 'cpf': cpf, 'endereco': endereco}) 

    print("\nUsuário Registrado.")

def filtrar_usuarios(cpf,usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario['cpf'] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, lista_usuarios):

    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuarios(cpf, lista_usuarios)
    if usuario:
        print("Conta Criada com sucesso!")
        return {'agencia': agencia, 'numero_conta': numero_conta, 'usuario': usuario}
    else:
        print("\nUsuário não encontrado! Impossivel criar conta.\n")
        return None

def listar(contas):
     
    for conta in contas:
        linha = f"""\
            Agencia:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Tiitular:\t{conta['usuario']['nome']}
        """
        print('=' * 100)
        print(textwrap.dedent(linha))

def saque(*,saldo, valor, extrato, limite, numero_saques, limite_saques):

    if valor > saldo:
            print(f"Saldo insuficiente. Saldo Atual: R$ {saldo:.2f}")
    elif valor > limite:
        print(f"Limite não permitido para saque. Limite atual: R$ {limite}")
    elif numero_saques >= limite_saques:    
        print(f"Quantidade máxima de {limite_saques} Saques ultrapassadas.")
    elif valor > 0:
        saldo -= valor
        extrato += (f"Saque: R$ {valor:.2f}\n")
        numero_saques += 1
        print(f"\nSaque Realizado com sucesso! Saldo Atual: R${saldo:.2f}")
    else:
        print("Operação não permitida! Valor inválido.") 

    return saldo, extrato

def depositar(saldo, valor, extrato,/):     
    
    if valor > 0:
        saldo += valor
        extrato += (f"Depósito: R$ {valor:.2f}\n")
        print("\nDepósito Realizado com sucesso!")
    else:
        print("Operação não Permitida! Valor inválido")

    return saldo, extrato
    

def exibir_extrato(saldo,/,*,extrato):
    print("=======================================================")
    print("Sem movimentações para o período" if not extrato else extrato)
    print(f"\nSaldo Atual: R$ {saldo:.2f}")
    print("=======================================================")

def main():

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    lista_usuarios = []
    contas = []

    
    LIMITE_SAQUES = 3
    AGENCIA = '0001'

    while True:

        opcao = menu()

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))
            saldo, extrato = depositar(saldo, valor,extrato)


        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))
            saldo, extrato = saque(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES)

        elif opcao == "e":
            exibir_extrato(saldo,extrato=extrato)
            
        elif opcao == "q":
            break
        
        elif opcao == "nu": 
            criar_usuario(lista_usuarios)

        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, lista_usuarios)

            if conta:
                contas.append(conta)
        
        elif opcao == "lc":  
            listar(contas)


        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

main()