class Pessoa:
    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone

class PessoaFisica(Pessoa):
    def __init__(self, nome, telefone, cpf):
        super().__init__(nome, telefone)
        self.cpf = cpf

class PessoaJuridica(Pessoa):
    def __init__(self, nome, telefone, cnpj):
        super().__init__(nome, telefone)
        self.cnpj = cnpj

# Criação da classe pessoa, utilizando herança Pessoa PODERÁ ser Fisica OU juridica