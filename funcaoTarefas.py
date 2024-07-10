def adicionarTarefa(tarefas, tarefasDic):
    tarefa = input("Digite o nome da tarefa para adicionar:")
    tarefas.append(tarefas)
    tarefasDic.update({tarefa:"Não Concluída"})
    
def removerTarefa (tarefas,tarefasDic):
    tarefa = input("Digite o nome da tarefa para remover:")
    tarefas.remove(tarefa)
    tarefasDic.pop(tarefa)

def conclusaoTarefa(tarefasDic):
    tarefa = input("Digite o nome para marcar a tarefa que está concluída:")
    tarefasDic.update ({tarefa:"Concluída"})
    print(tarefasDic)