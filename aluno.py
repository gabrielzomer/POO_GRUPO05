class Aluno:

    def __init__(self, nome, cpf, email, ano_nascimento):
        self._nome = nome
        self._cpf = cpf
        self._email = email
        self._ano_nascimento = ano_nascimento

    
    def calcula_idade(self, ano_atual):
        idade = ano_atual - self._ano_nascimento
        return idade