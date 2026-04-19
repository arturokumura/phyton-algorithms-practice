''' Dado um número inteiro de qualquer tamanho (inteiro longo), fornecido pelo usuário via teclado,
elabore um programa para mostrar na tela o número invertido.'''
n = int(input("Informe um número: "))
resultado = 0
while n > 0:
    digito = n % 10
    resultado = (resultado * 10) + digito
    n = n // 10
print(resultado)
