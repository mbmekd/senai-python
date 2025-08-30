
# sistema gerenciador de nomes
nomes = []

while True:
    print("===LISTA DE NOMES==")
    print("1 - adicionar nomes")
    print("2 - listar nomes")
    print("3 - deletar todos os nomes")
    print("4 - deletar apenas um nome")
    print("9 - sair da lista de nomes")

    opcao= input ("insira uma opção:")

# adcionar nomes

    if opcao == "1":
        nome = input ("digitar nome:")
        nomes.append (nome)
        print ("nome adicionado")

# listar todos os nomes

    elif opcao == "2":
        if len (nomes) == 0:
            print ("nao existem nomes cadastrados")
        else:
            for nome in nomes :
                print (nome)

# excluir todos os nomes

    elif opcao == "3": 
        opcao= input ("deseja exluir todos os nomes? Escreva sim ou nao:")
        if opcao == "sim":
            print("Todos os nomes foram exluidos")
            nomes = []
        if opcao == "nao":
            print("Ok")
    
# excluir nome especifico

    elif opcao == "4":
        if len (nomes) == "0":
            print("nenhum nome cadastrado")
        else:
            pos = input ("escolha um nome para deletar:")
            nomes.remove (nome)
            print("nome deletado")

# encerrar sistema

    elif opcao == "9":
        print ("encerrado")
        break

   # informacoes nao validas

    else:
        print("Informação invalida")
    
