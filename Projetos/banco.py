saldo = 0
limite_saque = 3
print("".center(60, "-"))
operacao = input("[d]Depositar | [s]Sacar \n[e]Extrato | [q]Sair \n")
print("".center(60, "-"))

while operacao != "q":
    if operacao == "d":
        saldo += float(input("Informe o valor a ser depositado "))

    elif operacao == "e":
        print("Extrato".center(60, "-"))
        print(f"R$ {saldo}")
        print("".center(60, "-"))

    elif operacao == "s" and limite_saque > 0:
        saque = float(input("Informe o valor a ser sacado "))

        if saldo >= saque and saque <= 500:
            saldo -= saque
            limite_saque -= 1
        else:
            print("Não é possível sacar! \n")

    elif operacao == "s" and limite_saque == 0:
        print("Limite de saques atingido")

    print("".center(60, "-"))
    operacao = input("[d]Depositar | [s]Sacar \n[e]Extrato | [q]Sair \n")
    print("".center(60, "-"))
