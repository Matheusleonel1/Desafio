# O Departamento Estadual de Meteorologia solicitou o desenvolvimento de um programa que leia um conjunto indeterminado de temperaturas, ao final informe a menor e a maior temperatura, bem como a média delas.


temperatura = []
n=1

for i in range(100000):
    temperatura.append(int(input(f'Informe a temperatura {n}: ')))


