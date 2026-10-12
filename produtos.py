"""Funções imperativas para gerenciar produtos em memória."""

from decimal import Decimal, InvalidOperation


def ler_codigo(mensagem):
    """Lê um código textual não vazio."""
    while True:
        codigo = input(mensagem).strip()
        if codigo:
            return codigo
        print("O código não pode ficar vazio.")


def ler_nome(mensagem):
    """Lê um nome não vazio."""
    while True:
        nome = input(mensagem).strip()
        if nome:
            return nome
        print("O nome não pode ficar vazio.")


def ler_inteiro_nao_negativo(mensagem):
    """Lê um número inteiro maior ou igual a zero."""
    while True:
        texto = input(mensagem).strip()
        try:
            valor = int(texto)
            if valor >= 0:
                return valor
        except ValueError:
            pass
        print("Valor inválido. Digite um número inteiro maior ou igual a zero.")


def ler_preco_centavos(mensagem):
    """Lê um valor em reais e o converte exatamente para centavos."""
    while True:
        texto = input(mensagem).strip().replace(",", ".")
        try:
            valor_reais = Decimal(texto)
            valor_centavos = valor_reais * 100
            if (
                valor_reais.is_finite()
                and valor_reais > 0
                and valor_centavos == valor_centavos.to_integral_value()
            ):
                return int(valor_centavos)
        except (InvalidOperation, ValueError):
            pass
        print("Preço inválido. Informe um valor positivo com até duas casas decimais.")


def formatar_reais(valor_centavos):
    """Formata um valor inteiro em centavos para exibição em reais."""
    reais = valor_centavos // 100
    centavos = valor_centavos % 100
    return f"R$ {reais},{centavos:02d}"


def buscar_produto(produtos, codigo):
    """Retorna o produto com o código informado ou None se não existir."""
    for produto in produtos:
        if produto["codigo"] == codigo:
            return produto
    return None


def cadastrar_produto(produtos):
    """Solicita os dados e adiciona um produto com quantidade inicial zero."""
    print("\n--- CADASTRAR PRODUTO ---")
    codigo = ler_codigo("Código: ")

    if buscar_produto(produtos, codigo) is not None:
        print("Já existe um produto com esse código.")
        return

    nome = ler_nome("Nome: ")
    preco_centavos = ler_preco_centavos("Preço: R$ ")
    estoque_minimo = ler_inteiro_nao_negativo("Estoque mínimo: ")
    produtos.append(
        {
            "codigo": codigo,
            "nome": nome,
            "preco_centavos": preco_centavos,
            "quantidade": 0,
            "estoque_minimo": estoque_minimo,
        }
    )
    print("Produto cadastrado com sucesso. Quantidade inicial: 0.")


def exibir_produto(produto):
    """Mostra um produto de forma padronizada."""
    print(
        f"Código: {produto['codigo']} | "
        f"Nome: {produto['nome']} | "
        f"Preço: {formatar_reais(produto['preco_centavos'])} | "
        f"Quantidade: {produto['quantidade']} | "
        f"Estoque mínimo: {produto['estoque_minimo']}"
    )


def listar_produtos(produtos):
    """Exibe todos os produtos cadastrados."""
    print("\n--- PRODUTOS CADASTRADOS ---")
    if not produtos:
        print("Nenhum produto cadastrado.")
        return

    for produto in produtos:
        exibir_produto(produto)


def consultar_produto(produtos):
    """Localiza e exibe um produto pelo código."""
    print("\n--- CONSULTAR PRODUTO ---")
    codigo = ler_codigo("Código: ")
    produto = buscar_produto(produtos, codigo)

    if produto is None:
        print("Produto não encontrado.")
    else:
        exibir_produto(produto)


def editar_produto(produtos):
    """Altera nome, preço e estoque mínimo de um produto existente."""
    print("\n--- EDITAR PRODUTO ---")
    codigo = ler_codigo("Código do produto: ")
    produto = buscar_produto(produtos, codigo)

    if produto is None:
        print("Produto não encontrado.")
        return

    produto["nome"] = ler_nome("Novo nome: ")
    produto["preco_centavos"] = ler_preco_centavos("Novo preço: R$ ")
    produto["estoque_minimo"] = ler_inteiro_nao_negativo("Novo estoque mínimo: ")
    print("Produto atualizado com sucesso.")


def excluir_produto(produtos):
    """Remove um produto existente após confirmação."""
    print("\n--- EXCLUIR PRODUTO ---")
    codigo = ler_codigo("Código do produto: ")
    produto = buscar_produto(produtos, codigo)

    if produto is None:
        print("Produto não encontrado.")
        return

    exibir_produto(produto)
    confirmacao = input("Confirmar exclusão? (s/n): ").strip().lower()
    if confirmacao == "s":
        produtos.remove(produto)
        print("Produto excluído com sucesso.")
    else:
        print("Exclusão cancelada.")


def exibir_menu_produtos():
    """Exibe as operações disponíveis para produtos."""
    print("\n=== PRODUTOS ===")
    print("1 - Cadastrar")
    print("2 - Listar")
    print("3 - Consultar por código")
    print("4 - Editar")
    print("5 - Excluir")
    print("0 - Voltar")


def menu_produtos(produtos):
    """Mantém o submenu de produtos em execução; não retorna valor."""
    while True:
        exibir_menu_produtos()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            cadastrar_produto(produtos)
        elif opcao == "2":
            listar_produtos(produtos)
        elif opcao == "3":
            consultar_produto(produtos)
        elif opcao == "4":
            editar_produto(produtos)
        elif opcao == "5":
            excluir_produto(produtos)
        elif opcao == "0":
            break
        else:
            print("Opção inválida. Tente novamente.")
