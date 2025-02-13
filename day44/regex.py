import re

def validar_email(email):
    """
    Funcao recebe email e valida atraves do regex
    args: email para validacao
    """
    regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if re.match(regex, email):
        print(f"{email} - Email validado")
    else:
        print(f"{email} - Email invalido")

# ^ indica o inicio do texto
# [a-zA-Z0-9_.+-]
# @ simbolo obrigatorio de um email
# +\. 
# $ finaliza o texto 

validar_email("contato@ackercode.com")
validar_email("contatoackercode.com")