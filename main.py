"""Ponto de entrada do sistema de controle de estoque e vendas."""

from estoque import menu_estoque
from produtos import menu_produtos
from vendas import menu_vendas


def exibir_menu_principal():
    """Exibe as opções disponíveis no menu principal."""
    print("\n=== CONTROLE DE ESTOQUE E VENDAS ===")
    print("1 - Produtos")
    print("2 - Estoque")
    print("3 - Vendas")
    print("0 - Sair")


def main():
    """Cria os dados compartilhados e mantém o menu principal em execução."""
    produtos = []
    movimentacoes = []
    vendas = []

    while True:
        exibir_menu_principal()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            menu_produtos(produtos)
        elif opcao == "2":
            menu_estoque(produtos, movimentacoes)
        elif opcao == "3":
            menu_vendas(produtos, movimentacoes, vendas)
        elif opcao == "0":
            print("Programa encerrado. Os dados mantidos em memória foram perdidos.")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
