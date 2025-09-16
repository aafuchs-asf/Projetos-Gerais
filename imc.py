listGeral = []
y = 0

while y == 0:

    nome = input('Qual é o seu nome?').upper()         
    idade = input('Qual é a sua idade? ')              
    peso = float(input('Qual é o seu peso?(kg)'))      
    altura = float(input('Qual é a sua altura? (m)'))  
    imc = peso /(altura * altura)                      

    listGeral.append([nome, idade, peso, altura, imc])

    x = input('Deseja continuar respondendo? (s/n)').upper()
    if x == 'N':
        y = 1

for item in listGeral:

    if item[4] < 16:
        print(f'{item[0]} - {item[1]} anos - Baixo peso Grau I')
    elif item[4] < 16.99:
        print(f'{item[0]} - {item[1]} anos - Baixo peso Grau II')
    elif item[4] < 18.49:
        print(f'{item[0]} - {item[1]} anos - Baixo peso Grau III')
    elif item[4] < 24.99:
        print(f'{item[0]} - {item[1]} anos - Peso adequado')
    elif item[4] < 29.99:
        print(f'{item[0]} - {item[1]} anos - Sobrepeso')
    elif item[4] < 34.99:
        print(f'{item[0]} - {item[1]} anos - Obesidade grau I')
    elif item[4] < 39.99:
        print(f'{item[0]} - {item[1]} anos - Obesidade grau II')
    else:
        print(f'{item[0]} - {item[1]} anos - Obesidade grau III')
    