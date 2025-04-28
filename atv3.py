class SistemaDeReservas:
    def __init__(self):
        print("\nSistema de Reservas de Cinema")
        self.inicializar_assentos()
        self.executar_menu_principal()
    
    def inicializar_assentos(self):
        while True:
            try:
                capacidade = int(input("Informe a quantidade total de assentos: "))
                if capacidade <= 0:
                    print("A sala deve ter pelo menos 1 assento.")
                    continue
                    
                self.capacidade_total = capacidade
                self.assentos = {num: False for num in range(1, capacidade + 1)}
                break
            except ValueError:
                print("Por favor, insira um número válido.")
    
    def executar_menu_principal(self):
        while True:
            self.exibir_opcoes()
            escolha = input("\nSelecione uma opção: ")
            
            if escolha == "1":
                self.exibir_mapa_assentos()
            elif escolha == "2":
                self.realizar_reserva()
            elif escolha == "3":
                self.liberar_assento()
            elif escolha == "4":
                print("\n🍿 Bom filme! Volte sempre!")
                break
            else:
                print("Opção inválida. Por favor, tente novamente.")
    
    def exibir_opcoes(self):
        print("\n=== MENU PRINCIPAL ===")
        print("1. Visualizar mapa de assentos")
        print("2. Reservar assento")
        print("3. Cancelar reserva")
        print("4. Sair do sistema")
    
    def exibir_mapa_assentos(self):
        print("\n Mapa de Assentos (Disponível = ○ | Ocupado = ●)")
        print("=" * 50)
        
        for num, ocupado in self.assentos.items():
            simbolo = "●" if ocupado else "○"
            print(f"{num:03d}: {simbolo}", end="  ")
            
            if num % 5 == 0:
                print()
        
        print("\n" + "=" * 50)
    
    def realizar_reserva(self):
        self.exibir_mapa_assentos()
        
        while True:
            try:
                assento = int(input("\nInforme o número do assento desejado: "))
                
                if assento not in self.assentos:
                    print(f"Assento inválido. Escolha entre 1 e {self.capacidade_total}.")
                    continue
                    
                if self.assentos[assento]:
                    print(f" O assento {assento} já está ocupado.")
                else:
                    self.assentos[assento] = True
                    print(f" Assento {assento} reservado com sucesso!")
                break
                
            except ValueError:
                print("Por favor, digite apenas números.")
    
    def liberar_assento(self):
        self.exibir_mapa_assentos()
        
        while True:
            try:
                assento = int(input("\nInforme o número do assento para cancelar: "))
                
                if assento not in self.assentos:
                    print(f"Assento inválido. Escolha entre 1 e {self.capacidade_total}.")
                    continue
                    
                if not self.assentos[assento]:
                    print(f" O assento {assento} já está livre.")
                else:
                    self.assentos[assento] = False
                    print(f" Reserva do assento {assento} cancelada.")
                break
                
            except ValueError:
                print("Por favor, digite apenas números.")

# Inicia o sistema de reservas
sala_cinema = SistemaDeReservas()
