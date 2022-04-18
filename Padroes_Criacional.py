# Exemplo conceitual

from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any


class Builder(ABC):
    """
    A interface Builder especifica métodos para a criação das diferentes partes do
    os objetos do Produto.
    """

    @property
    @abstractmethod
    def product(self) -> None:
        pass

    @abstractmethod
    def produce_part_a(self) -> None:
        pass

    @abstractmethod
    def produce_part_b(self) -> None:
        pass

    @abstractmethod
    def produce_part_c(self) -> None:
        pass


class ConcreteBuilder1(Builder):
    """
    As classes de Construtor de concreto seguem a interface do Construtor e fornecem
    implementações específicas das etapas de construção. o programa pode ter
    várias variações de Construtores, implementadas de forma diferente.
    """

    def __init__(self) -> None:
        """
        Uma nova instância de construtor deve conter um objeto de produto em branco, que é
        utilizado na montagem posterior..
        """
        self.reset()

    def reset(self) -> None:
        self._product = Product1()

    @property
    def product(self) -> Product1:
        
        product = self._product
        self.reset()
        return product

    def produce_part_a(self) -> None:
        self._product.add("PartA1")

    def produce_part_b(self) -> None:
        self._product.add("PartB1")

    def produce_part_c(self) -> None:
        self._product.add("PartC1")


class Product1():
    
    def __init__(self) -> None:
        self.parts = []

    def add(self, part: Any) -> None:
        self.parts.append(part)

    def list_parts(self) -> None:
        print(f"Product parts: {', '.join(self.parts)}", end="")


class Director:
    """
    O Diretor é responsável apenas pela execução das etapas do edifício em um
    seqüência particular. É útil na produção de produtos de acordo com uma
    ordem ou configuração específica. Estritamente falando, a classe de Diretores é
    opcional, uma vez que o cliente pode controlar diretamente os construtores.
    """

    def __init__(self) -> None:
        self._builder = None

    @property
    def builder(self) -> Builder:
        return self._builder

    @builder.setter
    def builder(self, builder: Builder) -> None:
        """
        O Diretor trabalha com qualquer instância construtora que o código do cliente passe
        a ela. Desta forma, o código do cliente pode alterar o tipo final do novo
        produto montado.
        """
        self._builder = builder

    """
    O Diretor pode construir várias variações de produtos usando o mesmo
    etapas de construção.
    """

    def build_minimal_viable_product(self) -> None:
        self.builder.produce_part_a()

    def build_full_featured_product(self) -> None:
        self.builder.produce_part_a()
        self.builder.produce_part_b()
        self.builder.produce_part_c()


if __name__ == "__main__":
    """
     O código do cliente cria um objeto de construção, passa-o para o diretor e depois
    inicia o processo de construção. O resultado final é recuperado do
    objeto do construtor.
    """

    director = Director()
    builder = ConcreteBuilder1()
    director.builder = builder

    print("Standard basic product: ")
    director.build_minimal_viable_product()
    builder.product.list_parts()

    print("\n")

    print("Standard full featured product: ")
    director.build_full_featured_product()
    builder.product.list_parts()

    print("\n") # Seguir na Linha abaixo.

    # Remember, the Builder pattern can be used without a Director class.
    print("Custom product: ")
    builder.produce_part_a()
    builder.produce_part_b()
    builder.product.list_parts()
