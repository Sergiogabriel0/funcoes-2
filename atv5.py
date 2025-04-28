class GerenciadorDeContatos:
    def __init__(self):
        self.lista_contatos = []
        self.iniciar_aplicativo()
    
    def iniciar_aplicativo(self):
        while True:
            self.exibir_menu_principal()
            escolha = input("\nEscolha uma opção: ")
            
            if escolha == "1":
                self.cadastrar_novo_contato()
            elif escolha == "2":
                self.pesquisar_contatos()
            elif escolha == "3":
                self.mostrar_todos_contatos()
            elif escolha == "4":
                self.editar_contato()
            elif escolha == "5":
                self.remover_contato()
            elif escolha == "6":
                print("\n Até logo! Seus contatos estão salvos.")
                break
            else:
                print("\n Opção inválida. Tente novamente.")
    
    def exibir_menu_principal(self):
        print("\n ZAPZAP - GERENCIADOR DE CONTATOS")
        print("1.  Adicionar novo contato")
        print("2.  Buscar contato")
        print("3.  Listar todos os contatos")
        print("4.  Editar contato")
        print("5.  Remover contato")
        print("6.  Sair")
    
    def cadastrar_novo_contato(self):
        print("\n➕ NOVO CONTATO")
        while True:
            nome = input("Nome completo: ").strip()
            if nome:
                break
            print("O nome não pode estar vazio!")
        
        while True:
            telefone = input("Telefone (com DDD): ").strip()
            if telefone and telefone.isdigit():
                break
            print("Telefone inválido! Use apenas números.")
        
        while True:
            email = input("E-mail: ").strip()
            if "@" in email and "." in email:
                break
            print("E-mail inválido! Digite um e-mail válido.")
        
        self.adicionar_contato(nome, telefone, email)
    
    def adicionar_contato(self, nome, telefone, email):
        novo_contato = {
            'nome': nome,
            'telefone': telefone,
            'email': email
        }
        self.lista_contatos.append(novo_contato)
        print(f"\n Contato '{nome}' adicionado com sucesso!")
    
    def pesquisar_contatos(self):
        if not self.lista_contatos:
            print("\n Sua lista de contatos está vazia.")
            return
        
        termo = input("\n Digite o nome, telefone ou e-mail para buscar: ").lower()
        resultados = []
        
        for contato in self.lista_contatos:
            if (termo in contato['nome'].lower() or 
                termo in contato['telefone'] or 
                termo in contato['email'].lower()):
                resultados.append(contato)
        
        if not resultados:
            print("\n Nenhum contato encontrado.")
        else:
            print(f"\n {len(resultados)} contato(s) encontrado(s):")
            for i, contato in enumerate(resultados, 1):
                print(f"\n{i}.  Nome: {contato['nome']}")
                print(f"    Telefone: {contato['telefone']}")
                print(f"    E-mail: {contato['email']}")
    
    def mostrar_todos_contatos(self):
        if not self.lista_contatos:
            print("\n Sua lista de contatos está vazia.")
            return
        
        print(f"\n TOTAL DE CONTATOS: {len(self.lista_contatos)}")
        for i, contato in enumerate(sorted(self.lista_contatos, key=lambda x: x['nome']), 1):
            print(f"\n{i}.  Nome: {contato['nome']}")
            print(f"    Telefone: {contato['telefone']}")
            print(f"    E-mail: {contato['email']}")
    
    def editar_contato(self):
        if not self.lista_contatos:
            print("\n Sua lista de contatos está vazia.")
            return
        
        self.mostrar_todos_contatos()
        try:
            indice = int(input("\n Digite o número do contato que deseja editar: ")) - 1
            if 0 <= indice < len(self.lista_contatos):
                contato = self.lista_contatos[indice]
                print(f"\nEditando contato: {contato['nome']}")
                
                novo_nome = input(f"Nome atual ({contato['nome']}): ").strip() or contato['nome']
                novo_telefone = input(f"Telefone atual ({contato['telefone']}): ").strip() or contato['telefone']
                novo_email = input(f"E-mail atual ({contato['email']}): ").strip() or contato['email']
                
                self.lista_contatos[indice] = {
                    'nome': novo_nome,
                    'telefone': novo_telefone,
                    'email': novo_email
                }
                print("\n Contato atualizado com sucesso!")
            else:
                print("\n Número de contato inválido!")
        except ValueError:
            print("\n Por favor, digite um número válido.")
    
    def remover_contato(self):
        if not self.lista_contatos:
            print("\n Sua lista de contatos está vazia.")
            return
        
        self.mostrar_todos_contatos()
        try:
            indice = int(input("\n Digite o número do contato que deseja remover: ")) - 1
            if 0 <= indice < len(self.lista_contatos):
                contato_removido = self.lista_contatos.pop(indice)
                print(f"\n Contato '{contato_removido['nome']}' removido com sucesso!")
            else:
                print("\n Número de contato inválido!")
        except ValueError:
            print("\n Por favor, digite um número válido.")

app_contatos = GerenciadorDeContatos()
