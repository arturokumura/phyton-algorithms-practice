'''Crie uma função retornar o maior elemento inteiro de uma lista. Não
será permitido o uso de função que não seja da sua autoria.
'''
def maior(nums):
    if len(nums) == 1:
        return nums[0]
    maior_resto = maior(nums[1:])
 
    if nums[0] > maior_resto:
        return nums[0]
    else:
        return maior_resto


lista = [10,2,3,11,4,9]
print(maior(lista))
