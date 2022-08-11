n1 = int(input("n1: "))
n2 = int(input("n2: "))
n3 = int(input("n3: "))

maior = n1;
menor = n1;

if(menor > n2):
    menor = n2
if(menor > n3):
    menor = n3

if(maior < n2):
    maior = n2
if(maior < n3):
    maior = n3

print(f"Maior {maior}")
print(f"Menor {menor}")
