usuario_teste = {
    "nome": "Leo",
    "nascimento": "10/03/2010",
    "cpf": "00079425612",
    "endereco": "Rua Bahia",
}

lista_usuarios = [usuario_teste]
contas = []


def criar_usuario(nome, nascimento, cpf, endereco):
    usuario = {"nome": nome, "nascimento": nascimento, "cpf": cpf, "endereco": endereco}
    for x in lista_usuarios:
        if x["cpf"] == usuario["cpf"]:
            validacao = False
            break
        else:
            validacao = True
    if validacao:
        lista_usuarios.append(usuario)
        print("Usuário Cadastrado")
    else:
        print("Não foi possível cadastrar, CPF já existente")


def criar_conta(contador):
    cpf = str(input("Informe o CPF "))
    agencia = ("0001",)

    for z in lista_usuarios:
        if z["cpf"] == cpf:
            validacao = True
            usuario_valido = z
            break
        else:
            validacao = False
    if validacao:
        print("Conta cadastrada ao usuário fornecido")
        contasi = {
            "agencia": agencia,
            "num_conta": contador,
            "usuario": usuario_valido["nome"],
            "cpf": cpf,
            "extrato": 0,
        }
        contas.append(contasi)
        return True
    else:
        print("Não é possivel criar conta, CPF inválido")
        return False


def verificar_usuario(cpf_usuario):
    for x in lista_usuarios:
        if x["cpf"] == cpf_usuario:
            verific_usuario = True
            break
        else:
            verific_usuario = False

    return verific_usuario


def verificar_conta(num_conta):
    if len(contas) == 0:
        verific_conta = False
    else:
        for x in contas:
            if x["num_conta"] == num_conta:
                verific_conta = True
                break
            else:
                verific_conta = False

    return verific_conta


def depositar(valor, cpf, conta):
    contador_interno = 0
    for x in contas:
        if (x["cpf"] == cpf) and (x["num_conta"] == conta):
            contas[contador_interno]["extrato"] += valor
        else:
            contador_interno += 1


def sacar(valor, cpf, conta):
    contador_interno = 0
    for x in contas:
        if (x["cpf"] == cpf) and (x["num_conta"] == conta):
            if (contas[contador_interno]["extrato"] >= valor) and valor > 0:
                contas[contador_interno]["extrato"] -= valor
                print("Sacado com sucesso")
            else:
                print("Não é possivel sacar, valor indisponível ")
        else:
            contador_interno += 1


def extrato(cpf, conta):
    contador_interno = 0
    for x in contas:
        if (x["cpf"] == cpf) and (x["num_conta"] == conta):
            print("R$", end=" ")
            print(contas[contador_interno]["extrato"])
        else:
            contador_interno += 1


def listar_contas(cpf):
    print(f"Contas Vinculadas ao cpf {cpf}:")
    for x in contas:
        if x["cpf"] == cpf:
            print(x)
    print("FIM!")


print(lista_usuarios)

print("".center(60, "-"))
texto = """
    OPERAÇÕES:

    [d]Depositar     | [s]Sacar
    [e]Extrato       | [u]Criar Usuário
    [c]Criar conta   | [l]Listar Contas
    [q]Sair
    """
print(texto)
operacao = input("Informe qual operação deseja ")
print("".center(60, "-"))

contador = 1

while operacao != "q":
    usuario, conta, vrfc1, vrfc2, cpf = None, None, None, None, None

    # --------------------------------------------------------------------------------------------------------------------
    if operacao == "d":
        usuario = str(input("Informe o CPF do usuario "))
        conta = int(input("Informe o número da conta "))
        vrfc1 = verificar_usuario(usuario)
        vrfc2 = verificar_conta(conta)

        if vrfc1 and vrfc2:
            valor = int(input("Informe o valor que deseja depositar "))
            depositar(valor, usuario, conta)
        else:
            print("Não é possivel depositar, CPF ou conta inválidos ")

    # --------------------------------------------------------------------------------------------------------------------
    elif operacao == "s":
        usuario = str(input("Informe o CPF do usuario "))
        conta = int(input("Informe o número da conta "))
        vrfc1 = verificar_usuario(usuario)
        vrfc2 = verificar_conta(conta)
        if vrfc1 and vrfc2:
            valor = int(input("Informe o valor que deseja sacar "))
            sacar(valor, usuario, conta)
        else:
            print("Não é possivel sacar, CPF ou conta inválidos")

    # --------------------------------------------------------------------------------------------------------------------
    elif operacao == "e":
        usuario = str(input("Informe o CPF do usuario "))
        conta = int(input("Informe o número da conta "))
        vrfc1 = verificar_usuario(usuario)
        vrfc2 = verificar_conta(conta)

        if vrfc1 and vrfc2:
            extrato(usuario, conta)
        else:
            print("Não é possivel mostrar extrato, CPF ou conta inválidos")

    # --------------------------------------------------------------------------------------------------------------------

    elif operacao == "u":
        nome = str(input("Informe o nome do usuário "))  # nome
        nasc = str(input("Informe a data de nascimento "))  # nasc
        cpf = str(input("Informe o CPF do usuário "))  # cpf
        endereco = str(input("Informe o endereço do usuario "))  # endereco
        criar_usuario(nome, nasc, cpf, endereco)

    # --------------------------------------------------------------------------------------------------------------------

    elif operacao == "c":
        val = criar_conta(contador)
        if val:
            contador += 1

    elif operacao == "l":
        cpf = str(input("Informe o CPF do usuário que deseja ver as contas "))
        vrfc1 = verificar_usuario(cpf)

        if vrfc1:
            listar_contas(cpf)
        else:
            print("CPF inválido")

    print("".center(60, "-"))
    print(texto)
    operacao = input("Informe qual operação deseja ")
    print("".center(60, "-"))
