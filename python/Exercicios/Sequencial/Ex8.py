salhora = float(input("Quanto você ganha por hora? \n"))
ir = salhora * 0.11
inss = salhora * 0.08
sind = salhora * 0.05
salliquido = salhora - ir - inss - sind
print(f"+ Salário Bruto : R$ {salhora}\n"
      f"- IR (11%) : {ir}\n"
      f"- INSS (8%) : {inss}\n"
      f"- Sindicato (8%) : {sind}\n"
      f"= Salário Liquido : {salliquido}")