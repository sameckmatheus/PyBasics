from datetime import datetime


class ContaBancaria:
    def __init__(self, numero, nome, tipo):
        self.numero = numero
        self.saldo = 0
        self.status = False
        self.tipo = tipo
        self.limite = 0
        self.nome = nome

    def depositar(self, valor):
        if self.status:
            self.saldo += valor
            horario_transacao = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
            return (f'====================================================================================\n'
                    f'Depósito de R$ {valor:.2f} foi realizado com sucesso para a conta: {self.numero}. \n'
                    f'Horário do depósito: {horario_transacao}\n')
        else:
            return f'Não foi possível realizar o depósito, pois a conta: {self.numero} parece estar inavtiva...'

    def sacar(self, valor):
        if self.status:
            if self.saldo >= valor:
                self.saldo -= valor
                horario_transacao = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
                return (f'Saque de R$ {valor:.2f} foi realizado com sucesso para a conta: {self.numero}. \n'
                        f'Horário do saque: {horario_transacao}')

            elif valor > self.saldo:
                saque = (self.saldo + self.limite) - valor
                horario_transacao = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
                return (f'Saque de R$ {valor:.2f} foi realizado com sucesso para a conta: {self.numero}. \n'
                        f'Horário do saque: {horario_transacao}')

            else:
                return f'Saldo para saque de R$ {valor:.2f} insuficiente.'
        else:
            return f'Não foi possível realizar o saque, pois a conta: {self.numero} parece estar inavtiva...'

    def ativar_conta(self):
        if not self.status:
            self.status = True
            return f'Atenção, sua conta está avita!'

    def ativar_limite(self):
        if self.limite == 0:
            if self.status:
                self.limite = 1000
                return (f'\nParabéns, você foi contemplado!\n'
                        f'seu novo limite de conta, é: {self.limite}')
            else:
                return 'Você ainda não tem um limite de conta...'

    def verificar_saldo(self):
        if self.status:
            return (f'\nO seu saldo atual, é: R$ {self.saldo:.2f}\n'
                    f'====================================================================================')
        else:
            return f'Não possível verificar o saldo da conta: {self.numero}, pois, a mesma está inativa.'
