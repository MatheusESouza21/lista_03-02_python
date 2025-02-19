#Nas eleições municipais, os munícipios com 200.000 eleitores ou mais, tem segundo turno caso o 1º colocado não tenha mais que 50% dos votos.
#Escreva um programa que leia: O nome do munícipio, a quantidade de eleitores e a quantidade de votos do candidato mais votado. Informe se haverá segundo turno ou não.
nome = input('Qual o nome do municipio? ')
eleitores = int(input('Quantos eleitores {} tem? '.format(nome)))
votos = int(input('Quantos votos o candidato mais votado de {} tem? '.format(nome)))
if eleitores > 200000 and votos < eleitores / 2:
    print('Haverá segundo turno.')
else:
    print('Não haverá segundo turno.')

print('Matheus Eduardo')