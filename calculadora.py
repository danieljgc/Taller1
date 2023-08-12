print("Bienvenido a la calculadora:")
num1 = int(input("Inserta el primer número: "))
num2 = int(input("Inserta el segundo número: "))
operador = input("¿Que operación deseas realizar (inserta solo el simbolo: +, -, *, /)?")

if operador == "+":
    resultado = num1 + num2
    print("El resultado es: ",resultado)
elif operador == "-":
    resultado = num1 - num2
    print("El resultado es: ",resultado)
elif operador == "*":
    resultado = num1 * num2
    print("El resultado es: ",resultado)
elif operador == "/":
    resultado = num1 / num2
    print("El resultado es: ",int(resultado))

print("Gracias")