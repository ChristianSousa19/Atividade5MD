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
