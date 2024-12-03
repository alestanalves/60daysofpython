fibonacci = [0, 1] # A sequência sempre começa com 0 e 1
print(fibonacci[-1] + fibonacci[-2]) # soma 1 mais 0

for i in range(8):
    proximo_numero = fibonacci[-1] + fibonacci[-2]
    fibonacci.append(proximo_numero)

print(fibonacci)