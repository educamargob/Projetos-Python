"""
Classe Quadrado: Crie uma classe que modele um quadrado:

Atributos: Tamanho do lado
Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área;
"""
class quadrado:
    def __init__(self, tamanho_lado):
        self.tamanho_lado = tamanho_lado
    
    def muda_tamanho_lado(self, tamanho_lado):
        self.tamanho_lado = tamanho_lado
    
    def valor_lado(self):
        return self.tamanho_lado
    
    def calcula_area(self):
        return self.tamanho_lado * self.tamanho_lado
