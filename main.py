#Trabalho Projeto Integrador
#Professora: Camila Carolina Salgueiro Serrão
#Maria Luiza Rodrigues Da silva;
#Ana Luisa Esteves Oliveira;
#jennifer Rebeca;
#Tamily fernanda.

from classe import *
from cadastro import *
equipes = {}
print("Sistema de Cadastro")
print("1. Cadastrar Capitão de Equipe")
print("2. Cadastrar Aluno")
print("3. Exibir Cadastro")
opcao = int(input("Opção: "))

if opcao == 1:
  curso_capitao = input('Digite seu curso: ')
  nome_capitao = input('Digite seu Nome Completo: ')
  email_capitao = input('Digite seu e-mail: ')
  num_matricula_capitao = input('Digite seu número de matrícula: ')
  data_nascimento_capitao = input('Digite a sua data de nascimento(00/00/00): ')
  num_camisa_capitao = input('Digite o número da sua camisa: ')
  capitao = CapitaoEquipe(nome_capitao, email_capitao, num_matricula_capitao, curso_capitao, data_nascimento_capitao, num_camisa_capitao)
  cadastrar_capitao(curso_capitao, nome_capitao,email_capitao, num_matricula_capitao, data_nascimento_capitao, num_camisa_capitao)
elif opcao == 2:
  nome_aluno = input('Digite seu Nome Completo: ')
  curso_aluno = input('Digite seu curso: ')
  email_aluno = input('Digite seu e-mail: ')
  num_matricula_aluno = input('Digite seu número de matrícula: ')
  data_nascimento_aluno = input('Digite a sua data de nascimento(00/00/00): ')
  num_camisa_aluno = input('Digite o número da sua camisa: ')
  aluno = AlunoEquipe(nome_aluno,curso_aluno, email_aluno, num_matricula_aluno, data_nascimento_aluno,num_camisa_aluno)
  cadastrar_aluno(nome_aluno,curso_aluno, email_aluno, num_matricula_aluno, data_nascimento_aluno, num_camisa_aluno)
elif opcao == 3:
    exibir_cadastro()
    exibir_cadastro2()