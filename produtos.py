# Classe que representa um produto
class Produto:
    def __init__(self, nome: str, preco: float, categoria: str) -> None:
        self.nome = nome
        self.preco = preco
        self.categoria = categoria

    def __str__(self) -> str:
        return f"Produto: {self.nome}, Preço: R${self.preco:.2f}, Categoria: {self.categoria}"
