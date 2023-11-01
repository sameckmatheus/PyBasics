#  =============================================================================================  #

from datetime import datetime


class ContaBancaria:
    def __init__(self, numero, nome, tipo):
        self.numero = numero
        self.saldo = 0
        self.status = False
        self.tipo = tipo
        self.nome = nome

    def depositar(self, valor):
        if self.status:
            self.saldo += valor
            horario_transacao = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
            return (f'====================================================================================\n'
                    f'Depósito de R$ {valor:.2f} foi realizado com sucesso para a conta: {self.numero}. \n'
                    f'Horário do depósito: {horario_transacao}\n')
        else:
            return f'Não foi possível realizar o depósito, pois a conta: {self.numero} parece estar inativa...'

    def sacar(self, valor):
        if self.status:
            if self.verificar_saldo_suficiente(valor):
                self.saldo -= valor
                horario_transacao = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
                return (f'Saque de R$ {valor:.2f} foi realizado com sucesso para a conta: {self.numero}. \n'
                        f'Horário do saque: {horario_transacao}')
            else:
                raise SaldoInsuficienteError(f'Saldo para saque de R$ {valor:.2f} insuficiente.')
        else:
            return f'Não foi possível realizar o saque, pois a conta: {self.numero} parece estar inativa...'

    def ativar_conta(self):
        if not self.status:
            self.status = True
            return f'Atenção, sua conta está avita!'

    def verificar_saldo(self):
        if self.status:
            return (f'\nO seu saldo atual, é: R$ {self.saldo:.2f}\n'
                    f'====================================================================================')
        else:
            return f'Não possível verificar o saldo da conta: {self.numero}, pois, a mesma está inativa.'

    def verificar_saldo_suficiente(self, valor):
        return self.saldo >= valor


class LimiteConta:
    LIMITE_PADRAO_CONTA_CORRENTE = 1000
    LIMITE_PADRAO_CONTA_POUPANCA = 500

    def __init__(self, tipo_conta):
        self.tipo_conta = tipo_conta
        self.limite = self.definir_limite_padrao()

    def definir_limite_padrao(self):
        if self.tipo_conta == 'corrente':
            return LimiteConta.LIMITE_PADRAO_CONTA_CORRENTE
        elif self.tipo_conta == 'poupanca':
            return LimiteConta.LIMITE_PADRAO_CONTA_POUPANCA
        else:
            return 0


class Transacao:
    def __init__(self, valor, tipo_transacao):
        self.valor = valor
        self.tipo_transacao = tipo_transacao
        self.horario_transacao = datetime.now().strftime('%d/%m/%Y %H:%M:%S')


class SaldoInsuficienteError(Exception):
    pass
#  =============================================================================================  #
