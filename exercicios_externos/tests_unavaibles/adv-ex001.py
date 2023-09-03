''' Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:  

a. Se o usuário informar o valor de A igual a zero. a equação não e do segundo grau e o programa não deve fazer pedir os demais valores, sendo encerrado;

b. Se o delta calculado for negativo, a equação não possui raízes reais. Informe ao usuário e encerre o programa;

c. Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe ao usuário;

d. Se o delta for positivo, a equação possui duas raízes reais; informe-as ao usuário;'''

a = float(input('Digite o valor de a: '))
b = float(input('Digite o valor de b: '))
c = float(input('Digite o valor de c: '))

delta = (b**2 - 4*a*c)
x1 = (-b + delta**(1/2) / (2*a))
x2 = (-b - delta**(1/2) / (2*a))

print(f'O valor de X1 é: {x1}')
print(f'O valor de X2 é: {x2}')

if (a, b, c)!= 0 :
  print('A equação é completa.')
  pass
else:
  print('A equação é incompleta.')
  pass
