class Conta:
    def __init__(self, numero, titular, saldo, limite = 1000.00):
        print("Construindo objeto ...")
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print(f"Saldo {self.__saldo} do titular {self.__titular}")

    def deposita(self, valor):
        self.__saldo += valor

    def __pode_sacar(self):
        valor_disponivel = self.__saldo + self.__limite
        return valor_a_sacar <= valor_disponivel

    def saca(self, valor):
        if(self.__pode_sacar(valor)):
            self.__saldo -= valor
        else:
            print(f"O valor {valor} passou o limite")

    def transferir(self, valor, destino):
        self.saca(valor)  ##Saca valor da própria conta
        destino.deposita(valor)

    def get_saldo(self):
        return self.__saldo

    def get_titular(self):
        return self.__titular

    @property
    def saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def set_limite(self, limite):
        self.__limite = limite

    @staticmethod
    def codigo_banco():
        return "001"

    @staticmethod
    def codigos_bancos():
        return {'BB':'001', 'Caixa':'104', 'Bradesco':'237'}






