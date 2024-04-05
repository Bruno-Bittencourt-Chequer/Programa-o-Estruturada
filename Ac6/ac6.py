


# EX01: Hello World

print("Hello World!")


#EX02: Extremamente Básico

A = int(input())
B = int(input())
X = A + B

print("X =", X, end="\n")




#EX03: Cálculo Simples

entrada = input()
codigo_peca1 = int(entrada[:2])
num_peca1 = int(entrada[3:5])
valor_unitario1 = float(entrada[6:])
 
entrada = input()
codigo_peca2 = int(entrada[:2])
num_peca2 = int(entrada[3:5])
valor_unitario2 = float(entrada[6:])

total_a_pagar = (num_peca1 * valor_unitario1) + (num_peca2 * valor_unitario2)

print("VALOR A PAGAR: R$", total_a_pagar)




#EX04: O Maior

a = int(input())
b = int(input())
c = int(input())

maior_ab = (a + b + (a - b)) // 2
if maior_ab > c:
    maior = maior_ab
else:
    maior = c
print(maior, "eh o maior")



#EX05: Distância entre dois Pontos

x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

distancia = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
distancia_arredondada = round(distancia, 4)

print(distancia_arredondada)


