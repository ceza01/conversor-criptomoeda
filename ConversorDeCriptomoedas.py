from forex_python.converter import CurrencyRates
from forex_python.bitcoin import BtcConverter
c = CurrencyRates()
b = BtcConverter()

while True:
  print("CONVERSÃO DE CRIPTOMOEDAS")
  print("1-Convertor de Bitcoins em Reais")
  print("2-Convertor de Reais em Bitcoins")
  print("3-Sair")
  x = int(input("Escolha uma opção: "))
  if x == 1:
    conversão1 = float(input("Digite o valor de Bitcoins que você deseja converter para Reais: "))
    resultado1 = b.convert_btc_to_cur(conversão1, 'BRL')
    print("O resultado da conversão é: ", resultado1)
    ui = input('Você quer continuar? [S/N] ')
    if ui.upper() != 'S':
      break
  elif x == 2:
    conversão2 = float(input("Digite o valor em Reais que você deseja converter para Bitcoin: "))
    resultado2= b.convert_to_btc(conversão2, 'BRL')
    print("O resultado da conversão é: ", resultado2)
    ui = input('Você quer continuar? [S/N] ')
    if ui.upper() != 'S':
      break
  elif x == 0 or x > 3:
    print("Você digitou um valor inválido!")
    ui = input('Você quer continuar? [S/N] ')
    if ui.upper() != 'S':
      break
  else:
      break
print("Você saiu do conversor!")

