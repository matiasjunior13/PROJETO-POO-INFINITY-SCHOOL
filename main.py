class Cliente:
    def __init__(self, id:int, nome:str, idade:int, cpf:float, telefone:str,email:str ) -> None:
        self.id = id
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        self.telefone = telefone
        self.email = email

class Quarto:
    def __init__(self, id:int, nome:str, valor:int ) -> None:
        self.id = id
        self.nome = nome
        self.valor = valor
        self.disponibilidade = True

class Reserva:
    def __init__(self, id:int, data_entrada:str, id_quarto:int, id_cliente:float,data_saida:str ) -> None:
        self.id = id
        self.data_entrada = data_entrada
        self.id_quarto = id_quarto
        self.id_cliente = id_cliente
        self.data_saida = data_saida



class Hotel:
    def __init__(self, nome:str) -> None:
        self.nome = nome
        self.lista_de_clientes = []
        self.lista_de_quartos = []
        self.lista_de_reservas = []
        self.historico_de_reservas = []
        self.id_clientes = 1
        self.id_quartos = 1
        self.id_reservas = 1
    
    def cadastrarCliente(self):
        nome = input("Digite o nome do cliente: ")
        idade = int(input("Digite a idade do cliente: "))
        cpf = input("Digite o CPF do cliente: ")
        telefone = input("Digite o telefone do cliente: ")
        email = input("Digite o email do cliente: ")
        
        cliente = Cliente(id= self.id_clientes, nome=nome, cpf=cpf,idade=idade, telefone=telefone, email=email)
        self.id_clientes +=1

        self.lista_de_clientes.append(cliente)
        return "Cliente cadastrado com sucesso."
    
    def verClientes(self):
        for cliente_da_vez in self.lista_de_clientes:
            print(f"""
            ID: {cliente_da_vez.id}
            Nome: {cliente_da_vez.nome}
            CPF: {cliente_da_vez.cpf}
            Idade: {cliente_da_vez.idade}
            Telefone: {cliente_da_vez.telefone}
            E-mail: {cliente_da_vez.email}
            """)


    def editarCliente(self):
        id_cliente = int(input("Digite o ID do cliente que você deseja editar: "))
        cliente_encontrado = False
        for cliente_da_vez in self.lista_de_clientes:
            if cliente_da_vez.id == id_cliente:
                cliente_encontrado = True
                nome = input("Digite o novo nome do cliente: ")
                idade = int(input("Digite a nova idade do cliente: "))
                cpf = input("Digite o novo CPF do cliente: ")
                telefone = input("Digite o novo telefone do cliente: ")
                email = input("Digite o novo email do cliente: ")
                cliente_da_vez.nome = nome
                cliente_da_vez.idade = idade
                cliente_da_vez.cpf = cpf


                cliente_da_vez.telefone = telefone
                cliente_da_vez.email = email
                return "Cliente atualizado com sucesso"

        if cliente_encontrado == False:
            return "Cliente não encontrado"

    def removerCLiente(self):
        id_cliente = int(input("Digite o ID do cliente que você deseja editar: "))
        cliente_encontrado = False
        for cliente_da_vez in self.lista_de_clientes:
            if cliente_da_vez.id == id_cliente:
                cliente_encontrado = True
                self.lista_de_clientes.remove(cliente_da_vez)
                return "Cliente removido com sucesso"

        if cliente_encontrado == False:
            return "Cliente não encontrado"

    def cadastrarQuarto(self):
        nome = input("Digite o nome do quarto: ")
        valor = float(input("Digite a valor do quarto: "))
        
        quarto = Quarto(id= self.id_quartos, nome=nome,valor=valor)
        self.id_quartos +=1

        self.lista_de_quartos.append(quarto)
        return "Quarto criado com sucesso."

    
    def verQuartos(self):
        for quarto_da_vez in self.lista_de_quartos:
            print(f"""
            ID: {quarto_da_vez.id}
            Nome: {quarto_da_vez.nome}
            Valor: R${quarto_da_vez.valor}
            Disponibilidade: {quarto_da_vez.disponibilidade}
            """)

    def editarQuarto(self):
        id_quarto = int(input("Digite o ID do quarto que você deseja editar: "))
        quarto_encontrado = False
        for quarto_da_vez in self.lista_de_quartos:
            if quarto_da_vez.id == id_quarto:
                quarto_encontrado = True
                while True:
                    menu_editar_quarto = input("""
                    O que você quer editar:
                    1 - Nome
                    2 - Valor
                    0 - Voltar
                    """)
                    match menu_editar_quarto:
                        case "1":
                            novo_nome = input("Digite o novo nome do quarto: ")
                            quarto_da_vez.nome = novo_nome
                        case "2":
                            novo_valor = int(input("Digite o novo valor do quarto: "))
                            quarto_da_vez.valor = novo_valor
                        case "0":
                            return "Quarto atualizado com sucesso"
                        case _:
                            print("Opção inválida")


        if quarto_encontrado == False:
            return "Quarto não encontrado"

    def removerQuarto(self):
        id_quarto = int(input("Digite o ID do quarto que você deseja editar: "))
        quarto_encontrado = False
        for quarto_da_vez in self.lista_de_quartos:
            if quarto_da_vez.id == id_quarto:
                quarto_encontrado = True
                self.lista_de_quartos.remove(quarto_da_vez)
                return "Quarto removido com sucesso"

        if quarto_encontrado == False:
            return "Quarto não encontrado"


    def fazerReserva(self):
        data_entrada = input("Digite a data de entrada da reserva: ")
        data_saida = input("Digite a data de saida da reserva: ")
        for quarto_da_vez in self.lista_de_quartos:
            print(f"""ID: {quarto_da_vez.id} -  Nome:{quarto_da_vez.nome}""")
        id_quarto = int(input("Digite o ID do quarto da reserva: "))
        for quarto_da_vez in self.lista_de_quartos:
            if quarto_da_vez.id == id_quarto and quarto_da_vez.disponibilidade == True:
                for cliente_da_vez in self.lista_de_clientes:
                    print(f"""ID: {cliente_da_vez.id}-    Nome: {cliente_da_vez.nome}""")
                id_cliente = int(input("Digite o ID do cliente da reserva: "))
                for cliente_da_vez in self.lista_de_clientes:
                    if cliente_da_vez.id == id_cliente:
                        quarto_da_vez.disponibilidade = False
                        reserva = Reserva(id= self.id_reservas, data_entrada=data_entrada, data_saida=data_saida, id_quarto=id_quarto, id_cliente=id_cliente)
                        self.id_reservas +=1
                        self.lista_de_reservas.append(reserva)
                        self.historico_de_reservas.append(reserva)
                        return f"Reserva do quarto {quarto_da_vez.nome} realizada com sucesso para o cliente {cliente_da_vez.nome}"
                    

                    
    def encerrarReserva(self):
        id_reserva = int(input("Digite o ID da reserva que você deseja encerrar: "))
        for reserva_da_vez in self.lista_de_reservas:
            if reserva_da_vez.id == id_reserva:
                for quarto_da_vez in self.lista_de_quartos:
                    if quarto_da_vez.id == reserva_da_vez.id_quarto:
                        quarto_da_vez.disponibilidade = True
                        self.lista_de_reservas.remove(reserva_da_vez)
                        return "Reserva encerrada."

    def verQuartosReservados(self):
        for quarto_da_vez in self.lista_de_quartos:
            if quarto_da_vez.disponibilidade == False:
                print(f"""
                ID: {quarto_da_vez.id}
                Nome: {quarto_da_vez.nome}
                CPF: {quarto_da_vez.valor}
                Disponibilidade: {quarto_da_vez.disponibilidade}
                """)

    def verQuartosDisponiveis(self):
        for quarto_da_vez in self.lista_de_quartos:
            if quarto_da_vez.disponibilidade == True:
                print(f"""
                ID: {quarto_da_vez.id}
                Nome: {quarto_da_vez.nome}
                CPF: {quarto_da_vez.valor}
                Disponibilidade: {quarto_da_vez.disponibilidade}
                """)


hotel1 = Hotel(nome="Hotel Terra da Luz")

while True:
    menu = input("""
    \n
    ============================= Hotel Terra da Luz =============================
    Seja bem vindo!
    \n
    Orientações para utilização do sistema:
    - Cadastrar Quarto
    - Cadastrar Cliente
    Obs.: Após o cadastro é possivel utilizar todas as opções do menu.
    \n
    \n
    Escolha uma opção:
    1 - Ver Quartos disponiveis
    2 - Ver Quartos reservados
    3 - Fazer uma Reserva
    4 - Encerrar uma Reversa
    5 - Gerenciar Clientes
    6 - Gerenciar Quartos
    0 - Sair
    """)

    match menu:
        case "1":
            hotel1.verQuartosDisponiveis()
        case "2":
            hotel1.verQuartosReservados()
        case "3":
            print(hotel1.fazerReserva())
        case "4":
            print(hotel1.encerrarReserva())
        case "5":
            while True:
                menu_cliente = input("""
                    Escolha uma opção:
                    1 - Adicionar Cliente
                    2 - Ver todos os Clientes
                    3 - Editar Cliente
                    4 - Excluir Cliente
                    0 - Voltar
                    """)
                match menu_cliente:
                    case "1":
                        print(hotel1.cadastrarCliente())
                    case "2":
                        hotel1.verClientes()
                    case "3":
                        print(hotel1.editarCliente())
                    case "4":
                        print(hotel1.removerCLiente())
                    case "0":
                        print("Voltando ao menu principal")
                        break
                    case _:
                        print("Opção Inválida")
        case "6":
            while True:
                menu_quarto = input("""
                    Escolha uma opção:
                    1 - Adicionar Quarto
                    2 - Ver todos os Quartos
                    3 - Editar Quarto
                    4 - Excluir Quarto
                    0 - Voltar
                    """)
                match menu_quarto:
                    case "1":
                        print(hotel1.cadastrarQuarto())
                    case "2":
                        hotel1.verQuartos()
                    case "3":
                        print(hotel1.editarQuarto())
                    case "4":
                        print(hotel1.removerQuarto())
                    case "0":
                        print("Voltando ao menu principal")
                        break
                    case _:
                        print("Opção Inválida")
        case "0":
            print("Fim do Programa")
            break
        case _:
            print("Opção inválida")
