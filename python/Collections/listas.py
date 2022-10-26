idades = [39, 30, 27, 18]

print(len(idades))
print(idades[0])

idades.append(10)

for idade in idades:
    print(idade)

idades.remove(30)

print(idades)

if 18 in idades:
    idades.remove(18)

print(idades)

idades.insert(0, 20)
print(idades)


idades.extend([27, 19])
print(idades)

for idade in idades:
    print(idade + 1)

idades_ano_que_vem = []
for idade in idades:
    idades_ano_que_vem.append(idade+1)
print(idades_ano_que_vem)

print([(idade+1) for idade in idades])

print([(idade) for idade in idades if idade > 21])