#conficionales 'If'
# if True:
    # print ('se cumple la conficion')
    # print ('tambien se muestra este "print"')

# numero_n = 6
# print ('\nusaremos el numero 6 como muestra\n')
# if numero_n % 2 == 0:
    # print (numero_n, 'es un numero Par')
# else:
    # print (numero_n, 'no es un numero Par')

# #sentencia "while"
# print ('\nPractica en "while"')
# c = 0
# while c < numero_n:
    # c += 1
    # if c == 3 or c == 4:
        # print ('se obia en el proceso "c" vale', c)
        # continue
    # # if c == 7:
        # # print ('rompo con el proceso')
        # # break
    # print ('c vale:', c)
# else:
    # print ('se ha completado el proceso, como tal "c" vale', c)

#Prueva de consola
# print ('\n\n\tbienvenido a este menu interactivo\n')
# while True:
    # print ('''Que es lo que quieres hacer, escribe una opcion:
    # 1. Recibir un saludo
    # 2. Sumar 2 numeros
    # 3. Salir''')

    # opcion = int(input())
    # if opcion == 1:
        # saludar = input('Como te llamas:\t')
        # print ('\nHola, como estas', saludar, 'espero que estes bien en la quarentena\n')
    # elif opcion == 2:
        # n1 = int(input('introduce el primer numero:\t'))
        # n2 = int(input('introduce el segundo numero:\t'))
        # print ('\nLa suma de los 2 numeros es', n1 + n2, '\n')
    # elif opcion == 3:
        # print ('\nHasta luego "capullo"')
        # break
    # else :
        # print ('\nEres un Zoquete, digita bien el numero "retrasado"\n')

# print ('\nPractica en "for"')
# for i in range(numero_n):
    # print ('Este numero es:', i)

# print('\n')
# lista = [1, 2, 3, 4, 5, 6]
# for indice,numero in enumerate(lista):
#     lista[indice] *= 3
#     indice += 1
# print('lista del 1 al 6, multiplicado por *3:', lista)


#Practicas
#ejercicion N1
print('....................................................................')
n1 = float(input('ingrese un numero:\t'))
n2 = float(input('\ningrese otro numero:\t'))

if n1 == float(n1) and n2 == float(n2):
    print ('\nlos 2 numeros suman', n1 + n2)
    print ('la resta del primero con el segundo es', n1 - n2)
    print ('la muntiplicacion de los 2 numeros es', n1 * n2)
else:
    print ('eres un tonto, solo tenias que introducir 2 numeros puto')

#ejercicion N2
#ingrese un numero impar, repetir el proceso hasta que lo logre
print('....................................................................')
while True:
    numero_impar = int(input('\ningrese un numero impar:\t'))
    if (numero_impar % 2) != 0:
        print('\nBien Hecho, eso era todo')
        break
    else:
        print('\nPuto, solo tienes que introducir un puto numero impar.')

#ejetcicion N3
#un programa que sume todos los numero pares del 0 al 100
#con while tambien sale, y es mas facil aun..
print('....................................................................')
sumatoria = 0
for i,n in enumerate(range(100)):
    if (n % 2) == 0:
        sumatoria += n
    else:
        continue
print ('\nla suma total es:', sumatoria)

#otra forma de hacerlo mais facil
easy_sum = sum(range(0, 101, 2))
print ('\nla suma total del metodo de una sola linea es:', easy_sum)


#ejercicion N4
#Pida cuantos numeros desea introducir, luego se realiza la media aritmetica
print('....................................................................')
numero_consulta = int(input('\nCuantos numeros desea introducir:\t'))
numero_count = 0
numero_variable = 0
numero_suma = 0
while numero_count < numero_consulta:
    numero_count += 1
    numero_variable = float(input('Ingrese un numero:\t'))
    numero_suma += numero_variable
print ('\nla media de los', numero_count, 'es:\t', numero_suma/numero_count)

#ejercicio N5
#pida un numero del 0 al 9, solo continue si es correcto, luego comprueve si se encuentra en la lista 'numeros = [1, 3, 6, 9]'
print('....................................................................')
numeros = [1, 3, 6, 9]
while True:
    numero_peticion = int(input('Ingrese un numero del 0 al 9:\t'))
    if numero_peticion in list(range(10)):
        if numero_peticion in numeros:
            print ('Tu numero', numero_peticion, 'se encuentra en la lista ganadora', numeros)
        else:
            print ('Sigue intentando...')
        break

#ejercicio N6
#jugar con range(numero o variables, como inicio, final, salto)
print('....................................................................')
print('rango del 0 al 10:', list(range(11)))
print('rango del -10 al 0:', list(range(-10, 1)))
print('rango del 0 al 20, solo numeros pares:', list(range(0, 21, 2)))
print('rango del -20 al 0, solo numeros impares:', list(range(-19, 2, 2)))
print('numeros multiples de 5, en el rango de 0 al 50:', list(range(0, 51, 5)))
print('esto es una mierda')
