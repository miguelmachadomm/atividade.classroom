class ContaBancaria:
    def _init_ (self, titular):
        self.titular = titular
        self.saldo = 0

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f'Depósito de R${valor:.2f} realizado com sucesso.')
        else:
            print('O valor do depósito deve ser maior que zero.')

    def sacar(self, valor):
        if valor > 0:
            if valor <= self.saldo:
                self.saldo -= valor
                print(f'Saque de R${valor:.2f} realizado com sucesso.')
            else:
                print('Saldo insuficiente para realizar o saque.')
        else:
            print('O valor do saque deve ser maior que zero.')

    def ver_saldo(self):
        print(f'Saldo atual da conta de {self.titular}: R${self.saldo:.2f}')

# Criando um objeto da classe ContaBancaria
conta = ContaBancaria("João")

# Fazendo alguns depósitos e saques para testar a funcionalidade
conta.depositar(1000)
conta.sacar(500)
conta.ver_saldo()

conta.depositar(200)
conta.sacar(800)
conta.ver_saldo()