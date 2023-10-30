from conta_bancaria import ContaBancaria

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
