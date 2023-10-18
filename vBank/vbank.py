##################################################################################################################
# MÓDULOS
##################################################################################################################

import random

##################################################################################################################
# PERSONALIZAÇÃO
##################################################################################################################

normal = "\033[0;0m"
vermelho = "\033[31m"
verde = "\033[32m"
azul = "\033[34m"
ciano = "\033[36m"
magenta = "\033[35m"
amarelo = "\033[33m"
preto = "\033[30m"
branco = "\033[37m"
negrito = "\033[1m"
reverso = "\033[2m"
fundo_preto = "\033[40m"
fundo_vermelho = "\033[41m"
fundo_verde = "\033[42m"
fundo_amarelo = "\033[43m"
fundo_azul = "\033[44m"
fundo_magenta = "\033[45m"
fundo_ciano = "\033[46m"
fundo_branco = "\033[47m"

##################################################################################################################
# LISTAS
##################################################################################################################

lista_principal_clientes=[]

##################################################################################################################
# CLASSES
##################################################################################################################

class tipo_cadastro:
    nome=""
    sobrenome=""
    cpf=0
    email=""
    endereco=""
    telefone=""
    vconta=0
    limite=0.0
    saldo=0.0

##################################################################################################################
# FUNÇÕES MÓDULO CLIENTE
##################################################################################################################

# Consultando existência de conta com mesmo número.
def gera_vconta_repete(vconta):
        cadastro_encontrado=0
        for i in range(len(lista_principal_clientes)):
            buscando=lista_principal_clientes[i].vconta
            if vconta==buscando:
                cadastro=i
                cadastro_encontrado=1
        if cadastro_encontrado == 1:
            return "0"
        if cadastro_encontrado == 0:
            return "1"

# Gerador de números para a nova conta.
def gera_vconta_numeros():
    vconta=0
    opera=1
    for i in range (6):
        novo=random.randint(1,9)
        add=opera*novo
        vconta+=add
        opera*=10
    return (vconta)

# Ao cadastrar uma nova conta, o programa gera o número da nova conta.
def gera_vconta():
    gerador="1"
    while gerador == "1":
        vconta=gera_vconta_numeros()
        final=gera_vconta_repete(vconta)
        if final == "0":
            gera_vconta()
        else:
            return vconta

# Finalizado o cadastro, exibir o cadastro completo.
def cadastrar_cliente_ver_cadastro():
    i=(len(lista_principal_clientes))-1
    print("\nNome:",lista_principal_clientes[i].nome,"\nSobrenome:",lista_principal_clientes[i].sobrenome,"\nCPF:",lista_principal_clientes[i].cpf,"\nE-mail:",lista_principal_clientes[i].email,"\nEndereço:",lista_principal_clientes[i].endereco,"\nTelefone:",lista_principal_clientes[i].telefone,"\nvConta:",lista_principal_clientes[i].vconta,"\nLimite autorizado: R$ {0:.2f}".format(lista_principal_clientes[i].limite),"\nSaldo: R$ {0:.2f}".format(lista_principal_clientes[i].saldo,"\n"))
    return "1"

# Tendo finalizado o procedimento de cadastro de novo cliente, o programa solicita exibição do cadastro completo ou retorno ao menu anterior.
def cadastrar_cliente_finalizar():
    opcao="1"
    while opcao != "0":
        print(reverso + "\n--------------------------------------------------\nSCGO vBank Gerente de Contas - Gerenciar Clientes - Cadastrar Cliente - Finalizar Cadastro\n--------------------------------------------------\n" + normal + "\n1 = Ver cadastro\n0 = Finalizar e retornar ao menu anterior\n")
        opcao=input("Informe a opção desejada: ")
        if opcao == "1":
            opcao=cadastrar_cliente_ver_cadastro()
        if opcao == "0":
            return 0
        if opcao != "1" and opcao != "2" and opcao != "3":
            print("Esta não é uma opção válida.")
            opcao="1"

# Após confirmar que o CPF informado para novo cadastro não consta em nenhum cadastro já existente, o programa verifica a validade do CPF informado.
def valida_cpf(eh_novo):
    cpf=eh_novo
    d2=cpf%10
    cpf=cpf//10
    d1=cpf%10
    cpf=cpf//10
    soma=0
    multiplicador=2
    for i in range (9):
        digito=cpf%10
        soma+=(digito*multiplicador)
        cpf=cpf//10
        multiplicador+=1
    testa_d1=soma%11
    if testa_d1 < 2:
        d1_valido=0
    else:
        d1_valido=11-testa_d1
    cpf=(eh_novo//10)
    multiplicador=2
    soma=0
    for i in range (10):
        digito=cpf%10
        soma+=(digito*multiplicador)
        cpf=cpf//10
        multiplicador+=1
    testa_d2=soma%11
    if testa_d2 < 2:
        d2_valido=0
    else:
        d2_valido=11-testa_d2
    if d1_valido == d1 and d2_valido == d2:
        print("O CPF informado é válido.")
        return "1"
    else:
        print("O CPF informado não é válido.")
        return "0"

# Para novo cadastro, após informar CPF, programa verifica se o CPF já consta em algum cadastro existente
def cadastrar_cliente_busca_existente(novo_cpf):
    cadastro_encontrado=0
    for i in range(len(lista_principal_clientes)):
        buscando=lista_principal_clientes[i].cpf
        if novo_cpf==buscando:
            cadastro=i
            cadastro_encontrado=1
    return cadastro_encontrado

# Cadastrar um novo cliente, no módulo de gerenciamento de clientes
def cadastrar_cliente():
    print(reverso + "\n--------------------------------------------------\nSCGO vBank Gerente de Contas - Gerenciar Clientes - Cadastrar Cliente\n--------------------------------------------------\n" + normal + "\nCadastro vBank")
    novo_cpf=int(input("Informe o CPF (apenas números) do/a novo/a cliente: "))
    eh_novo=cadastrar_cliente_busca_existente(novo_cpf)
    if eh_novo == 0:
        print("O CPF informando ainda não consta em nossos cadastros.")
        opcao=valida_cpf(novo_cpf)
        if opcao == "1":
            print("\nCadastro de Cliente:")
            novo_cliente=tipo_cadastro()
            novo_cliente.nome=input("Nome: ")
            novo_cliente.sobrenome=input("Sobrenome: ")
            novo_cliente.cpf=novo_cpf
            novo_cliente.email=input("E-mail: ")
            novo_cliente.endereco=input("Endereço: ")
            novo_cliente.telefone=input("Telefone: ")
            # novo_cliente.vconta=int(input("vConta: "))
            novo_cliente.vconta=gera_vconta()
            novo_cliente.limite=1000.00
            novo_cliente.saldo=0.00
            lista_principal_clientes.append(novo_cliente)
            print("\nCadastro realizado com sucesso.")
            cadastrar_cliente_finalizar()
            return "1"
        if opcao == "0":
            return "1"
    if eh_novo == 1:
        print("Já existe um cadastrao com o CPF informado.")
        return "1"

# Em encontrando o campo buscado, o programa possibilita exibição do cadastro completo
def consultar_cadastro_ver_completo(i):
    opcao="1"
    while opcao != "0":
        opcao=input("\nDeseja visualizar o cadastro completo (s/n)?")
        if opcao == "s":
            print("\nNome:",lista_principal_clientes[i].nome,"\nSobrenome:",lista_principal_clientes[i].sobrenome,"\nCPF:",lista_principal_clientes[i].cpf,"\nE-mail:",lista_principal_clientes[i].email,"\nEndereço:",lista_principal_clientes[i].endereco,"\nTelefone:",lista_principal_clientes[i].telefone,"\nvConta:",lista_principal_clientes[i].vconta,"\nLimite autorizado: R$ {0:.2f}".format(lista_principal_clientes[i].limite),"\nSaldo: R$ {0:.2f}".format(lista_principal_clientes[i].saldo))
            return "1"
        if opcao == "n":
            return "1"
        if opcao != "s" and opcao != "n":
            print("Esta não é uma opção válida.")
            opcao="1"

# Operação de consulta de cadastro, através do CPF
def consultar_cadastro_cpf():
        busca=int(input("Consultar CPF: "))
        cadastro_encontrado=0
        for i in range(len(lista_principal_clientes)):
            buscando=lista_principal_clientes[i].cpf
            if busca==buscando:
                cadastro=i
                cadastro_encontrado=1
        if cadastro_encontrado == 1:
            print("Este CPF já está cadastrado.\nNome do/a cliente: ",lista_principal_clientes[i].nome,lista_principal_clientes[i].sobrenome,"\n")
            return consultar_cadastro_ver_completo(i)
        if cadastro_encontrado == 0:
            print("Não foi encontrado nenhum cadastro com o CPF informado.")
            return "1"

# Operação de consulta de cadastro, através do nome
def consultar_cadastro_nome():
        busca=input("Consultar Nome: ")
        cadastro_encontrado=0
        for i in range(len(lista_principal_clientes)):
            buscando=lista_principal_clientes[i].nome
            if busca==buscando:
                cadastro=i
                cadastro_encontrado=1
        if cadastro_encontrado == 1:
            print("Este Nome já está cadastrado.\nNome do/a cliente: ",lista_principal_clientes[i].nome,lista_principal_clientes[i].sobrenome,"\n")
            return consultar_cadastro_ver_completo(i)
        if cadastro_encontrado == 0:
            print("Não foi encontrado nenhum cadastro com o nome informado.")
            return "1"

# Operação de consulta de cadastro, através do sobrenome
def consultar_cadastro_sobrenome():
        busca=input("Consultar Sobrenome: ")
        cadastro_encontrado=0
        for i in range(len(lista_principal_clientes)):
            buscando=lista_principal_clientes[i].sobrenome
            if busca==buscando:
                cadastro=i
                cadastro_encontrado=1
        if cadastro_encontrado == 1:
            print("Este Sobrenome já está cadastrado.\nNome do/a cliente: ",lista_principal_clientes[i].nome,lista_principal_clientes[i].sobrenome,"\n")
            return consultar_cadastro_ver_completo(i)
        if cadastro_encontrado == 0:
            print("Não foi encontrado nenhum cadastro com o sobrenome informado.")
            return "1"

# Operação de consulta de cadastro, através do número da conta
def consultar_cadastro_vconta():
        busca=int(input("Consultar vConta: "))
        cadastro_encontrado=0
        for i in range(len(lista_principal_clientes)):
            buscando=lista_principal_clientes[i].vconta
            if busca==buscando:
                cadastro=i
                cadastro_encontrado=1
        if cadastro_encontrado == 1:
            print("Esta vConta já está cadastrado.\nNome do/a cliente: ",lista_principal_clientes[i].nome,lista_principal_clientes[i].sobrenome,"\n")
            return consultar_cadastro_ver_completo(i)
        if cadastro_encontrado == 0:
            print("Não foi encontrado nenhum cadastro com a vConta informada.")
            return "1"

# Operação de consulta de cadastro, no módulo de gerenciamento de clientes
def consultar_cadastro ():
    opcao="1"
    while opcao != "0":
        print(reverso + "\n--------------------------------------------------\nSCGO vBank Gerente de Contas- Gerenciar Clientes - Consultar Cadastro\n--------------------------------------------------\n" + normal + "\nConsultar por:\n1 = CPF\n2 = Nome \n3 = Sobrenome\n4 = vConta\n0 = Retornar ao menu anterior\n")
        opcao=input("Informe a opção desejada: ")
        if opcao == "1":
            opcao=consultar_cadastro_cpf()
        if opcao == "2":
            opcao=consultar_cadastro_nome()
        if opcao == "3":
            opcao=consultar_cadastro_sobrenome()
        if opcao == "4":
            opcao=consultar_cadastro_vconta()
        if opcao == "0":
            return "1"
        if opcao != "1" and opcao != "2" and opcao != "3" and opcao != "4" and opcao != "0":
            print("Esta não é uma opção válida.")


# Confirmação de alteração de cadastro
def alterar_cadastro_confirmar_conta_buscada ():
    opcao=input("Deseja alterar esta conta (s/n)? ")
    if opcao == "s":
        return 1
    if opcao == "n":
        return 0
    if opcao != "s" and opcao != "n":
        print("Esta não é uma opção válida.")
        alterar_cadastro_confirmar_conta_buscada()

# Tendo informado o CPF, informa a titularidade, solicita confirmação de alteração da conta e solicita o campo a ser alterado
def alterar_cadastro_encontrado (cadastro):
    print("Titularidade da conta a ser alterada:",lista_principal_clientes[cadastro].nome,lista_principal_clientes[cadastro].sobrenome)
    confirma=alterar_cadastro_confirmar_conta_buscada()
    if confirma == 1:
        altera=input("Você pode realizar alterações cadastrais nos seguintes campos:\n1 = Nome\n2 = Sobrenome\n3 = Email\n4 = Endereço\n5 = Telefone\n0 = Cancelar atualização cadastral e retornar\nInforme a informação que deseja alterar: ")
        if altera == "1":
            novo=input("Infome o novo Nome: ")
            lista_principal_clientes[cadastro].nome=novo
            return cadastro
        if altera == "2":
            novo=input("Infome o novo Sobrenome: ")
            lista_principal_clientes[cadastro].sobrenome=novo
            return cadastro
        if altera == "3":
            novo=input("Infome o novo E-mail: ")
            lista_principal_clientes[cadastro].email=novo
            return cadastro
        if altera == "4":
            novo=input("Infome o novo Endereço: ")
            lista_principal_clientes[cadastro].endereco=novo
            return cadastro
        if altera == "5":
            novo=input("Infome o novo Telefone: ")
            lista_principal_clientes[cadastro].telefone=novo
            return cadastro
        if altera == "0":
            return -1

# Realizar alteração em cadastro existente, no módulo de gerenciamento de clientes
def alterar_cadastro ():
    print(reverso + "\n--------------------------------------------------\nSCGO vBank Gerente de Contas- Gerenciar Clientes - Alterar Cadastro\n--------------------------------------------------\n" + normal + "\nEsta opção permite realizar atualização cadastral. \nPara alterar um cadastro, é necessário o informar o CPF registrado.")
    busca=int(input("Informe o CPF do cadastro que deseja alterar: "))
    cadastro_encontrado=0
    for i in range(len(lista_principal_clientes)):
        buscando=lista_principal_clientes[i].cpf
        if busca==buscando:
            cadastro=i
            cadastro_encontrado=1
    if cadastro_encontrado == 1:
        alterar_cadastro_encontrado(cadastro)
        return cadastro
    else:
        opcao="1"
        while opcao!="0":
            opcao=input("O CPF informado não é um cliente vBank.\nDeseja realizar uma nova busca (s/n)?" )
            if opcao == "s":
                alterar_cadastro()
            if opcao == "n":
                return "1"
            if opcao != "s" and opcao != "n":
                print("Esta não é uma opção válida.")
                opcao="1"

# Ao solicitar uma exclusão de conta, tendo confirmado a titularidade, o programa solicita confirmação da operação
def excluir_cadastro_confirmar_conta_buscada ():
    opcao=input("Deseja realmente excluir esta conta (s/n)? ")
    if opcao == "s":
        return 1
    if opcao == "n":
        return 0
    if opcao != "s" and opcao != "n":
        print("Esta não é uma opção válida.")
        excluir_cadastro_confirmar_conta_buscada()

# Ao solicitar uma exclusão de conta, apresenta os dados da conta a ser excluída
def excluir_cadastro_encontrado(cadastro):
    print("Titularidade da conta a ser alterada:",lista_principal_clientes[cadastro].nome,lista_principal_clientes[cadastro].sobrenome)
    confirma=excluir_cadastro_confirmar_conta_buscada()
    if confirma == 1:
        lista_principal_clientes.pop(cadastro)
        print("Cadastro excluído com sucesso.")
        return "1"

# Realizar exclusão de um cadastro, no módulo de gerenciamento de clientes
def excluir_cadastro ():
    print(reverso + "\n--------------------------------------------------\nSCGO vBank Gerente de Contas- Gerenciar Clientes - Excluir Cadastro\n--------------------------------------------------\n" + normal +"\nEsta opção remove permanentemente um cadastro de cliente. \nPara excluir um cadastro, é necessário o informar o CPF registrado.")
    busca=int(input("Informe o CPF do cadastro que deseja excluir: "))
    cadastro_encontrado=0
    for i in range(len(lista_principal_clientes)):
        buscando=lista_principal_clientes[i].cpf
        if busca==buscando:
            cadastro=i
            cadastro_encontrado=1
    if cadastro_encontrado == 1:
        excluir_cadastro_encontrado(cadastro)
        return "1"
    if cadastro_encontrado == 0:
        opcao="1"
        while opcao!="0":
            opcao=input("O CPF informado não é um cliente vBank.\nDeseja realizar uma nova busca (s/n)?" )
            if opcao == "s":
                excluir_cadastro()
                return "1"
            if opcao == "n":
                return "1"
            if opcao != "s" and opcao != "n":
                print("Esta não é uma opção válida.")
                opcao="1"

##################################################################################################################
# OPERAÇÕES MÓDULO CONTA
##################################################################################################################

# Busca a conta através do cpf
def operar_conta_busca_conta_cpf():
    busca=int(input("Informe o CPF da conta:"))
    for i in range(len(lista_principal_clientes)):
        buscando=lista_principal_clientes[i].cpf
        if busca==buscando:
            return i
    return "1"

# Busca a conta através do número de conta
def operar_conta_busca_conta_vConta():
    busca=int(input("Informe o número da vConta:"))
    for i in range(len(lista_principal_clientes)):
        buscando=lista_principal_clientes[i].vconta
        if busca==buscando:
            return i
    return "1"

# Buscar conta para realizar operação de crédito ou de débito em conta corrente
def operar_conta_busca_conta():
    opcao="1"
    while opcao != "0":
        opcao=input(reverso + "\n--------------------------------------------------\nSCGO vBank Gerente de Contas- Gerenciar Conta Corrente - Débito\n--------------------------------------------------\n" + normal + "\nPara realizar uma operação, você precisa acessar a conta.\nPara acessar a conta desejada, escolha uma das opções:\n1 = CPF\n2 = vConta\n0 = Retornar ao menu anterior.\n\nInforme a opção desejada: ")
        if opcao == "1":
            opcao=operar_conta_busca_conta_cpf()
            if opcao == "1":
                print("O CPF informado não consta em nossos cadastros.")
                opcao="1"
            else:
                return opcao
        if opcao == "2":
            opcao=operar_conta_busca_conta_vConta()
            if opcao == "1":
                print("O número de vConta informado não consta em nossos cadastros.")
                opcao="1"
            else:
                return opcao
        if opcao == "0":
            return "1"
        if opcao != "1" and opcao != "2" and opcao != "0":
            print("Esta não é uma opção válida.")
            opcao="1"
    return "1"

# Realizar um débito em conta, no módulo de gerenciamento de conta correte
def debitar():
    conta_debitar=operar_conta_busca_conta()
    if conta_debitar == "1":
        return "1"
    if conta_debitar != "1":
        print("\nCliente vBank: ",lista_principal_clientes[conta_debitar].nome, lista_principal_clientes[conta_debitar].sobrenome, "\nSaldo da vConta: R$ {:.2f}".format(lista_principal_clientes[conta_debitar].saldo), "\nLimite autorizado: R$ ",lista_principal_clientes[conta_debitar].limite, "\nSaldo disponível: R$ {0:.2f}".format((lista_principal_clientes[conta_debitar].saldo)+(lista_principal_clientes[conta_debitar].limite)))
        valor_disponível=((lista_principal_clientes[conta_debitar].saldo)+(lista_principal_clientes[conta_debitar].limite))
        valor=float(input("\nInforme o valor a ser debitado: R$ "))
        if valor_disponível-valor >= 0:
            lista_principal_clientes[conta_debitar].saldo=((lista_principal_clientes[conta_debitar].saldo)-valor)
            print("\nOperação realizada com sucesso.\n\nCliente vBank: ",lista_principal_clientes[conta_debitar].nome, lista_principal_clientes[conta_debitar].sobrenome, "\nSaldo da vConta: R$ {:.2f}".format(lista_principal_clientes[conta_debitar].saldo), "\nLimite autorizado: R$ ",lista_principal_clientes[conta_debitar].limite, "\nSaldo disponível: R$ {0:.2f}".format((lista_principal_clientes[conta_debitar].saldo)+(lista_principal_clientes[conta_debitar].limite)))
        if valor_disponível-valor < 0:
            print("Esta conta não possui disponibilidade para esta operação.")
            debitar()

# Realizar um crédito em conta, no módulo de gerenciamento de conta correte
def creditar():
    conta_creditar=operar_conta_busca_conta()
    if conta_creditar == "1":
        return "1"
    if conta_creditar != "1":
        print("\nCliente vBank: ",lista_principal_clientes[conta_creditar].nome, lista_principal_clientes[conta_creditar].sobrenome, "\nSaldo da vConta: R$ {:.2f}".format(lista_principal_clientes[conta_creditar].saldo), "\nLimite autorizado: R$ ",lista_principal_clientes[conta_creditar].limite, "\nSaldo disponível: R$ {:.2f}".format(((lista_principal_clientes[conta_creditar].saldo)+(lista_principal_clientes[conta_creditar].limite))))
        valor_disponível=((lista_principal_clientes[conta_creditar].saldo)+(lista_principal_clientes[conta_creditar].limite))
        valor=float(input("\nInforme o valor a ser creditado: R$ "))
        lista_principal_clientes[conta_creditar].saldo=((lista_principal_clientes[conta_creditar].saldo)+valor)
        print("\nOperação realizada com sucesso.\n\nCliente vBank: ",lista_principal_clientes[conta_creditar].nome, lista_principal_clientes[conta_creditar].sobrenome, "\nSaldo da vConta: R$ {0:.2f}".format(lista_principal_clientes[conta_creditar].saldo), "\nLimite autorizado: R$ ",lista_principal_clientes[conta_creditar].limite, "\nSaldo disponível: R$ {0:.2f}".format((lista_principal_clientes[conta_creditar].saldo)+(lista_principal_clientes[conta_creditar].limite)))
        return "1"

##################################################################################################################
# FUNÇÕES DE NAVEGAÇÃO
#################################################################################################################

# Validar a saída do menu secundario Clientes e retorno ao menu principal do programa
def valida_saida_clientes():
    testando_saida="s"
    while testando_saida == "s":
        testando_saida=input("Deseja realmente retonar ao menu principal (s/n)? ")
        testando_saida.lower
        if testando_saida == "s":
            return "s"
        if testando_saida == "n":
            return "n"
        if testando_saida != "s" and testando_saida != "n":
            print("Esta não é uma opção válida.")
            testando_saida="s"

# Chama as funções secundárias da opção principal Clientes
def menu_secundario_clientes():
    opcao="1"
    while opcao != "0":
        print(reverso + "\n--------------------------------------------------\nSCGO vBank Gerente de Contas- Gerenciar Clientes\n--------------------------------------------------\n" + normal + "\n1 = Consultar cadastro\n2 = Cadastrar cliente\n3 = Alterar cadastro\n4 = Excluir cadastro\n0 = Voltar para o menu principal\n")
        opcao=input("Informe a opção desejada: ")
        if opcao == "1":
            opcao=consultar_cadastro()
        if opcao == "2":
            opcao=cadastrar_cliente()
        if opcao == "3":
            opcao=alterar_cadastro()
            if opcao == "1":
                opcao="1"
            else:
                i=input("Deseja verificar o cadastro alterado (s/n)?")
                if i == "s":
                    print("\nNome:",lista_principal_clientes[opcao].nome,"\nSobrenome:",lista_principal_clientes[opcao].sobrenome,"\nCPF:",lista_principal_clientes[opcao].cpf,"\nE-mail:",lista_principal_clientes[opcao].email,"\nEndereço:",lista_principal_clientes[opcao].endereco,"\nTelefone:",lista_principal_clientes[opcao].telefone,"\nvConta:",lista_principal_clientes[opcao].vconta,"\nLimite autorizado: R$ {0:.2f}".format(lista_principal_clientes[opcao].limite),"\nSaldo: R$ {0:.2f}".format(lista_principal_clientes[opcao].saldo))
                    opcao="1"
                else:
                    opcao="1"
        if opcao == "4":
            excluir_cadastro()
        if opcao == "0":
            retornar=valida_saida_clientes()
            if retornar == "s":
                return "s"
            if retornar == "n":
                opcao="1"
        if opcao != "1" and opcao != "2" and opcao != "3" and opcao != "4" and opcao != "0":
            print("Esta não é uma opção válida.")

# Validar a saída do menu secundario Conta Corrente e retorno ao menu principal do program
def valida_saida_conta():
    testando_saida="s"
    while testando_saida == "s":
        testando_saida=input("Deseja realmente retonar ao menu principal (s/n)? ")
        testando_saida.lower
        if testando_saida == "s":
            return "s"
        if testando_saida == "n":
            return "n"
        if testando_saida != "s" and testando_saida != "n":
            print("Esta não é uma opção válida.")
            testando_saida="s"

# Chama as funções secundárias da opção principal Conta Correte
def menu_secundario_conta():
    opcao="1"
    while opcao != "0":
        print(reverso + "\n--------------------------------------------------\nSCGO vBank Gerente de Contas- Gerenciar Conta Corrente\n--------------------------------------------------\n" + normal + "\n1 = Débito\n2 = Crédito\n0 = Voltar para o menu principal\n")
        opcao=input("Informe a opção desejada: ")
        if opcao == "1":
            debitar()
        if opcao == "2":
            creditar()
        if opcao == "0":
            retornar=valida_saida_conta()
            if retornar == "s":
                return "s"
            if retornar == "n":
                opcao="1"
        if opcao != "1" and opcao != "2" and opcao != "0":
            print("Esta não é uma opção válida.")

# Confirmação da ooção principal de sair do programa
def valida_saida_principal():
    testando_saida="s"
    while testando_saida == "s":
        testando_saida=input("Deseja realmente sair do SCGO vBank (s/n)? ")
        testando_saida.lower
        if testando_saida == "s":
            return "s"
        if testando_saida == "n":
            return "1"
        if testando_saida != "s" and testando_saida != "n":
            print("Esta não é uma opção válida.")
            testando_saida="s"

# Chama as funções principais do programa
def menu_principal():
    logado=1
    while logado == 1:
        gerente=input("\n\n\n\n" + fundo_branco + preto + "============================   vBank   ============================"+ fundo_preto + normal + "\nBem-vindo/a ao Sistema Central de Gerenciamento de Operações vBank.\nPara iniciar o SCGO vBank, informe seu IDvBank: ")
        print ("\n\n==================================================\nLogin efetuado com sucesso.\nUtilizador/a registrado/a:",gerente,"\nPerfil do/a utilizador/a: Gerente de Contas\nSistema Central de Gerenciamento de Operações\n©SCGO 2019 | Versão 1.0 | vBank®\n==================================================\n")
        opcao="1"
        while opcao != "0":
            print("\n\n" + reverso + "--------------------------------------------------\nSCGO vBank Gerente de Contas\n--------------------------------------------------\n" + normal + "\n1 = Gerenciar clientes\n2 = Gerenciar conta corrente\n0 = Sair do SCGO vBank")
            opcao=input("\nInforme a operação desejada: ")
            if opcao == "1":
                retorno=menu_secundario_clientes()
                if retorno == "s":
                    opcao="1"
            if opcao == "2":
                retorno=menu_secundario_conta()
                if retorno == "s":
                    opcao="1"
            if opcao == "0":
                desiste=valida_saida_principal()
                if desiste == "s":
                    print("\n\n==================================================\nLogout efetuado com sucesso.\nUtilizador/a registrado/a:",gerente,"\nPerfil do/a utilizador/a: Gerente de Contas\nSistema Central de Gerenciamento de Operações\n©SCGO 2019 | vBank®\n==================================================\n")
                if desiste == "1":
                    opcao="1"
            if opcao != "1" and opcao != "2" and opcao != "0":
                print("Esta não é uma opção válida.")

##################################################################################################################
# PROGRAMA PRINCIAL
##################################################################################################################

menu_principal()