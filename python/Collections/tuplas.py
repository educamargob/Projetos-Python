from tkinter import commondialog


class contaCorrente:
    def __init__(self, codigo):
        self.codigo = codigo
        self.saldo = 0
    
    def deposita(self, valor):
        self.saldo += valor

    def __str__(self):
        return "[>>Codigo {} saldo {} <<]".format(self.codigo, self.saldo)


conta_do_gui = contaCorrente(15)
conta_do_gui.deposita(500)
print(conta_do_gui)

conta_da_dani = contaCorrente(52213)
conta_da_dani.deposita(1000)
print(conta_da_dani)

contas = [conta_da_dani, conta_do_gui]
for conta in contas:
    print(conta)


def deposita_para_todas(contas):
    for conta in contas:
        conta.deposita(100)

contas = [conta_da_dani, conta_do_gui]
deposita_para_todas(contas)
print(contas[0], contas[1])

#Tuplas
guilherme = ('Guilherme', 37, 19811)
daniela = ('Daniela', 37, 19811)

usuarios = [guilherme, daniela]