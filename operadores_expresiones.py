# Primera Pregunta
number_a = int(input('Introduce un numero entero:\t'))
number_b = int(input('Introduce otro numero entero:\t'))

print('los numeros son iguales:\t', number_a == number_b)
print('los numeros son diferentes:\t', number_a != number_b)
print('a es mayor que b:\t', number_a > number_b)
print('b es mayor o igual que b:\t', number_b >= number_a)

# segunda Pregunta
texto_usuario = input('introduce un texto corto:\t')

print('el texto esta entre 3 a 9 caracteres:\t', len(texto_usuario) >= 3 and len(texto_usuario) < 10)


# tercera Pregunta
numero_magico = 12345679
numero_usuario = int(input('Ingrese un numero entero del 1 al 9:\t'))
numero_usuario *= 9
numero_magico *= numero_usuario

print(numero_magico)
print('hola, perro')
