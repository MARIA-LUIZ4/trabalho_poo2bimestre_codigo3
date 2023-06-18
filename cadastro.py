import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def obter_lista_membros():
  try:
   with open("alunos_cadastrados.txt", "r") as arquivo:
     linhas = arquivo.readlines()
     membros = []
     for linha in linhas:
      campos = linha.strip().split(",")
      nome_completo = campos[0].split(":")[1].strip()
      curso = campos[1].split(":")[1].strip()
      email = campos[2].split(":")[1].strip()
      num_matricula = campos[3].split(":")[1].strip()
      data_nascimento = campos[4].split(":")[1].strip()
      num_camisa = campos[5].split(":")[1].strip()
      membro = {
         "Nome Completo": nome_completo,
         "Curso": curso,
         "E-mail": email,
         "Número de Matrícula": num_matricula,
         "Data de Nascimento": data_nascimento,
         "Número da Camisa": num_camisa
      }
      membros.append(membro)
   return membros
  except FileNotFoundError:
    return []


def cadastrar_capitao(curso_capitao, nome_capitao, email_capitao, num_matricula_capitao, data_nascimento_capitao,num_camisa_capitao):
    with open("capitao_cadastro.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(f"Curso: {curso_capitao}, Nome Completo: {nome_capitao}, E-mail: {email_capitao}, Número de Matrícula: {num_matricula_capitao}, Data de nascimento: {data_nascimento_capitao}, Número da camisa: {num_camisa_capitao}\n")
    lista_membros = obter_lista_membros()
    membros_por_curso = {}

    for membro in lista_membros:
        curso_membro = membro['Curso']
        if curso_membro == curso_capitao:  # Verifica se o curso do membro é igual ao do capitão
         if curso_membro not in membros_por_curso:
             membros_por_curso[curso_membro] = []
             membros_por_curso[curso_membro].append(membro)

    capitao = {
          "Nome Completo": nome_capitao,
          "E-mail": email_capitao,
          "Número de Matrícula": num_matricula_capitao,
          "Data de Nascimento": data_nascimento_capitao,
          "Número da Camisa": num_camisa_capitao
    }

    if curso_capitao in membros_por_curso:
        membros_por_curso[curso_capitao].append(capitao)
    else:
        membros_por_curso[curso_capitao] = [capitao]

    lista_membros_formatada = []
    for curso, membros in membros_por_curso.items():
        membros_formatados = []
        for membro in membros:
            membro_str = f"Nome Completo: {membro['Nome Completo']}, Curso: {curso}, E-mail: {membro['E-mail']}, Número de Matrícula: {membro['Número de Matrícula']}, Data de Nascimento: {membro['Data de Nascimento']}, Número da Camisa: {membro['Número da Camisa']}"
            membros_formatados.append(membro_str)
        lista_membros_curso = "\n".join(membros_formatados)
        lista_membros_formatada.append(lista_membros_curso)
    lista_membros_str = "\n\n".join(lista_membros_formatada)
  #email de confirmação
    email_remetente = email_capitao
    email_destinatario = "projetoum8@gmail.com"
    senha_destinatario = "cswldlepklocmidl"
    mensagem = MIMEMultipart()
    mensagem["From"] = email_remetente
    mensagem["To"] = email_destinatario
    mensagem["Subject"] = "Confirmação de Cadastro"
    texto_email = f"""
    Olá, eu sou {nome_capitao},
      E estou finalizando o meu cadastro como capitão da minha equipe, na modalidade vôlei de areia!
      Segue abaixo a lista de membros inscritos na equipe:
      {lista_membros_str}
      E meu e-mail para caso algo não esteja de acordo:
      {email_capitao}
      Obrigado!
      Atenciosamente,
      {nome_capitao}
"""
    parte_texto = MIMEText(texto_email, "plain")
    mensagem.attach(parte_texto)
    try:
        servidor_smtp = smtplib.SMTP("smtp.gmail.com", 587)
        servidor_smtp.starttls()
        servidor_smtp.login(email_destinatario, senha_destinatario)
        servidor_smtp.sendmail(email_remetente,email_destinatario,mensagem.as_string())
        servidor_smtp.quit()
        print("Email de confirmação enviado com sucesso!")
        #with open("capitao_cadastro.txt", "w"):
            #pass
            #with open("alunos_cadastrados.txt", "w"):
                #pass
    except smtplib.SMTPException as e:
        print("Ocorreu um erro ao enviar o email de confirmação:", str(e))


def cadastrar_aluno(nome_aluno,curso_aluno, email_aluno, num_matricula_aluno, data_nascimento_aluno, num_camisa_aluno):
  with open("alunos_cadastrados.txt", "a", encoding="utf-8") as arquivo:
    arquivo.write(f"Nome Completo: {nome_aluno}, Curso: {curso_aluno}, E-mail: {email_aluno}, Numero de Matricula: {num_matricula_aluno}, Data de Nascimento: {data_nascimento_aluno}, Número da camisa: {num_camisa_aluno}\n")


def exibir_cadastro():
  with open("capitao_cadastro.txt", "r") as arquivo:
    linhas = arquivo.readlines()
    for linha in linhas:
      print(linha.rstrip())


def exibir_cadastro2():
  with open("alunos_cadastrados.txt", "r") as arquivo:
    linhas = arquivo.readlines()
    for linha in linhas:
      print(linha.rstrip())
