class GerenciadorDeEstoque:
    def __init__(self):
        self.itens_em_estoque = []
        self.iniciar_sistema()
    
    def iniciar_sistema(self):
        while True:
            self.exibir_menu_principal()
            escolha = self.obter_escolha_usuario()
            
            if escolha == "1":
                self.cadastrar_novo_item()
            elif escolha == "2":
                self.mostrar_relatorio_estoque()
            elif escolha == "3":
                print("Até a próxima!")
                break
            else:
                print("Opção não reconhecida. Por favor, tente novamente.")
    
    def exibir_menu_principal(self):
        print("\n=== CONTROLE DE ESTOQUE ===")
        print("1. Cadastrar novo produto")
        print("2. Consultar estoque")
        print("3. Encerrar sistema")
    
    def obter_escolha_usuario(self):
        return input("\nDigite o número da opção desejada: ")
    
    def cadastrar_novo_item(self):
        nome_produto = input("\nInforme o nome do produto: ")
        qtd_estoque = self.obter_quantidade_valida()
        preco_unitario = self.obter_preco_valido()
        
        self.registrar_produto(nome_produto, qtd_estoque, preco_unitario)
    
    def obter_quantidade_valida(self):
        while True:
            entrada = input("Informe a quantidade em estoque: ")
            if entrada.isdigit():
                return int(entrada)
            print("Valor inválido! Digite um número inteiro.")
    
    def obter_preco_valido(self):
        while True:
            entrada = input("Informe o preço unitário (ex: 19.99): ")
            try:
                return float(entrada)
            except ValueError:
                print("Valor inválido! Use o formato 00.00")
    
    def registrar_produto(self, nome, quantidade, preco):
        novo_item = {
            'nome': nome,
            'quantidade': quantidade,
            'preco': preco
        }
        self.itens_em_estoque.append(novo_item)
        print(f"\n'{nome}' foi adicionado ao estoque com sucesso!")
    
    def mostrar_relatorio_estoque(self):
        if not self.itens_em_estoque:
            print("\nNenhum produto cadastrado no estoque.")
            return
        
        valor_total_estoque = 0
        print("\nRELATÓRIO DE ESTOQUE")
        
        for indice, produto in enumerate(self.itens_em_estoque, start=1):
            valor_item = produto['quantidade'] * produto['preco']
            valor_total_estoque += valor_item
            
            print(f"\n{item}. {produto['nome'].upper()}")
            print(f"   Quantidade disponível: {produto['quantidade']} unidades")
            print(f"   Preço unitário: R$ {produto['preco']:.2f}")
            print(f"   Valor total: R$ {valor_item:.2f}")
        
        print(f"\nVALOR TOTAL DO ESTOQUE: R$ {valor_total_estoque:.2f}")

sistema_estoque = GerenciadorDeEstoque()
