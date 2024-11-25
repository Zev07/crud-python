class Contato:
    """Representação do contato"""
    def __init__(self, nome: str, telefone: str, profissao: str):
        self.nome = nome
        self.telefone = telefone
        self.profissao = profissao

    """Apresentação"""
    def __str__(self):
        return f"Nome: {self.nome}, Telefone: {self.telefone}, Profissão: {self.profissao}"

def adicionar_pessoa(lista_pessoas):
    print("\n --- Adicionar Pessoa ---")
    nome = input("Digite o nome: ")
    telefone = input("Digite o telefone: ")
    profissao = input("Digite a profissão: ")

    contato = Contato(nome, telefone, profissao)
    lista_pessoas.append(contato)
    print("Pessoa adicionada com sucesso!")

def listar_pessoas(lista_pessoas):
    print("\n --- Lista de Contatos ---")
    if not lista_pessoas:
        print("Nenhuma pessoa cadastrada.")
    else:
        for i, pessoa in enumerate(lista_pessoas, start=1):
            print(f"{i}. {pessoa}")

def remover_pessoa(lista_pessoas):
    print("\n --- Remover Pessoa ---")
    listar_pessoas(lista_pessoas)
    
    if lista_pessoas:
        try:
            index = int(input("Digite o número da pessoa a ser removida: ")) - 1
            if 0 <= index < len(lista_pessoas):
                removed = lista_pessoas.pop(index)
                print(f"{removed.nome} foi removido da lista.")
            else:
                print("Índice inválido.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")

def modificar_pessoa(lista_pessoas):
    print("\n --- Modificar Pessoa ---")
    listar_pessoas(lista_pessoas)
    
    if lista_pessoas:
        try:
            index = int(input("Digite o número da pessoa a ser modificada: ")) - 1
            if 0 <= index < len(lista_pessoas):
                pessoa = lista_pessoas[index]
                
                print(f"Modificando os dados de {pessoa.nome}:")
                novo_nome = input(f"Novo nome (atual: {pessoa.nome}): ")
                novo_telefone = input(f"Novo telefone (atual: {pessoa.telefone}): ")
                nova_profissao = input(f"Nova profissão (atual: {pessoa.profissao}): ")

                pessoa.nome = novo_nome if novo_nome else pessoa.nome
                pessoa.telefone = novo_telefone if novo_telefone else pessoa.telefone
                pessoa.profissao = nova_profissao if nova_profissao else pessoa.profissao
                
                print(f"{pessoa.nome} foi atualizado com sucesso.")
            else:
                print("Índice inválido.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")

def menu_principal():
    lista_pessoas = []

    while True:
        print("\n --- Agenda de Contato ---")
        print("1. Adicionar Pessoa")
        print("2. Listar Pessoas")
        print("3. Remover Pessoa")
        print("4. Modificar Pessoa")
        print("5. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_pessoa(lista_pessoas)
        elif opcao == "2":
            listar_pessoas(lista_pessoas)
        elif opcao == "3":
            remover_pessoa(lista_pessoas)
        elif opcao == "4":
            modificar_pessoa(lista_pessoas)
        elif opcao == "5":
            print("Saindo...")
            break
        else:
            print("Opção Inválida! Tente novamente.")

menu_principal()
