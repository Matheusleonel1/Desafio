nomes = " Alessandro, Maria, Eduarda"
nomes_lista = [ "Alessandro", "Maria", "Eduarda" ]
num = []

for i in range (5): 
    num.append(int(input("Informe um valor inteiro")))


for i in range(len(num)):
    print(f" O número {num[i]} está na posição {i} da lista ")

print("\nResumo da questão" )
print(num)
print("----------------------")
print(nomes)
print(nomes_lista)
print(nomes_lista[2])