"""
Faça um programa que simule um lançamento de dados. Lance o dado 100 vezes e armazene os resultados em um vetor . Depois, mostre quantas vezes cada valor foi conseguido. Dica: use um vetor de contadores(1-6) e uma função para gerar numeros aleatórios, simulando os lançamentos dos dados.
"""
import random
lados = [1, 2, 3, 4, 5, 6]
resultados = []
for i in range (100):
    random.shuffle(lados)
    lado = lados[0]
    resultados.append(lado)

print(resultados)