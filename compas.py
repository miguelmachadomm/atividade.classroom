lista_compras = []

def adicionar_item(item):
    lista_compras.append(item)
    print(f"{item} foi adicionado à lista.")

def remover_item(item):
    if item in lista_compras:
        lista_compras.remove(item)
        print(f"{item} foi removido da lista.")
    else:
        print(f"{item} não está na lista.")

def editar_item(item_antigo, item_novo):
    if item_antigo in lista_compras:
        index = lista_compras.index(item_antigo)
        lista_compras[index] = item_novo
        print(f"{item_antigo} foi substituído por {item_novo}.")
    else:
        print(f"{item_antigo} não está na lista.")

def listar_itens():
    if len(lista_compras) > 0:
        print("Itens na lista de compras:")
        for item in lista_compras:
            print(item)
    else:
        print("A lista de compras está vazia.")

while True:
    print("\nMenu:")
    print("1 - Adicionar item")
    print("2 - Remover item")
    print("3 - Editar item")
    print("4 - Listar itens")
    print("5 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        item = input("Digite o item que deseja adicionar: ")
        adicionar_item(item)
    elif opcao == "2":
        item = input("Digite o item que deseja remover: ")
        remover_item(item)
    elif opcao == "3":
        item_antigo = input("Digite o item que deseja editar: ")
        item_novo = input("Digite o novo valor do item: ")
        editar_item(item_antigo, item_novo)
    elif opcao == "4":
        listar_itens()
    elif opcao == "5":
        print("Saindo...")
        break
    else:
        print("Opção inválida. Tente novamente.")