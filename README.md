# 📚 Gerenciador de Tarefas em Python (CLI)

Este é um simples gerenciador de tarefas desenvolvido em Python, operado via linha de comando (CLI). Ele permite que o usuário adicione, visualize, marque como concluída e exclua tarefas, com a capacidade de salvar e carregar a lista de tarefas em um arquivo JSON.

---

## ✨ Funcionalidades

* **Adicionar Tarefa:** Inclua novas tarefas na lista.
* **Visualizar Tarefas:** Exiba todas as tarefas cadastradas, com seus respectivos números e status (concluída ou não).
* **Marcar Tarefa como Concluída:** Altere o status de uma tarefa de pendente para concluída.
* **Excluir Tarefa:** Remova tarefas da lista.
* **Persistência de Dados:** Salva e carrega a lista de tarefas automaticamente de um arquivo JSON (`lista_tarefas.json`), garantindo que suas tarefas não sejam perdidas ao fechar o programa.
* **Tratamento de Erros:** Lida com entradas inválidas do usuário (ex: digitar texto em vez de número).

---

## 🏁 Como Usar

1.  **Clone o Repositório:**
    ```bash
    git clone [https://github.com/Brenopsxky/Gerenciador-de-Tarefas.git](https://github.com/Brenopsxky/Gerenciador-de-Tarefas.git)
    cd Gerenciador-de-Tarefas
    ```

2.  **Execute o Programa:**
    ```bash
    python gerenciador_tarefas.py
    ```

3.  **Interaja via Terminal:**
    Siga as instruções exibidas no terminal para navegar entre as opções do menu (adicionar, ver, marcar, excluir, sair).

---

## 🛠️ Tecnologias Utilizadas

* **Python 3:** A linguagem de programação principal.
* **Módulo `json`:** Utilizado para salvar e carregar as tarefas em formato JSON, garantindo a persistência dos dados.

---

## 📊 Estrutura Lógica (Fluxograma) - Em atualização

A lógica central do programa segue o seguinte fluxo principal:

![Fluxograma do Gerenciador de Tarefas](docs/fluxograma_gerenciador_tarefas.png)

---

## 🚀 Status Atual do Projeto

Este projeto de Gerenciador de Tarefas acaba de receber uma grande atualização! As seguintes melhorias foram **implementadas e fazem parte do commit atual**:

* **Refatoração para POO (Programação Orientada a Objetos):**
    * As tarefas agora são representadas por **objetos da classe `Tarefa`**, encapsulando `id`, `descrição` e `status de conclusão`.
    * A lógica de gerenciamento foi centralizada na **classe `GerenciadorDeTarefas`**, que agora detém a lista de tarefas e controla suas operações.
* **Persistência Automática de Dados:** 
    * Todas as alterações nas tarefas são **salvas automaticamente** no arquivo `tarefas.json`.
    * As tarefas são **carregadas automaticamente** desse arquivo ao iniciar o programa, garantindo que nenhum dado seja perdido entre as sessões.

---

## 📈 Melhorias Futuras / Próximos Passos (MVP e Evolução)

Este projeto representa uma **Versão Mínima Viável (MVP)** do Gerenciador de Tarefas. As próximas melhorias planejadas incluem:

* **Validação e Tratamento de Erros Robusto:** Aprimorar a validação de entradas do usuário e adicionar tratamento de exceções para garantir que o programa lide graciosamente com situações inesperadas (ex: entrada de texto onde se espera um número, arquivos de dados corrompidos).
* **Melhorias na Interface do Usuário (Terminal UX/UI):** Reduzir a poluição visual, padronizar mensagens e, futuramente, explorar a criação de uma **Interface Gráfica do Usuário (GUI)** para uma experiência mais interativa.
* **Novas Funcionalidades Essenciais:** Adicionar opções cruciais para um gerenciador de tarefas completo, como:
    * **Edição de Tarefas:** Permitir a modificação da descrição de tarefas existentes.
    * **Listagem Filtrada:** Capacidade de listar tarefas por status (concluídas/pendentes).
* **Refatoração Contínua e Otimização:** Revisar e aprimorar o código existente para maior legibilidade, manutenção e eficiência.

---

## 👨‍💻 Autor

Breno Lisboa (Brenopsxky)
[https://www.linkedin.com/in/blisboa-tech/](https://www.linkedin.com/in/blisboa-tech/ | [blisboa.tech@gmail.com](mailto:blisboa.tech@gmail.com)

---
