menu = """
+              MENU              +

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

+                                +
=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))
        if valor > 0:
            saldo += valor
            extrato += (f"Depósito: R$ {valor:.2f}\n")
            print("\nDepósito Realizado com sucesso!")
        else:
            print("Operação não Permitida! Valor inválido")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        if valor > saldo:
            print(f"Saldo insuficiente. Saldo Atual: R$ {saldo:.2f}")

        elif valor > limite:
            print(f"Limite não permitido para saque. Limite atual: R$ {limite}")

        elif numero_saques >= LIMITE_SAQUES:    
            print(f"Quantidade máxima de {LIMITE_SAQUES} Saques ultrapassadas.")

        elif valor > 0:
            saldo -= valor
            extrato += (f"Saque: R$ {valor:.2f}\n")
            numero_saques += 1
            print(f"\nSaque Realizado com sucesso! Saldo Atual: R${saldo:.2f}")
        
        else:
            print("Operação não permitida! Valor inválido.")

    elif opcao == "e":
        cabecalho = " EXTRATO "
        rodape = ""
        print(cabecalho.center(35, "="))
        print("Sem movimentações para o período" if not extrato else extrato)
        print(f"\nSaldo Atual: R$ {saldo:.2f}")
        print(rodape.center(35, "="))
        

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")