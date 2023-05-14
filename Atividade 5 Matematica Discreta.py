# Entrada dos conjuntos
A = set(map(int, input("Entre com os elementos do conjunto A separados por espaço: ").split()))
B = set(map(int, input("Entre com os elementos do conjunto B separados por espaço: ").split()))

# Escolha da operação
op = int(input("Escolha a operação:\n1 - União\n2 - Interseção\n3 - Diferença\n"))

# Operações
if op == 1:
  S = A.union(B)
elif op == 2:
  S = A.intersection(B)
elif op == 3:
  S = A.difference(B)
else:
  print("Operação inválida.")

# Saída do resultado
print("Resultado: S =", S)

#Implemente a recursividade para imprimir todos os números pares entre 1 a 10.

#Implemente sem usar a recursividade e print as duas telas.



#Implementação da recursividade para imprimir todos os números pares entre 1 a 10:

def print_pares_rec(n):
  if n > 10:
    return
  if n % 2 == 0:
    print(n)
  print_pares_rec(n+1)

print_pares_rec(1)


#Implementação sem usar a recursividade:

for i in range(1, 11):
  if i % 2 == 0:
    print(i)




