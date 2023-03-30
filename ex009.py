print(f"{8 * '<'}DESAFIO000{8 * '>'}")
print(f'{5 * "<" }10°mini-desafio de python{5 * ">"}')
prod = (input('Digite o nome de um produto: '))
preco = int(input('Agora digite o preço do produto: '))
valordodesconto = preco * (5/100)
desconto = preco - valordodesconto
print(f'O preço do {prod} com 5% de desconto é: {desconto}')