class GerenciadorDeTarefas:
    def __init__(self):
        self.lista_de_tarefas = []
        self.iniciar_interface()
    
    def iniciar_interface(self):
        while True:
            self.mostrar_opcoes()
            escolha = input("Selecione uma opção: ")
            
            if escolha == "1":
                self.criar_nova_tarefa()
            elif escolha == "2":
                self.exibir_tarefas()
            elif escolha == "3":
                self.concluir_tarefa()
            elif escolha == "4":
                print("Até logo!")
                exit()
            else:
                print("Opção não reconhecida. Por favor, tente novamente.")
    
    def mostrar_opcoes(self):
        print("\nMenu do Gerenciador de Tarefas")
        print("1. Criar nova tarefa")
        print("2. Visualizar todas as tarefas")
        print("3. Completar uma tarefa")
        print("4. Encerrar programa")
    
    def criar_nova_tarefa(self):
        titulo = input("Informe o título da tarefa: ")
        data_limite = input("Informe a data limite (formato DD/MM/AAAA): ")
        self.registrar_tarefa(titulo, data_limite)
    
    def registrar_tarefa(self, titulo, data_limite):
        nova_tarefa = {
            'titulo': titulo,
            'data_limite': data_limite,
            'finalizada': False
        }
        self.lista_de_tarefas.append(nova_tarefa)
        print(f"Tarefa '{titulo}' registrada com sucesso!")
    
    def exibir_tarefas(self):
        if not self.lista_de_tarefas:
            print("\nNão há tarefas cadastradas no momento.")
            return
        
        print("\nTarefas Pendentes (Ordenadas por Data Limite)")
        tarefas_ordenadas = sorted(self.lista_de_tarefas, key=lambda t: t['data_limite'])
        for idx, tarefa in enumerate(tarefas_ordenadas, start=1):
            simbolo_status = "✔" if tarefa['finalizada'] else "❌"
            print(f"{idx}. [{simbolo_status}] {tarefa['titulo']} (Data: {tarefa['data_limite']})")
    
    def concluir_tarefa(self):
        self.exibir_tarefas()
        if not self.lista_de_tarefas:
            return
        
        try:
            numero_tarefa = int(input("\nInforme o número da tarefa concluída: "))
            if 1 <= numero_tarefa <= len(self.lista_de_tarefas):
                tarefas_ordenadas = sorted(self.lista_de_tarefas, key=lambda t: t['data_limite'])
                tarefa_selecionada = tarefas_ordenadas[numero_tarefa-1]
                tarefa_selecionada['finalizada'] = True
                print(f"Tarefa '{tarefa_selecionada['titulo']}' atualizada para concluída!")
            else:
                print("Número fora do intervalo válido.")
        except:
            print("Entrada inválida. Por favor, digite apenas números.")

sistema_de_tarefas = GerenciadorDeTarefas()
