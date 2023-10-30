class ContaBancaria:
    def __init__(self, numero, saldo, nome, status, tipo, limite):
        self.numero = numero
        self.saldo = saldo
        self.status = status
        self.tipo = tipo
        self.limite = limite
        self.nome = nome

    def depositar(self, valor):
        if self.status:
            self.saldo += valor
            print(f'Depósito de R$ {valor:.2f} foi realizado com sucesso para a conta: {self.numero}.')
        else:
            print(f'Não foi possível realizar o depósito, pois a conta: {self.numero} parece estar inavtiva...')

    def sacar(self, valor):
        if self.status:
            if self.saldo >= valor:
                self.saldo -= valor
                print(f'Saque de R$ {valor:.2f} foi realizado com sucesso para a conta: {self.numero}')
            else:
                print(f'Saldo para saque de R$ {valor:.2f} insuficiente.')
        else:
            print(f'Não foi possível realizar o saque, pois a conta: {self.numero} parece estar inavtiva...')

    def ativar_conta(self):
        if not self.status:
            self.status = True

    def verificar_saldo(self):
        if self.status:
            return f'O seu saldo atual, é: R$ {self.saldo:.2f}'
        else:
            print(f'Não possível verificar o saldo da conta: {self.numero}, pois, a mesma está inativa.')


Conta1 = ContaBancaria(1729, 5000, "Roberto", True, "Corrente", 5000)
Conta1.depositar(8000)
Conta1.sacar(5300)
Conta1.ativar_conta()
print(Conta1.verificar_saldo())
print()

Conta2 = ContaBancaria(9898, 5000, "João", True, "Corrente", 7000)
Conta2.depositar(3500)
Conta2.sacar(200)
Conta2.ativar_conta()
print(Conta2.verificar_saldo())
print()

Conta3 = ContaBancaria(6699, 5000, "Maria", False, "Corrente", 4000)
Conta3.depositar(600)
Conta3.sacar(100)
Conta3.ativar_conta()
print(Conta3.verificar_saldo())
