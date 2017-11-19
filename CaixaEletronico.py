# authors = 'Thallison', 'Diorgeles', 'Abimael', 'Lucas'
saque = 251
cedulas_disp = [50, 20, 10, 100]
result = 0
cont = 0
notas_utilizadas = []

while True:
    numeros_ordenados = sorted(cedulas_disp, reverse=True)
    cont = saque
    for cedula in numeros_ordenados:
        while(cont >= cedula):
            result = result + cedula
            cont = cont - cedula
            notas_utilizadas.append(cedula)

    valor_inutilizado = saque - sum(notas_utilizadas)
    print(['Valores não utilizados', valor_inutilizado])
    print('Notas utilizadas:')
    print (notas_utilizadas)
    break
