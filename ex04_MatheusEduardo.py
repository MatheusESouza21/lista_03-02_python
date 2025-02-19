#No SENAILÂNDIA mulheres e homens podem servir o exército do país. O serviço é opcional e é muito comum que as pessoas se apresentem para o serviço em algum momento da vida.
#Existe uma única restrição para o ingresso, que é a idade da pessoa: 
#Para mulheres, a idade aceita é entre 21 e 34 anos (>=21 e <=34)
#Para homens, a idade aceita é entre 18 e 39 anos (>=18 e <=39)
#Escreva um programa que leia 3 dados de entrada: Nome da pessoa, idade e gênero. Informe se a pessoa será aceita ou não para o serviço.
#OBS: Para o gênero deve ser lido somente um caractere, que pode ser: ‘f’ ou ‘F’, ‘m’ ou ‘M’. Qualquer coisa diferente, deve ser informado como inválido.
nome = input('Qual o nome da pessoa? ')
idade = int(input('Qual idade da pessoa? '))
genero = input('Qual o gênero da pessoa?(F ou M) ').lower()
if genero == 'm' and idade >=18 <=39:
    print('{} será aceito no serviço.'.format(nome))
elif genero == 'f' and idade >=21 <=34:
    print('{} será aceita no serviço.'.format(nome))
elif genero == 'm' and idade <18 > 39:
    print('{} não será aceito no serviço.'.format(nome))
elif genero == 'f' and idade <21 > 34:
    print('{} não será aceita no serviço.'.format(nome))
else:
    print('Inválido.')

print('Matheus Eduardo')