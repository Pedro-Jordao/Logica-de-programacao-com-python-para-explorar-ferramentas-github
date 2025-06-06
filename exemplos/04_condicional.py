# Conteúdo do arquivo: /logica-de-programacao/logica-de-programacao/exemplos/04_condicional.py

# Este arquivo apresenta a estrutura condicional if.

numero = int(input("Digite um número: "))  # Solicita um número ao usuário

# Verifica se o número é positivo, negativo ou zero
if numero > 0:
    print("O número é positivo.")  # Mensagem para número positivo
elif numero < 0:
    print("O número é negativo.")  # Mensagem para número negativo
else:
    print("O número é zero.")  # Mensagem para zero