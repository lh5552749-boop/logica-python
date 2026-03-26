print('Calculadora simples')

num1 = float(input('Digite o primeiro numero: ' ))
num2 = float(input('Digite o segundo numero: '))

print('Escolha a operaçao:')
print('1 - Soma')
print('2 - Subtraçao')
print('3 - Multiplicaçao')
print('4 - Divisao')

opcao = input('Digite a opçao: ')

if opcao == '1':
    resultado = num1 + num2
    print('Resultado:', resultado)
elif opcao == '2':
    resultado = num1 - num2
    print('Resultado:', resultado)
elif opcao == '3':
    resultado = num1 * num2
    print('Resultado:., resultado')
elif opcao == '4':
     if num2 != 0:
         resultado = num1 / num2
         print('Resulatado:', resultado)
     else:
          print('Nao e possivel dividir por zero.')
else:
         print('Opçao invalida.')