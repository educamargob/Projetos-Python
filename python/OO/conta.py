class Conta:

    def __int__(self, numero, titular, saldo, limite = 1000):
        print("Construindo objeto ...")
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

    def extrato(self):
        print(f"Saldo {self.saldo} do titular {self.titular}")

    def deposita(self, valor):
        self.saldo += valor

    def saca(self, valor):
        self.saldo -= valor