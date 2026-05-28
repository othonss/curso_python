import subprocess
import json

def ler(tarefas, caminho_arquivo):
    dados = []
    try:
        with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
            dados = json.load(arquivo)
    except FileNotFoundError:
        print('Arquivo não existe')
        salvar(tarefas, caminho_arquivo)
    return dados

def salvar(tarefas, caminho_arquivo):
    dados = tarefas
    with open(caminho_arquivo, 'w', encoding='utf-8') as arquivo:
        dados = json.dump(tarefas, arquivo, indent=2, ensure_ascii=False)
    return dados


CAMINHO_ARQUIVO = 'video197.json'
lista_tarefas = ler([], CAMINHO_ARQUIVO)
lixeira_tarefas = []


while True:
    print("\nAdicione uma tarefa ou use os comandos: \n Listar - para mostrar as tarefas \n Desfazer - para desfazer a última tarefa \n Refazer - para refazer a última tarefa desfeita \n Limpar - para limpar a tela \n Sair - para sair do programa\n")
    acao = input("Adicionar tarefa: ")
    acao = acao.lower()
    print()
    if acao == "listar":
        if lista_tarefas:
            print("Tarefas:")
            for tarefa in lista_tarefas:
                print(f"- {tarefa}")
        else:
            print("Não há tarefas para serem listadas.")
    elif acao == "desfazer":
        if lista_tarefas:
            tarefa_removida = lista_tarefas.pop()
            lixeira_tarefas.append(tarefa_removida)
            print(f"Tarefa removida: {tarefa_removida}")
        else:
            print("Não há tarefas para desfazer.")
    elif acao == "refazer":
        if lixeira_tarefas:
            tarefa_refeita = lixeira_tarefas.pop()
            lista_tarefas.append(tarefa_refeita)
            print(f"Tarefa refazida: {tarefa_refeita}")
        else:
            print("Não há tarefas para refazer.")
    elif acao == "sair":
        break
    elif acao == "clear" or acao == "limpar":
        subprocess.run('cls', shell=True)
    else:
        if acao != "":
            lista_tarefas.append(acao)
        else:
            print('Você não digitou uma tarefa ou comando.')
    
    salvar(lista_tarefas, CAMINHO_ARQUIVO)