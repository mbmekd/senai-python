
# sistema de tarefas
tarefas = [] # lsita vazia

while True:
    print("===MENU TAREFAS==")
    print("1 - adicionar tarefas")
    print("2 - listar tarefas")
    print("9 - sair do sistema")

    opcao = input ("escolha sua opcao:")

#adicionar tarefa
    if opcao == "1":
        tarefa = input ("digitar a nova tarefa:")
        #append adicionar a lista
        tarefas.append(tarefa)
        print("tarefa adiocionada com sucesso")
    
    #listar tarefas
    elif opcao == "2":
        #len -> length -> tamanho
        if len (tarefas) == 0:
            print ("nao existem tarefas cadastradas")
        else: 
            for tarefa in tarefas:
             print (tarefa) 

    elif opcao == "9":
        print ("encerrado")
        break
    
    else:
        print ("opcao inexistente, tente novamente...")

    