import json # Importar o módulo json para salvar/carregar dados
import os # Importar o módulo os para verificar se o arquivo existe

tarefas_global = [] # Lista global para armazenar todas as tarefas

# Definir o nome do arquivo onde as tarefas serão salvas
NOME_ARQUIVO = "tarefas.json"

def adicionar_tarefa():
    """
    Adiciona uma nova tarefa à lista de tarefas.
    A tarefa é criada com status 'concluida' como False por padrão.
    """
    descricao = input("Digite a descrição da tarefa: ")
    tarefa = {"dados_descricao": descricao, "concluida": False}
    tarefas_global.append(tarefa)
    print(f"Tarefa '{descricao}' adicionada com sucesso!")

def ver_tarefas():
    """Exibe todas as tarefas com seu status de conclusão."""
    if not tarefas_global:
        print("Nenhuma tarefa cadastrada.")
        return

    print("\n--- SUAS tarefas ---")
    for indice, tarefa in enumerate(tarefas_global):
        status = "✅" if tarefa["concluida"] else "❌"
        print(f"{indice + 1}. {status} {tarefa["dados_descricao"]}")
    print("---------------------\n")

def marcar_tarefa_concluida():
    """Permite ao usuário marcar uma tarefa existente como concluída."""
    ver_tarefas()

    if not tarefas_global:
        # Sai da função se não houver tarefas para evitar pedir input.
        return

    try:
        num_tarefa = int(input("Digite o NÚMERO da tarefa que deseja marcar como CONCLUÍDA: "))
        
        # Ajusta o número para o índice da lista (usuário digita 1, índice é 0)
        indice_real = num_tarefa - 1 

        if 0 <= indice_real < len(tarefas_global):
            tarefas_global[indice_real]["concluida"] = True 
            print(f"Tarefa '{tarefas_global[indice_real]['dados_descricao']}' marcada como CONCLUÍDA! ✅")
        else:
            print("Número de tarefa inválido. Tente novamente.")
    except ValueError:
        print("Entrada inválida. Por favor, digite um número.")

def remover_tarefa():
    """Permite ao usuário remover uma tarefa da lista."""
    ver_tarefas()

    if not tarefas_global:
        return

    try:
        num_tarefa = int(input("Digite o NÚMERO da tarefa que deseja REMOVER: "))
        indice_real = num_tarefa - 1

        if 0 <= indice_real < len(tarefas_global):
            tarefa_removida = tarefas_global.pop(indice_real)
            print(f"Tarefa '{tarefa_removida['dados_descricao']}' REMOVIDA com sucesso!")
        else:
            print("Número de tarefa inválido. Certifique-se de digitar um número da lista.")
    except ValueError:
        print("Entrada inválida. Por favor, digite um número inteiro.")


def salvar_tarefas(tarefas):
    """Salva a lista de tarefas em um arquivo JSON."""
    try:
        # Abre o arquivo em modo de escrita ('w') com codificação UTF-8
        with open(NOME_ARQUIVO, 'w', encoding='utf-8') as file:
            # ensure_ascii=False para exibir caracteres especiais (como emojis) corretamente
            # indent=4 para formatar o JSON de forma legível (com 4 espaços de indentação)
            json.dump(tarefas, file, ensure_ascii=False, indent=4)
        print("tarefas salvas com sucesso!")
    except IOError: # Captura erros de entrada/saída (problemas com o arquivo)
        print("Erro ao salvar as tarefas: problema com o arquivo.")

def carregar_tarefas():
    """Carrega as tarefas de um arquivo JSON para a lista."""
    global tarefas_global
    # É necessário expressar 'global' porque vamos reatribuir a lista 'tarefas-global'

    if not os.path.exists(NOME_ARQUIVO):
        print("Nenhum arquivo de tarefas encontrado. Iniciando com lista vazia...\n")
        tarefas_global = [] # Garante que a lista esteja vazia se o arquivo não existir
        return

    try:
        with open(NOME_ARQUIVO, 'r', encoding='utf-8') as file:
            tarefas_global = json.load(file)
        print("tarefas carregadas com sucesso!")
    except json.JSONDecodeError: # Erro se o arquivo JSON estiver mal formatado
        print("Erro ao decodificar o arquivo de tarefas. O arquivo pode estar corrompido.")
        tarefas_global = [] # Reseta as tarefas para evitar problemas
    except IOError: # Captura erros de entrada/saída
        print("Erro ao carregar as tarefas.")
        tarefas_global = [] # Reseta as tarefas por erro de acesso ao arquivo

def menu_principal():
    """Exibe o menu principal e gerencia as opções do usuário."""
    while True:
        print("--- GERENCIADOR DE tarefas ---")
        print("1. Adicionar Tarefa")
        print("2. Ver tarefas")
        print("3. Marcar Tarefa como Concluída")
        print("4. Remover Tarefa")
        print("5. Salvar tarefas")
        print("6. Carregar tarefas")
        print("7. Sair")
        print("----------------------------")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            adicionar_tarefa()
        elif opcao == '2':
            ver_tarefas()
        elif opcao == '3':
            marcar_tarefa_concluida()
        elif opcao == '4':
            remover_tarefa()
        elif opcao == '5':
            salvar_tarefas(tarefas_global)
        elif opcao == '6':
            carregar_tarefas()
        elif opcao == '7':
            print("Saindo do Gerenciador de tarefas. Até mais!")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção de 1 a 7.")

if __name__ == "__main__":
    carregar_tarefas()
    menu_principal()