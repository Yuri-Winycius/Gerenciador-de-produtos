from typing import Dict, List
from produtos import Produto
from gerenciador_de_produtos import GerenciadorDeProdutos

# Função principal para interagir com o sistema
def main() -> None:
    gerenciador = GerenciadorDeProdutos()

    while True:
        print("\n=== Sistema de Cadastro de Produtos ===")
        print("1. Adicionar produto")
        print("2. Remover produto")
        print("3. Listar produtos")
        print("4. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            nome = input("Digite o nome do produto: ")
            preco = float(input("Digite o preço do produto: "))
            categoria = input("Digite a categoria do produto: ")
            gerenciador.adicionar_produto(nome, preco, categoria)
        
        elif opcao == '2':
            id_produto = int(input("Digite o ID do produto a ser removido: "))
            gerenciador.remover_produto(id_produto)
        
        elif opcao == '3':
            gerenciador.listar_produtos()
        
        elif opcao == '4':
            print("Saindo do sistema...")
            break
        
        else:
            print("Opção inválida, tente novamente.")


if __name__ == "__main__":
    main()
