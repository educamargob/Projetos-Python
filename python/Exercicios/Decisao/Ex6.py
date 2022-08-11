def apresentacao():
    valor = int(input("Digite um valor: "))
    valorstr = str(valor)
    imprime_casas(valor,valorstr)

def imprime_casas(valor, valorstr):
    if(valor < 10):
        print(f"Unidade: {valorstr[0]}")
    if(valor < 100 and valor >= 10):
        print(f"Unidade: {valorstr[0]}\n "
              f"Dezena: {valorstr[1]}")
    if(valor < 1000 and valor >= 100):
        print(f"Unidade: {valorstr[0]}\n"
              f"Dezena: {valorstr[1]}\n"
              f"Milhar: {valorstr[2]}")

if __name__ == "__main__" :
    apresentacao()
