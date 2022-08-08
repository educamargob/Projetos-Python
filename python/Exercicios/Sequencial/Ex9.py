import math
area = float(input("Área a ser pintada: "))
litros = area / 6
latas = math.ceil(litros / 18)
galoes = math.ceil(litros / 3.6)
precolata = latas * 80.00
preco_galao = galoes * 25.00
print(f"Comprando apenas latas de 18 litros, serão necessaria(s) {latas} Lata(s) com o valor de R$ {precolata}")
print(f"Comprando apenas latas de 3,6 litros, serão necessaria(s) {galoes} Lata(s) com o valor de R$ {precogalao}")
#print(f"Comprando apenas latas de 18 litros, serão necessaria(s) {galoes18} Lata(s) com o valor de R$ {preco18}")