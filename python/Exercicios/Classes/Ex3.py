"""
Classe Retangulo: Crie uma classe que modele um retangulo:

Atributos: LadoA, LadoB (ou Comprimento e Largura, ou Base e Altura, a escolher)
Métodos: Mudar valor dos lados, Retornar valor dos lados, calcular Área e calcular Perímetro;
Crie um programa que utilize esta classe. Ele deve pedir ao usuário que informe as medidades de um local. Depois, deve criar um objeto com as medidas e calcular a quantidade de pisos e de rodapés necessárias para o local.
"""
class retangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    def muda_tamanho_lados(self, base, altura):
        self.base = base
        self.altura = altura
    
    def valor_lados(self):
        return f"Base: {self.base}, Altura: {self.altura}"
    
    def calcula_area(self):
        area = self.base * self.altura
        return area
    
    def calcula_perimetro(self):
        perimetro = (self.base * 2) + (self.altura * 2)
        return perimetro

def executa():
    print("---------Retângulo---------")
    base = float(input("Favor digite o valor da base: "))
    altura = float(input("Favor digite o valor da altura: "))
    retangulo = retangulo(base,altura)
    print(retangulo.calcula_perimetro())

if(__name__ == "__main__"):
    executa()
