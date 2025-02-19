#Escreva um programa que forneça um tipo de aplicação financeira adequado a um investidor a partir de 2 dados fornecidos: O grau de aceitação de risco e o valor a ser investido.
#Deve ser lido no teclado na forma BX ou AL risco. Se for fornecido algo diferente disso, o programa deve mostrar uma mensagem indicando que foi fornecido um dado inválido.
#Para o valor, deve ser um número real.
risco = input('Digite o grau de risco (BX ou AL): ').upper()
investimento = float(input('Insira o investimento desejado: '))

if investimento < 1000 and risco == 'BX':
    print('Recomendamos que invista em poupança.')

elif investimento >= 1000 and risco == 'BX':
    print('Recomendamos que invista em renda fixa.')

elif investimento < 1000 and risco == 'AL':
    print('Recomendamos que invista em bitcoins.')

elif investimento >= 1000 and risco == 'AL':
    print('Recomendamos que invista em ações.')
else:
    print('Foi fornecido um risco inválido!')

print('Matheus Eduardo')
