from conta_bancaria import ContaBancaria

Conta1 = ContaBancaria(747489, "Roberto", "corrente")
print(Conta1.ativar_conta())
print(Conta1.depositar(200))
print(Conta1.sacar(220))
print(Conta1.verificar_saldo())

Conta2 = ContaBancaria(989823, "João", "poupanca")
#  Conta2.status = False
print(Conta2.ativar_conta())
print(Conta2.depositar(200))
print(Conta2.sacar(1000))
print(Conta2.verificar_saldo())
