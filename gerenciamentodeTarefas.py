import funcaoTarefas as ft
print('Menu') 
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
sair = False

while sair == False:
    opcao = int(input('Escolha a opção que deseja: '))
    if opcao == 1:
        ft.adicionarTarefa(tarefas, tarefasDic)
        print(tarefas)
    
    if opcao == 2:
        ft.removerTarefa(tarefas, tarefasDic)
        
    if opcao == 3:
        ft.conclusaoTarefa(tarefasDic)
        
    if opcao == 4:
        print(tarefas)
        
    if opcao == 7:
        sair = True