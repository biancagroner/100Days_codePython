#Solicitando ao usuário que digite um número com 2 digitos e realizando a soma desses números
two_digit_number = input("Digite um número com 2 digítos")

num1 = int(two_digit_number[0])
num2 = int(two_digit_number[1])

soma = num1 + num2
print(soma)



## Calculando o IMC, trabalhando com transaformação de dados
altura = float(input("Entre com sua altura em metros: "))
peso = int(input("Entre com o seu peso em kg: "))

IMC = int(peso/(altura ** 2))
print(IMC)


## Calculando o tempo que falta considerando que a idade máxima é 90 anos
idade = input("Quantos anos você tem? ")

idade = 90 - int(idade)
days = idade * 365
weeks = idade * 52
months = idade * 12

print(f"Você tem {days} dias, {weeks} semanas e {months} meses restantes.")