import os 
lista = []
rodando = True
while rodando:
    opcao_escolhida = input(
    '[1] para Inserir um item na lista:\n'
    '[2] para apagar a lista:\n'
    '[3] para mostrar os itens da lista:\n'
    '[4] para finalizar o programa.\n'
    'Escolha uma das opções acima: '
    )
    try:
        escolha = int(opcao_escolhida)
        if escolha > 4 or escolha == 0:
            print('\n***INFORME APENAS OS NÚMEROS [1, 2, 3 OU 4] ENTRE AS OPÇÕES***\n')
        elif escolha == 1:
            os.system('cls')
            item_novo = input('Digite o item: ')
            lista.append(item_novo)
        elif escolha == 2:
            lista.clear()
            print('\n***LISTA APAGADA!***\n')
        elif escolha == 3:
            os.system('cls')
            for indice, item in enumerate(lista):
                print(indice, item)
        elif escolha == 4:
            os.system('cls')
            print('\n***PROGRAMA FINALIZADO***\n')
            rodando = False
    except:
        print('\n***INFORME APENAS NÚMEROS PARA AS OPÇÕES***\n')
    
        
    