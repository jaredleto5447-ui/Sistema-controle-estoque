import json
def adicionar_produto(produtos, nome, precos, quantidades):
    produto = {"nome": nome, "preco": preco, "quantidade": quantidade}

    produtos.append(produto)
    print(f"{nome} foi adicionado com sucesso!")

def mostrar_produtos(produtos):
            print("\n --- ESTOQUE ---")

            if len(produtos) == 0:
                print("nenhum produto cadastrado")
            else:
                for produto in produtos:
                 print(f"nome: {produto['nome']}")
                 print(f"preco: R$ {produto['preco']:.2f}")
                 print(f"quantidade {produto['quantidade']}")


print("------------------")

def remover_produto(produtos, nome):
    for produto in produtos:
        if produto["nome"] == nome:
            produtos.remove(produto)
            print("produto removido com sucesso!")

            return
    print("produto nao encontrado")


def calcular_valor_estoque(produtos):
    total = 0

    for produto in produtos:
        valor = produto["preco"] * produto["quantidade"]
        total += valor

    print(f"valor total do estoque: R$ {total:.2f}")


def atualizar_quantidade(produtos, nome, nova_quantidade):
    for produto in produtos:
        if produto["nome"].lower() == nome.lower():
            produto["quantidade"] = nova_quantidade
            print("quantidade atualizada com sucesso! ")
            return
        print("produto nao encontrado.")


def buscar_produto(produtos, nome):
    for produto in produtos:
        if produto["nome"].lower() == nome.lower():
            print("\n=== PRODUTO ENCONTRADO ===")
            print(f"nome:{produto['nome']}")
            print(f"preco:{produto['preco']:.2f}")
            print(f"quantidade:{produto['quantidade']}")
            return
        print("produto nao encontrado.")


def vender_produtos(produtos, nome, quantidade_vendida):
    for produto in produtos:
        if produto["nome"].lower() == nome.lower():
            if produto["quantidade"] >= quantidade_vendida:
                total = produto["preco"] * quantidade_vendida
                produto["quantidade"] -= quantidade_vendida


                print("\n===== VENDA REALIZADA =====")
                print(f"produto:{produto['nome']}")
                print(f"quantidade vendida: {quantidade_vendida}")
                print(f"valor total: R$ {total:.2f}")
                print(f"estoque restante: {produto['quantidade']}")

            else:
                print("estoque insuficiente!")

            return

            print("produto nao encontrado.")


def salvar_estoque(produtos):
    with open("estoque.json", "w", encoding="utf-8")as arquivo:
        json.dump(produtos, arquivo, indent=4, ensure_ascii=False)
        print("estoque salvo com sucesso!")


produtos = []

while True:
    print("1 - adicionar produto")
    print("2 - mostrar produto")
    print("3 - remover produto")
    print("4 - calcular valor estoque")
    print("5 - atualizar quantidade")
    print("6 - buscar produto")
    print("7 - registrar venda")
    print("0 - sair")

    opcao = input("escolha uma opcao: ")

    if opcao == "1":
        nome = input("nome: ")

        try:
            preco = float(input("preco:"))
            quantidade = int(input("quantidade:"))
            adicionar_produto(produtos, nome, preco, quantidade)

        except ValueError:
            print("error: digite valores numericos validos!")

    elif opcao == "2":
        mostrar_produtos(produtos)

    elif opcao == "3":
        nome = input("produto para remover: ")
        remover_produto(produtos, nome)

    elif opcao == "4":
        calcular_valor_estoque(produtos)

    elif opcao == "5":
        nome = input("nome do produto: ")
        nova_quantidade = int(input("quantidade: "))
        atualizar_quantidade(produtos, nome, nova_quantidade)
        salvar_estoque(produtos)

    elif opcao == "6":
        nome = input("digite o nome do produto: ")
        buscar_produto(produtos, nome)

    elif opcao == "7":
        nome = input("nome do produto: ")

        try:
            quantidade = int(input("quantidade vendida: "))
            vender_produtos(produtos, nome, quantidade)

        except ValueError:
              print("informe uma quantidade numerica !")

        vender_produtos(produtos, nome, quantidade)


    elif opcao == "0":
     print("sair")

     break


else:
    print("opcao invalida")