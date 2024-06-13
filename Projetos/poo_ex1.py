"""Criando um programa com POO, abstraindo uma bicicleta"""


class Bicicleta:
    """Criando a classe de uma bicicleta com atributos e métodos"""

    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
        self.correndo = False

    def buzinar(self):
        """Função que buzina"""
        print("BIBIBI!")

    def parar(self):
        """Função que muda o estado da bicicleta para
        'correndo = FALSE' se estiver andando"""
        if self.correndo:
            print("Parou!")
            self.correndo = False
        else:
            print("Já está parado")

    def correr(self):
        """Função que muda o estado da bicicleta para
        'correndo = TRUE' se estiver parada"""
        if self.correndo:
            print("Já está correndo")
        else:
            self.correndo = True
            print("Começando a correr!")


bike = Bicicleta("vermelha", "NIKE", 2023, 1200)
bike.buzinar()
bike.correr()
bike.correr()
bike.parar()
bike.parar()
