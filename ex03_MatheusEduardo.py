#Uma empresa financeira consegue empréstimo a pessoas físicas, quando o valor da parcela é menor que 8% do salário da pessoa. Escreva um programa que leia 2 números reais:
#  O valor do salário e o valor da parcela e informe se o empréstimo será concedido ou não.
salario = float(input('Qual o valor do salário? '))
parcela = float(input('Qual o valor da parcela? '))
if parcela < salario * 0.08:
    print('O empréstimo será concedido.')
else:
    print('O empréstimo não será concedido.')

print('Matheus Eduardo')