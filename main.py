import datetime
import os


menu = """

  +--------------------------------------+
  |   S I S T E M A    B A N C Á R I O   |
  +--------------------------------------+

  ****************************************
  *                                      *
  *         [d] Depositar                *
  *         [s] Sacar                    *
  *         [e] Extrato                  *
  *         [c] Cadastrar Cliente        *
  *         [p] Consultar Cliente        *
  *         [v] Listar Clientes          *
  *         [n] Criar Conta Corrente     *
  *         [t] Listar Contas            *
  *         [l] Limpar Tela              *
  *         [q] Sair                     *
  *                                      *
  ****************************************
"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

mensagem = ""

data = datetime.date.today()
hoje = ("00" + str(data.day))[-2:] + "/" + ("00" + str(data.month))[-2:] + "/" + str(data.year)


clientes = []
contas = []


def depositar(saldo_atual):
    global mensagem

    valor = input("\nInforme o valor do depósito: ")

    try:
        valor = float(valor) if len(valor) > 0 else 0
    
    except:
        valor = 0


    if valor > 0:
        print ("\n+----------")
        print(f"|  Depósito de R$ {valor:.2f} realizado com sucesso!")
        print(f"|  Seu saldo atual é de R$ {(saldo_atual+valor):.2f}")
        print ("+----------")

    else:
        print("\n=> Operação falhou! O valor informado é inválido.")

    mensagem = ""
    input()

    return valor


def saque(saldo_atual, limite_atual, numero_de_saques, limite_de_saques):
    global mensagem

    print(f"\n=> Seu saldo atual é de R$ {saldo_atual:.2f}\n")

    if saldo_atual > 0:
        valor = input("Informe o valor do saque: ")

        try:
            valor = float(valor) if len(valor) > 0 else 0

        except:
            valor = 0


        excedeu_saldo = valor > saldo_atual 
        excedeu_limite = valor > limite_atual
        excedeu_saques = numero_de_saques >= limite_de_saques
        
        mensagem = ""

        if excedeu_saldo:
            print("\n=> Operação falhou! Você não tem saldo suficiente.")
        
        elif excedeu_limite:
            print(f"\n=> Operação falhou! O valor do saque excedeu o limite de R$ {limite_atual:.2f}.")
        
        elif excedeu_saques:
            print(f"\n=> Operação falhou! Número máximo de saques excedido.\n=> Você tem direito a {limite_de_saques} saques diários.")
        
        elif valor > 0:
            print ("\n+----------")
            print(f"|  Saque de R$ {valor:.2f} realizado com sucesso!")
            print(f"|  Seu saldo atual é de R$ {saldo_atual:.2f}")
            print ("+----------")
        
        else:  
            print("Operação falhou! O valor informado é inválido.")
            
        
        input()
        
        return valor


    else:  
        mensagem = """
+---------------------------------+
|  Você não tem saldo suficiente  |
|  para saque.                    |
+---------------------------------+
"""
   
    return 0


def ver_extrato(saldo_atual, ver_extrato):
    global mensagem

    print("\n===================== EXTRATO =====================\n")
    print("=> Não foram realizadas movimentações." if not ver_extrato else ver_extrato)
    print(f"\nSaldo: R$ {saldo_atual:.2f}")
    print("\n===================================================")

    mensagem = ""
    input("")


def criar_usuario():

    while True:    
        os.system("cls")

        print("\n===================== CADASTRO DE CLIENTES =====================\n")
        
        cpf_existe = False

        cpf = input("Informe o CPF: ")
        
        if len(cpf) > 0:
            if len(clientes) > 0:
                for lista in clientes:
                    if lista[2] == cpf:
                        cpf_existe = True


            if not cpf_existe:
                nome = input("Informe o nome: ")
                data_nascimento = input("Informe a data de nascimento: ")
                endereco = input("Informe o endereço: ")

                novo = [nome, data_nascimento, cpf, endereco]

                clientes.append(novo)
                
                print("")

            else:
                print("\n=> CPF já existe no banco de dados.\n")
        
        else:
            print("")    

        acao = input("[Enter] para Continuar ou [S] para Sair.")
        
        if acao.lower() == "s":
            break
        

def consultar_cliente():

    while True:    
        os.system("cls")

        print("\n====================== CONSULTAR CLIENTE ======================\n")
        
        cpf_existe = False

        cpf = input("Informe o CPF.....:  ")
        
        if len(cpf) > 0:
            if len(clientes) > 0:
                for lista in clientes:
                    if lista[2] == cpf:
                        
                        print("Nome..............: ", lista[0])
                        print("Data de Nascimento: ", lista[1])
                        print("Endereço..........: ", lista[3])
                        
                        cpf_existe = True


            if cpf_existe:

                print("\n=> Conta(s) Corrente(s) Vínculada(s):\n")
                
                if len(contas) > 0:
                    for conta in contas:
                        if conta[3] == cpf:    
                            print("Número da Conta..: ", conta[0])
                            print("Agência..........: ", conta[1])
                            print("-"*30)

                print("")

            else:
                print("\n=> CPF já existe no banco de dados.\n")
        
        else:
            print("")    

        acao = input("[Enter] para Continuar ou [S] para Sair.")
        
        if acao.lower() == "s":
            break


def listar_usuarios():
    os.system("cls")

    print("\n================ LISTAGEM DE CLIENTES CADASTRADOS ===============\n")
    
    tracos = ""

    for lista in clientes:
        print(tracos * 65)
        
        print("Nome..............: ", lista[0])
        print("Data de Nascimento: ", lista[1])
        print("CPF...............: ", lista[2])
        print("Endereço..........: ", lista[3])
        
        tracos = "-"
        
    print("")
    input("Pressione [Enter] para continuar.")


def criar_conta():
    while True:    
        os.system("cls")

        print("\n==================== CRIAR CONTA CORRENTE ====================\n")
        
        cpf_existe = False
        nome = ""
        numero_conta = len(contas) + 1
        agencia = "0001"

        cpf = input("Informe o CPF do Cliente: ")
        
        if len(cpf) > 0:
            if len(clientes) > 0:
                for lista in clientes:
                    if lista[2] == cpf:
                        nome = lista[0]
                        cpf_existe = True


            if cpf_existe:
                novo = [numero_conta, agencia, nome, cpf]

                contas.append(novo)
                
                print("\nConta cadastrada com sucesso!\n")
                print("- Número da Conta: ", numero_conta)
                print("- Agência........: ", agencia)
                print("")

            else:
                print("\n=> CPF não existe no banco de dados.\n")
        
        else:
            print("")    

        acao = input("[Enter] para Continuar ou [S] para Sair.")
        
        if acao.lower() == "s":
            break
        

def listar_contas():
    os.system("cls")

    print("\n================== LISTAGEM DE CONTAS CORRENTES =================\n")
    
    tracos = ""

    for lista in contas:
        print(tracos * 65)
        
        print("Número da Conta...: ", lista[0])
        print("Agência...........: ", lista[1])
        print("Nome do Cliente...: ", lista[2])
        print("CPF do Cliente....: ", lista[3])
        
        tracos = "-"
        
    print("")
    input("\nPressione [Enter] para continuar.")


while True:
    os.system("cls")
    
    print(menu)
    print(mensagem)
    opcao = input("  => Informe a opção: ").lower()

    if opcao == "d":
        valor = depositar(saldo)
        
        if valor > 0:
            saldo += valor
            extrato += hoje + " - "
            extrato += f"Depósito de R$ {valor:.2f}\n"
        

    elif opcao == "s":
        valor = saque(
                        saldo_atual=saldo, 
                        limite_atual=limite, 
                        numero_de_saques=numero_saques, 
                        limite_de_saques=LIMITE_SAQUES
                     )

        if valor > 0:
            saldo -= valor
            extrato += hoje + " - "
            extrato += f"Saque de R$ {valor:.2f}\n"
            numero_saques += 1


    elif opcao == "e":
        ver_extrato(saldo, ver_extrato=extrato)


    elif opcao == "c":
        criar_usuario()
       
        mensagem = ""
        continue


    elif opcao == "p":
        consultar_cliente()
       
        mensagem = ""
        continue

    elif opcao == "v":
        listar_usuarios()
       
        mensagem = ""
        continue


    elif opcao == "n":
        criar_conta()

        mensagem = ""
        continue


    elif opcao == "t":
        listar_contas()

        mensagem = ""
        continue


    elif opcao == "l":
        mensagem = ""
        continue


    elif opcao == "q":
        print("\n\n  =================================\n")
        print("         SISTEMA FINALIZADO!")
        print("\n  =================================\n\n\n")
        
        break


    else:
        mensagem = """
+-------------------------------------------------------+
|  Operação inválida!                                   |
|  Por favor, selecione novamente a operação desejada.  |
+-------------------------------------------------------+
"""
