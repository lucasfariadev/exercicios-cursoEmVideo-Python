print('=== Desafio 04 =====')
print('Faça um programa que leia algo pelo teclado'
      'e mostre na tela o seu tipo primitivo'
      'e todas as informações possiveis sobre ele')

a = input('Digite algo: ')
print('O tipo primitivo desse valor é', type(a))
print('só tem espaços? ', a.isspace())
print('é um número? ', a.isnumeric())
print('é alfabético', a.isalpha())
print('é alfanumérico?', a.isalnum())
print('Está em maiúsculas', a.isupper())
print('Está em minúsculas', a.islower())
print('Está capitalizado', a.istitle())




