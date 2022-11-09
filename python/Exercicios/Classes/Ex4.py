"""
Classe Pessoa: Crie uma classe que modele uma pessoa:

Atributos: nome, idade, peso e altura
Métodos: Envelhercer, engordar, emagrecer, crescer. Obs: Por padrão, a cada ano que nossa pessoa envelhece, sendo a idade dela menor que 21 anos, ela deve crescer 0,5 cm.
"""

class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def crescer(self, ganho_altura):
        self.altura += ganho_altura

    def envelhecer(self):
        if self.idade < 21:
            self.crescer(0.5)
        self.idade += 1
    
    def engordar(self, ganho_peso):
        self.peso += ganho_peso
    

    