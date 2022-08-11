def apresentacao():
    salario_atual = int(input("Digite o salário do colaborador: "))
    verifica_aumento(salario_atual)

def verifica_aumento(salario):
    if salario <= 280.00:
        per_aumento = 0.2
        aumento = salario * per_aumento
        salario_final = salario + aumento
    elif salario > 280.00 and salario <= 700.00:
        per_aumento = 0.15
        aumento = salario * per_aumento
        salario_final = salario + aumento
    elif salario > 700.00 and salario < 1500.00:
        per_aumento = 0.1
        aumento = salario * per_aumento
        salario_final = salario + aumento
    else:
        per_aumento = 0.05
        aumento = salario * per_aumento
        salario_final = salario + aumento
    print(f"Salario antes do reajuste: {salario}\n"
          f"Percentual de aumento: {per_aumento*100}%\n"
          f"Valor de aumento: {aumento}\n"
          f"Salário após aumento: {salario_final}")

if __name__ == "__main__":
    apresentacao()
