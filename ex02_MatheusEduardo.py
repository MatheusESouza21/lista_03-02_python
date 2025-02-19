#Escreva um programa para exibir na tela o nome e a categoria de um lutador, o programa deve ler uma string para o nome e um número real para o peso.
#Conforme o peso, ocorrerá o enquadramento na categoria:
nome = input('Insira o nome do lutador: ')
peso = int(input('Insira seu peso: '))
if peso < 52:
    print('Inválido.')
elif peso >= 52 < 65:
    print('Nome: {} Categoria: Peso Pena'.format(nome))
elif peso >= 65 < 72:
    print('Nome: {} Categoria: Peso Leve'.format(nome))
elif peso >= 72 < 79:
    print('Nome: {} Categoria: Peso Ligeiro'.format(nome))
elif peso >= 72 < 86:
    print('Nome: {} Categoria: Peso Meio-Médio'.format(nome))
elif peso >= 86 < 90:
    print('Nome: {} Categoria: Peso Médio'.format(nome))
elif peso >= 90 < 100:
    print('Nome: {} Categoria: Peso Meio Pesado'.format(nome))
elif peso >= 100:
    print('Nome: {} Categoria: Peso Pesado'.format(nome))

print('Matheus Eduardo')