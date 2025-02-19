#No comércio o conceito de margem bruta é uma porcentagem que é aplicada ao preço de custo para se obter o preço de venda. 
# Uma loja tem como política comercial, aplicar uma margem bruta de 45%, quando o preço de custo é <= R$100,00. Se o produto custa mais que isso, a margem de lucro é 35%.
#Escreva um programa que leia o preço do produto e mostre seu preço de venda. 
preço = float(input('Qual o preço do produto? '))
if preço <= 100:
    pdevenda = preço + preço * 0.45
    print('O preço de venda é {}'.format(pdevenda))
elif preço > 100:
    pdevenda = preço + preço * 0.35
    print('O preço de venda é {}'.format(pdevenda))

print('Matheus Eduardo')