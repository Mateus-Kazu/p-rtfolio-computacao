
class ContaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor
        print(f"Depósito de R${valor:.2f} realizado com sucesso.")

    def sacar(self, valor):
        if valor > self.saldo:
            print("Saldo insuficiente.")
        else:
            self.saldo -= valor
            print(f"Saque de R${valor:.2f} realizado com sucesso.")

    def consultar_saldo(self):
        print(f"Saldo atual: R${self.saldo:.2f}")

# Exemplo de uso
conta = ContaBancaria("João")
conta.depositar(1000)
conta.sacar(200)
conta.consultar_saldo()
