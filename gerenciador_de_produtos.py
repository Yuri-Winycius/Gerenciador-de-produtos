from typing import Dict, List
from produtos import Produto

# Classe que gerencia o sistema de cadastro de produtos
class GerenciadorDeProdutos:
    def __init__(self) -> None:
        self.produtos: Dict[int, Produto] = {}
        self.proximo_id: int = 1

    # Função para adicionar um produto
    def adicionar_produto(self, nome: str, preco: float, categoria: str) -> None:
        produto = Produto(nome, preco, categoria)
        self.produtos[self.proximo_id] = produto
        print(f"Produto '{nome}' adicionado com sucesso! ID: {self.proximo_id}")
        self.proximo_id += 1

    # Função para remover um produto pelo ID
    def remover_produto(self, id_produto: int) -> None:
        if id_produto in self.produtos:
            removido = self.produtos.pop(id_produto)
            print(f"Produto '{removido.nome}' removido com sucesso!")
        else:
            print("ID do produto não encontrado!")

    # Função para listar todos os produtos
    def listar_produtos(self) -> None:
        if self.produtos:
            print("\nLista de Produtos:")
            for id_produto, produto in self.produtos.items():
                print(f"ID: {id_produto} - {produto}")
        else:
            print("Nenhum produto cadastrado.")