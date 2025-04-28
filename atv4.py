class SistemaBancario:
    def __init__(self):
        self.contas = {
            'admin': {'senha': '1234', 'saldo': 1000.00, 'historico': []},
            'cliente1': {'senha': 'abcd', 'saldo': 500.00, 'historico': []}
        }
        self.conta_autenticada = None
        self.iniciar_sistema()

    def iniciar_sistema(self):
        while True:
            self.exibir_menu_principal()
            opcao = input("\nEscolha uma opção: ")
            
            if opcao == "1":
                self.realizar_login()
                if self.conta_autenticada:
                    self.menu_operacoes()
            elif opcao == "2":
                self.criar_nova_conta()
            elif opcao == "3":
                print("\nObrigado por usar nosso sistema bancário. Até logo!")
                break
            else:
                print("\nOpção inválida. Por favor, tente novamente.")

    def exibir_menu_principal(self):
        print("\n BANCO DIGITAL")
        print("1. Acessar minha conta")
        print("2. Criar nova conta")
        print("3. Sair do sistema")

    def realizar_login(self):
        print("\n ÁREA DE LOGIN")
        usuario = input("Nome de usuário: ")
        senha = input("Senha: ")
        
        if usuario in self.contas and self.contas[usuario]['senha'] == senha:
            self.conta_autenticada = usuario
            print(f"\n Login realizado com sucesso! Bem-vindo(a), {usuario}!")
            return True
        else:
            print("\n Credenciais inválidas. Verifique seu usuário e senha.")
            return False

    def criar_nova_conta(self):
        print("\n CADASTRO DE NOVA CONTA")
        while True:
            novo_usuario = input("Escolha um nome de usuário: ")
            
            if novo_usuario in self.contas:
                print("Este nome de usuário já está em uso. Tente outro.")
            else:
                break
                
        nova_senha = input("Crie uma senha: ")
        self.contas[novo_usuario] = {
            'senha': nova_senha,
            'saldo': 0.00,
            'historico': []
        }
        print(f"\n Conta criada com sucesso! Bem-vindo(a), {novo_usuario}!")

    def menu_operacoes(self):
        while self.conta_autenticada:
            self.exibir_menu_conta()
            opcao = input("\nEscolha uma operação: ")
            
            if opcao == "1":
                self.realizar_deposito()
            elif opcao == "2":
                self.realizar_saque()
            elif opcao == "3":
                self.consultar_extrato()
            elif opcao == "4":
                self.consultar_saldo()
            elif opcao == "5":
                print(f"\nAté breve, {self.conta_autenticada}!")
                self.conta_autenticada = None
            else:
                print("\nOpção inválida. Tente novamente.")

    def exibir_menu_conta(self):
        print(f"\n CONTA: {self.conta_autenticada}")
        print("1. Realizar depósito")
        print("2. Realizar saque")
        print("3. Consultar extrato")
        print("4. Ver saldo atual")
        print("5. Encerrar sessão")

    def realizar_deposito(self):
        print("\n DEPÓSITO")
        while True:
            valor = input("Valor a depositar: R$ ")
            try:
                valor = float(valor)
                if valor > 0:
                    self.contas[self.conta_autenticada]['saldo'] += valor
                    transacao = f"Depósito: +R${valor:.2f}"
                    self.registrar_transacao(transacao)
                    print(f"\n Depósito realizado com sucesso!")
                    self.consultar_saldo()
                    break
                else:
                    print("O valor deve ser positivo.")
            except ValueError:
                print("Por favor, insira um valor numérico válido.")

    def realizar_saque(self):
        print("\n SAQUE")
        while True:
            valor = input("Valor a sacar: R$ ")
            try:
                valor = float(valor)
                if valor <= 0:
                    print("O valor deve ser positivo.")
                elif valor > self.contas[self.conta_autenticada]['saldo']:
                    print("Saldo insuficiente para esta operação.")
                else:
                    self.contas[self.conta_autenticada]['saldo'] -= valor
                    transacao = f"Saque: -R${valor:.2f}"
                    self.registrar_transacao(transacao)
                    print(f"\n Saque realizado com sucesso!")
                    self.consultar_saldo()
                    break
            except ValueError:
                print("Por favor, insira um valor numérico válido.")

    def consultar_extrato(self):
        print(f"\n EXTRATO BANCÁRIO - {self.conta_autenticada}")
        historico = self.contas[self.conta_autenticada]['historico']
        
        if not historico:
            print("Nenhuma transação registrada.")
        else:
            for transacao in historico:
                print(f"- {transacao}")
        
        self.consultar_saldo()

    def consultar_saldo(self):
        saldo = self.contas[self.conta_autenticada]['saldo']
        print(f"\nSeu saldo atual é: R${saldo:.2f}")

    def registrar_transacao(self, transacao):
        self.contas[self.conta_autenticada]['historico'].append(transacao)

banco_digital = SistemaBancario()
