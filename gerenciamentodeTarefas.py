import funcaoTarefas as ft
print('\n------------------Menu------------------') 
print ('''
    1. Adicionar Tarefa
    2. Remover Tarefa
    3. Marcar Tarefa Como Concluída
    4. Listar Todas as Tarefas
    5. Listar Tarefas Concluídas
    6. Listar Tarefas Não Concluídas
    7.Sair
''')

tarefas = []
tarefasDic = {}
opcoesValidas = ("1", "2", "3", "4", "5", "6", "7")
sair = False

while sair == False:
    opcao = input("\nEscolha uma opção: ").strip()

    if opcao not in opcoesValidas:
        print("Opção inválida, digite um número entre 1 e 7!\n")
    else: 
        opcao = int(opcao)

        if opcao == 1:
            ft.adicionarTarefa(tarefas, tarefasDic)

        if opcao == 2:
            ft.removerTarefa(tarefas, tarefasDic)

        if opcao == 3:
            ft.conclusaoTarefa(tarefasDic)

        if opcao == 4:
            print('------Minhas Tarefas------')
            for tarefa, status in tarefasDic.items():
                print(f"{tarefa}: {status}")
            print('--------------------------')
        
        if opcao == 5:
            ft.listarConcluidas(tarefasDic)
        
        if opcao == 6:
            ft.listarNaoConcluidas(tarefasDic)

        if opcao == 7:
            print("O Programa está finalizado")
            sair = True