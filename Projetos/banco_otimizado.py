"""Sistema que replica o funcionamento de um sistema de banco com funções """

# Criando um usuário já cadastrado no sistema
usuario_teste = {
    "nome": "Leona",
    "nascimento": "10/03/2010",
    "cpf": "63879425612",
    "endereco": "Rua Bahia",
}
# Cadastrando o usuário na lista e inicializando a lista de contas vinculadas
lista_usuarios = [usuario_teste]
contas = []

# FUNÇÕES DE CADASTRO


def criar_usuario(nome, nascimento, cpf, endereco):
    """
    Cria um usuário se o CPF já nao estiver cadastrado na "lista_usuarios"
    Não retorna nada
    """
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
    """
    Cria contas vinculadas a um usuário/CPF existente no sistema,
    as contas de cada usuário são numeradas de forma crescente.
    Caso um usuário seja cadastro retorna TRUE senao retorna FALSE.
    """
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
            "saldo": 0,
        }
        contas.append(contasi)
        return True
    else:
        print("Não é possivel criar conta, CPF inválido")
        return False


# FUNÇÕES DE VERIFICAÇÃO


#
def verificar_usuario(cpf_usuario):
    """
    Verifica e retorna se o usuário esta cadastrado,
    passa pela lista de usuarios verificando se o CPF esta presente,
    retorna True caso seja encontrado o cpf e retorna False caso não
    """
    for x in lista_usuarios:
        if x["cpf"] == cpf_usuario:
            verific_usuario = True
            break
        else:
            verific_usuario = False

    return verific_usuario


def verificar_conta(num_conta, cpf):
    """
    Verifica e retorna se o usuário esta cadastrado,
    caso o número de conta e cpf estejam errados retorna False.
    """
    if len(contas) == 0:
        verific_conta = False
    else:
        for x in contas:
            if (x["num_conta"] == num_conta) and (x["cpf"] == cpf):
                verific_conta = True
                break
            else:
                verific_conta = False

    return verific_conta


# FUNÇÕES DE OPERAÇÕES


# Função que
def depositar(valor, cpf, conta):
    """
    Passa pela lista de contas e assim que o CPF e Nº de conta corresponder
    ao desejado, adiciona o valor ao saldo.

    """
    contador_interno = 0
    for x in contas:
        if (x["cpf"] == cpf) and (x["num_conta"] == conta):
            contas[contador_interno]["saldo"] += valor
            print(f"Valor de R${valor} depositado")
        else:
            contador_interno += 1


def sacar(valor, cpf, conta):
    """
    Passa pela lista de contas e assim que o CPF e Nº de conta corresponder
    ao desejado, assim que encontrado verifica se o valor é positivo e
    se a saldo suficiente para retirar o valor, caso tudo seja positivo retira
    o valor correspondente do saldo da conta especificada.
    """
    contador_interno = 0
    for x in contas:
        if (x["cpf"] == cpf) and (x["num_conta"] == conta):
            if (contas[contador_interno]["saldo"] >= valor) and valor > 0:
                contas[contador_interno]["saldo"] -= valor
                print("Sacado com sucesso")
            else:
                print("Não é possivel sacar, valor indisponível ")
        else:
            contador_interno += 1


def extrato(cpf, conta):
    """
    Passa pela lista de contas e assim que o CPF e Nº de conta corresponder
    ao desejado, mostra o quando de saldo há na conta.
    """
    contador_interno = 0
    for x in contas:
        if (x["cpf"] == cpf) and (x["num_conta"] == conta):
            print("R$", end=" ")
            print(contas[contador_interno]["saldo"])
        else:
            contador_interno += 1


def listar_contas(cpf):
    """
    Passa pela lista de contas e todo cpf que corresponde ao informado
    é printado.
    """
    print(f"Contas Vinculadas ao cpf {cpf}:")
    for x in contas:
        if x["cpf"] == cpf:
            print(x)
    print("FIM!")


# INICIALIZANDO MENU

print("".center(60, "-"))
texto = """
    OPERAÇÕES:

    [d]Depositar     | [s]Sacar
    [e]Extrato       | [u]Criar Usuário
    [c]Criar conta   | [l]Listar Contas/Informações
    [q]Sair
    """
print(texto)
operacao = input("Informe qual operação deseja ").lower().lower()
print("".center(60, "-"))

contador = 1  # Iniciando o contador que númera as contas de forma crescente

# Loop que repete sempre que a opção escolhida não corresponda a SAIR
while operacao != "q":

    usuario, conta, vrfc1, vrfc2, cpf = None, None, None, None, None

    # --------------------------------------------------------------------------------------------------------------------
    # OPERAÇÃO DEPOSITAR

    if operacao == "d":
        usuario = str(input("Informe o CPF do usuario "))
        conta = int(input("Informe o número da conta "))
        vrfc1 = verificar_usuario(usuario)
        vrfc2 = verificar_conta(conta, usuario)

        if vrfc1 and vrfc2:
            valor = int(input("Informe o valor que deseja depositar "))
            depositar(valor, usuario, conta)
        else:
            print("Não é possivel depositar, CPF ou conta inválidos ")

    # --------------------------------------------------------------------------------------------------------------------
    # OPERAÇÃO SACAR

    elif operacao == "s":
        usuario = str(input("Informe o CPF do usuario "))
        conta = int(input("Informe o número da conta "))
        vrfc1 = verificar_usuario(usuario)
        vrfc2 = verificar_conta(conta, usuario)
        if vrfc1 and vrfc2:
            valor = int(input("Informe o valor que deseja sacar "))
            sacar(valor, usuario, conta)
        else:
            print("Não é possivel sacar, CPF ou conta inválidos")

    # --------------------------------------------------------------------------------------------------------------------
    # OPERAÇÃO EXTRATO

    elif operacao == "e":
        usuario = str(input("Informe o CPF do usuario "))
        conta = int(input("Informe o número da conta "))
        vrfc1 = verificar_usuario(usuario)
        vrfc2 = verificar_conta(conta, usuario)

        if vrfc1 and vrfc2:
            extrato(usuario, conta)
        else:
            print("Não é possivel mostrar extrato, CPF ou conta inválidos")

    # --------------------------------------------------------------------------------------------------------------------
    # OPERAÇÃO CRIAR USUÁRIO

    elif operacao == "u":
        nome_externo = str(input("Informe o nome do usuário "))  # nome
        nasc = str(input("Informe a data de nascimento "))  # nasc
        cpf = str(input("Informe o CPF do usuário "))  # cpf
        endereco = str(input("Informe o endereço do usuario "))  # endereco
        criar_usuario(nome_externo, nasc, cpf, endereco)

    # --------------------------------------------------------------------------------------------------------------------
    # OPERAÇÃO CRIAR CONTA

    elif operacao == "c":
        val = criar_conta(contador)
        if val:
            contador += 1

    # --------------------------------------------------------------------------------------------------------------------
    # OPERAÇÃO LISTAR CONTAS E INFORMAÇÕES

    elif operacao == "l":
        cpf = str(input("Informe o CPF do usuário que deseja ver as contas "))
        vrfc1 = verificar_usuario(cpf)

        if vrfc1:
            listar_contas(cpf)
        else:
            print("CPF inválido")

    # --------------------------------------------------------------------------------------------------------------------
    # Parte que possibilita a saída do looping caso escolha a opção de SAIR[q]

    print("".center(60, "-"))
    print(texto)
    operacao = input("Informe qual operação deseja ").lower()
    print("".center(60, "-"))
