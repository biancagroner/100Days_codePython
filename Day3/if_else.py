## Defina se um número é par  ou impar
number = int(input("Qual número você quer checar? "))

if number % 2 == 0:
    print("Esseé um número par")
else:
    print("Esse é um número par")

## calculando o IMC e imprimindo se está ou não acima do peso

height = float(input("Entre com a sua altura em m: "))
weight = float(input("Entre com o seu peso em kg: "))


IMC = weight/(height ** 2)
IMC = round(IMC)

if (IMC < 18.5):
    print(f"Seu IMC é {IMC}, você está abaixo do peso.")
elif (IMC > 18.5) & (IMC < 25) :
    print(f"Seu IMC é {IMC}, você está com o peso normal.")
elif (IMC > 25) & (IMC < 30):
    print(f"Seu IMC é {IMC}, você está um pouco acima do peso.")
elif (IMC > 30) & (IMC < 35):
    print(f"Seu IMC é {IMC}, você está obeso.")
else:
    print(f"Seu IMC é {IMC}, você está clinicamente obeso.")