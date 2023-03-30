print(f"{8 * '<'}DESAFIO000{8 * '>'}")
print(f'{5 * "<" }13°mini-desafio de python{5 * ">"}')
km = float(input('Quantos KM esse carro já percorreu? '))
day = int(input('E por quantos dias ele foi alugado? '))
pday = day * 60
pkm = km * 0.15
totol = pday + pkm
print(f'O valor total a ser pago é: {totol}')