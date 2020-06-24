import re
# Ejercicios con REGEX
# No tenga letras
NoLetras = '[^a-zA-Z]+$'
print('Ingrsar cadena de texto')
text = input()
print("Texto sin letras: ", True if re.match(NoLetras, text) else False)

# Solo tenga numeros
OnlyNumbers = r'^[\d]+$'
print('Ingrsar cadena de texto')
text = input()
print("solo numeros: ", True if re.match(OnlyNumbers, text) else False)

# Solo tenga letras Mayusculas
OnlyUCase = '^[A-Z]+$'
print('Ingrsar cadena de texto')
text = input()
print("solo mayusculas: ", True if re.match(OnlyUCase, text) else False)

# Solo tenga letras minusculas
OnlyLCase = '^[a-z]+$'
print('Ingrsar cadena de texto')
text = input()
print("solo minusculas: ", True if re.match(OnlyLCase, text) else False)

# No tenga numeros
NoNumbers = r'[^\d]+$'
print('Ingrsar cadena de texto')
text = input()
print("Sin numeros: ", True if re.match(NoNumbers, text) else False)
