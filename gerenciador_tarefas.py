import json # Importar o módulo json para salvar/carregar dados
import os   # Importar o módulo os para verificar se o arquivo existe

# Classe para representar uma única tarefa
class Tarefa:
    def __init__(self, id, descricao, concluida=False):
        self.id = id
        self.descricao = descricao
        self.concluida = concluida

# Classe principal para gerenciar as tarefas
class GerenciadorDeTarefas:
    def __init__(self):
        self.tarefas = [] # Lista para armazenar objetos Tarefa
        self.proximo_id = 1
        self.NOME_ARQUIVO = "tarefas.json" # Nome do arquivo de persistência, agora atributo da classe

        # Tenta carregar as tarefas ao iniciar o gerenciador
        self._carregar_tarefas() # Usamos um método "privado" para carregar no init

    def _salvar_tarefas(self):
        """Salva a lista de tarefas em um arquivo JSON."""
        # Converte a lista de objetos Tarefa para uma lista de dicionários antes de salvar
        dados_para_salvar = []
        for tarefa in self.tarefas:
            dados_para_salvar.append({
                "id": tarefa.id,
                "descricao": tarefa.descricao,
                "concluida": tarefa.concluida
            })
        
        try:
            with open(self.NOME_ARQUIVO, 'w', encoding='utf-8') as file:
                json.dump(dados_para_salvar, file, indent=4)
        except IOError:
            print(f"Erro: Não foi possível salvar as tarefas no arquivo '{self.NOME_ARQUIVO}'.")

    def _carregar_tarefas(self):
        """Carrega as tarefas de um arquivo JSON."""
        if os.path.exists(self.NOME_ARQUIVO):
            try:
                with open(self.NOME_ARQUIVO, 'r', encoding='utf-8') as file:
                    dados = json.load(file)
                    self.tarefas = [] # Limpa a lista antes de carregar
                    maior_id = 0
                    for item_json in dados:
                        # Cria uma instância de Tarefa para cada dicionário carregado
                        tarefa = Tarefa(
                            id=item_json["id"],
                            descricao=item_json["descricao"],
                            concluida=item_json["concluida"]
                        )
                        self.tarefas.append(tarefa)
                        if item_json["id"] > maior_id:
                            maior_id = item_json["id"]
                    self.proximo_id = maior_id + 1
            except (IOError, json.JSONDecodeError):
                print(f"Aviso: Não foi possível carregar as tarefas do arquivo '{self.NOME_ARQUIVO}'. Iniciando com lista vazia...")
                self.tarefas = []
                self.proximo_id = 1
        else:
            self.tarefas = []
            self.proximo_id = 1

    def adicionar_tarefa(self):
        """Adiciona uma nova tarefa à lista."""
        descricao = input("Digite a descrição da nova tarefa: ")
        if not descricao.strip(): # Verifica se a descrição não está vazia ou só com espaços
            print("A descrição da tarefa não pode ser vazia.")
            return

        nova_tarefa = Tarefa(id=self.proximo_id, descricao=descricao)
        self.tarefas.append(nova_tarefa)
        print(f"Tarefa '{descricao}' adicionada com sucesso! (ID: {self.proximo_id})")
        self.proximo_id += 1
        self._salvar_tarefas() # Salva automaticamente após adicionar

    def ver_tarefas(self):
        """Exibe todas as tarefas."""
        if not self.tarefas:
            print("Nenhuma tarefa para exibir.")
            return

        print("\n--- Suas Tarefas ---")
        for i, tarefa in enumerate(self.tarefas): # 'tarefa' aqui é um objeto Tarefa
            status = "✅" if tarefa.concluida else "❌" # Acessa o atributo .concluida
            # Acessa os atributos do objeto Tarefa usando '.'
            print(f"{i + 1}. [ID: {tarefa.id}] {tarefa.descricao} {status}")
        print("--------------------")

    def marcar_tarefa_concluida(self):
        """Permite ao usuário marcar uma tarefa existente como concluída."""
        self.ver_tarefas() # Chama o método da própria instância

        if not self.tarefas:
            return # Sai da função se não houver tarefas

        try:
            num_tarefa = int(input("Digite o NÚMERO da tarefa que deseja marcar como CONCLUÍDA: "))
            
            # Ajusta o número para o índice da lista (usuário digita 1, índice é 0)
            indice_real = num_tarefa - 1 

            if 0 <= indice_real < len(self.tarefas):
                self.tarefas[indice_real].concluida = True # Acessa atributo do objeto Tarefa
                print(f"Tarefa '{self.tarefas[indice_real].descricao}' marcada como CONCLUÍDA! ✅")
                self._salvar_tarefas() # Salva automaticamente após modificar
            else:
                print("Número de tarefa inválido. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")

    def remover_tarefa(self):
        """Permite ao usuário remover uma tarefa existente."""
        self.ver_tarefas() # Chama o método da própria instância

        if not self.tarefas:
            return # Sai da função se não houver tarefas

        try:
            num_tarefa = int(input("Digite o NÚMERO da tarefa que deseja REMOVER: "))
            indice_real = num_tarefa - 1 

            if 0 <= indice_real < len(self.tarefas):
                tarefa_removida = self.tarefas.pop(indice_real)
                print(f"Tarefa '{tarefa_removida.descricao}' (ID: {tarefa_removida.id}) removida com sucesso! 🗑️")
                self._salvar_tarefas() # Salva automaticamente após remover
            else:
                print("Número de tarefa inválido. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")

# --- Função Principal do Menu ---
def menu_principal():
    gerenciador = GerenciadorDeTarefas() # Cria uma instância do GerenciadorDeTarefas

    while True:
        print("\n--- Gerenciador de Tarefas ---")
        print("1. Adicionar tarefa")
        print("2. Ver tarefas")
        print("3. Marcar tarefa como concluída")
        print("4. Remover tarefa")
        print("5. Sair")
        print("----------------------------")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            gerenciador.adicionar_tarefa() # Chama o método da instância
        elif opcao == '2':
            gerenciador.ver_tarefas() # Chama o método da instância
        elif opcao == '3':
            gerenciador.marcar_tarefa_concluida() # Chama o método da instância
        elif opcao == '4':
            gerenciador.remover_tarefa() # Chama o método da instância
        elif opcao == '5':
            print("Saindo do gerenciador de tarefas. Até mais!")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção entre 1 e 5.")

# Executa o menu principal se o script for executado diretamente
if __name__ == "__main__":
    menu_principal()