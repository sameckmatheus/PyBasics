from conta_bancaria import ContaBancaria

Conta1 = ContaBancaria(7474, "Roberto", "corrente")
print(Conta1.ativar_conta())
print(Conta1.depositar(200))
print(Conta1.sacar(20))
print(Conta1.verificar_saldo())

Conta2 = ContaBancaria(9898, "João", "poupanca")
Conta2.status = False
print(Conta2.depositar(200))
print(Conta2.sacar(40))
print(Conta2.verificar_saldo())
