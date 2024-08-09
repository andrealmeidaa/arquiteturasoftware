from abc import ABC, abstractmethod

class ProductA(ABC):
    @abstractmethod
    def operation(self):
        pass
class ConcreteProductA1(ProductA):
    def operation(self):
       return "ProductA1"
class ConcreteProductA2(ProductA):
    def operation(self):
       return "ProductA2"
    
class ProductB(ABC):
    @abstractmethod
    def operation2(self):
        pass
class ConcreteProductB1(ProductB):
    def operation2(self):
        return "ProductB1"
class ConcreteProductB2(ProductB):
    def operation2(self):
        return "ProductB2"

class AbstractFactory(ABC):
    @abstractmethod
    def create_product_a(self) -> ProductA:
        pass

    @abstractmethod
    def create_product_b(self) -> ProductB:
        pass

class ConcreteFactoryA(AbstractFactory):
    def create_product_a(self) -> ProductA:
        return ConcreteProductA1()

    def create_product_b(self) -> ProductB:
        return ConcreteProductB1()

class ConcreteFactoryB(AbstractFactory):
    def create_product_a(self) -> ProductA:
        return ConcreteProductA2()

    def create_product_b(self) -> ProductB:
        return ConcreteProductB2()



# Exemplo de uso da Fábrica Abstrata
factory = ConcreteFactoryA()
product_a = factory.create_product_a()
product_b = factory.create_product_b()

print(product_a.operation())
print(product_b.operation())

#Segunda Fábrica

factoryB=ConcreteFactoryB()
product_a = factoryB.create_product_a()
product_b = factoryB.create_product_b()
print(product_a.operation2())
print(product_b.operation2())