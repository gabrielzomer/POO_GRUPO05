from pessoa import PessoaFisica, PessoaJuridica
from aluno import Aluno
from curso import Curso
from inscricao import Inscricao

tipo_pessoa = input("Digite '1' para Pessoa Física ou '2' para Pessoa Jurídica: ")

# Info pessoa
nome = input("Digite o nome: ")
telefone = input("Digite o telefone: ")

if tipo_pessoa == '1':
    cpf = input("Digite o CPF: ")
    pessoa = PessoaFisica(nome, telefone, cpf)
else:
    cnpj = input("Digite o CNPJ: ")
    pessoa = PessoaJuridica(nome, telefone, cnpj)

# Transforma em aluno.
matricula = input("Crie uma Matricula: ")
aluno = Aluno(matricula)

# Cadastrar o curso
nome_curso = input("Digite o nome do curso: ")
carga_horaria = int(input("Digite a carga horária do curso: "))
preco = float(input("Digite o preço do curso: "))
curso = Curso(nome_curso, carga_horaria, preco)

# Vincule o aluno ao curs
inscricao = Inscricao(aluno, curso)

print("\n\n\nInscrição realizada:")
print(f"Nome do Aluno: {pessoa.nome}")
print(f"Matricula: {aluno._matricula}")
print(f"Curso Inscrito: {curso.nome}")
