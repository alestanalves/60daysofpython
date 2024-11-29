#lista ordenada a partir do metodo sorted()

#1. lista numerica

lista_num = [55,69,31,66,77,121,661,1,2,3,4]

#sorted() eh uma funcao embutida no python 
#aceita uma lista e retorna ela em ordem
numeros_ordenados = sorted(lista_num)
numeros_ordenados2 = sorted(lista_num, reverse=True)

print(numeros_ordenados)
print(numeros_ordenados2)