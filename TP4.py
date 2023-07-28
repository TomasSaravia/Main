"""1)Escriba una función que muestre todos los números primos entre 1 y un número n que es
ingresado por parámetro."""

def primos(numero_primo):
    for i in range(1,numero_primo):
        if i == 2 or i == 3 or i == 5 or i == 7:
            print(i,end=" ")
        elif i == 1:
            pass
        elif i % 2 == 0 or i % 3 == 0 or i % 7 == 0 or i % 5 == 0:
            pass
        else:
            print(i,end=" ")

rango = int(input("Ingresa un numero maximo: "))
primos(rango)


"""2) Escriba una función que le pida al usuario ingresar condimentos para un sándwich, hasta
que el usuario ingrese "salir". Cada vez que se ingrese un condimento, muestre un mensaje
avisando que ya se agregó el condimento al sándwich. Escriba versiones diferentes del
programa de acuerdo a estos criterios:
• Use un test condicional en el ciclo while para detener la ejecución.
• Use un test condicional dentro del ciclo para decidir si continuar la ejecución."""

def sandwich():
    contador = 0
    while contador < 5:
        contador += 1
        condimentos = input("Que condimento desea agragarle al sándwich? (maximo 5): ")
        if condimentos == "salir":
            return   
        print(f"El condimento: {condimentos} se agrego al sándwich")

#Use un test condicional dentro del ciclo para decidir si continuar la ejecución.


def sendwich():
    contador = 0
    while contador < 5:
        contador += 1
        condimentos = input("Que condimento desea agragarle al sándwich? (maximo 5): ")
        if condimentos == "salir":
            return
        elif contador == 5:
            pregunta = input("Cantidad maxima agregada desea agregar mas?")    
            if pregunta == "si":
                sandwich() 
        print(f"El condimento: {condimentos} se agrego al sándwich")


"""3) A) Remera: Escriba una función “hacer_remera()” que tome como parámetros un
tamaño y el mensaje que debería ir impreso en la remera. La función debe mostrar un mensaje
describiendo el tamaño de la remera y el mensaje impreso en ella. Llame la función una vez
usando argumentos por posición. Llámela una segunda vez usando argumentos por clave.
B) Remeras Grandes: Modifique la “funcion hacer_remera()” para que el tamaño por
defecto sea "L" y el mensaje, "Me gusta Python". Haga un par de remeras, la primera con los
valores por defecto, y la segunda con valores diferentes."""

#A
def hacer_remera1(tamaño,mensaje):
    tamaño = print(f"El tamaño de la remera sera {tamaño}")
    mensaje = print(f"El mesaje sera: {mensaje}")

#hacer_remera1("XL","Hello World!")
#hacer_remera1(tamaño= "XXL", mensaje="Mägo de Oz")

#B

def hacer_remera(tamaño,mensaje):
        tamaño_defecto = print(f"El tamaño de la remera sera L ")
        mensaje_defecto = print(f"El mesaje sera Me gusta Python")
        respuesta = input("Desea cambiar el tamaño o el mensaje?: ")
        if respuesta == "si":
            tamaño = print(f"El tamaño de la remera sera {tamaño}")
            mensaje = print(f"El mesaje sera: {mensaje}")

hacer_remera("XL","20190724")
  
"""4) Serie de Fibonacci: Escriba una función fibonacci(n) que devuelva los n primeros numeros
de la serie de Fibonacci. En esta serie, los primeros dos números son 0 y 1, y cada sucesivo
número es la suma de los dos números inmediatamente anteriores (ejemplo: 0,1,1,2,3,5,8, …)."""


def Fibonacci(num):
    numero1 = 0
    print(numero1,end=" ")
    numero2 = 1
    print(numero2,end=" ")
    for i in range(n):
        suma = numero1 + numero2
        print(numerito,end=" ")
        numero1 = suma
        una_suma = numerito + numero2
        print(una_suma,end=" ")
        numero2 = una_suma
n= int(input("Hasta que numero desas ver la sucesion?: "))
Fibonacci(n)


"""5) (Opcional) Calculadora más inteligente: Modifique el ejercicio 9 del primer practico para que
la calculadora sea capaz de devolver el resultado solamente de una operación especificada por
el usuario. Por ejemplo, si el usuario ingresa dos numeros x, y, y luego ingresa "1", la
calculadora devuelve la suma entre los numeros x,y; si ingresa "2", devuelve la resta, etc."""


def calculadora(x,y):
    pregunta_R = int(input("Cual poracion desea realizar con estos numeros?(1-suma / 2-resta / 3-multiplicacion / 4-exponente / 5-division / 6-division entera): "))
    if pregunta_R > 7 or pregunta_R < 0:
        print("ingrese un numero valido")
    elif pregunta_R == 1:
        print(x + y)
    elif pregunta_R == 2:
        print(x - y)
    elif pregunta_R == 3:
        print(x * y)
    elif pregunta_R == 4:
        print(x ** y)
    elif pregunta_R == 5:
        print(x / y)
    elif pregunta_R == 6:
        print(x // y)        


calculadora(2,4)


"""6) (Opcional) Conversión imperial: Desarrollar un programa en Python que pueda convertir
gramos a libras, centímetros a pulgadas y kilómetros a millas. El programa debe permitir la
conversión en ambos sentidos. 1.60934 Km = 1 milla , 0.393701 pulgadas = 1 cm , 0.00220462 libras = 1 gramo"""

"""7) (Opcional) Cuando un año es bisiesto, el mes más corto del año, febrero, tiene 29 días en
vez de 28. Esto sucede casi cada 4 años. Los tres criterios que permiten saber si un año es
bisiesto en el calendario gregoriano (el nuestro) son los siguientes:
• Si el año es divisible enteramente por 4, es bisiesto a menos que: o El año sea divisible por
100, entonces NO es bisiesto, a menos que:
▪ El año sea también divisible por 400. Entonces sí es un año bisiesto. Esto significa que
en el calendario gregoriano los años 2000 y 2400 son bisiestos, mientras que los años 1900,
2100, 2200 y 2300 no son bisiestos.
a) Escriba una función que tome un año y diga si es bisiesto o no.
b) Modifique su programa para que devuelva todos los años bisiestos entre el año
actual y el año pasado a la función como parámetro (este debe ser posterior al año actual)."""


"""8) (Opcional) Si listamos todos los números naturales menores a 10 que son múltiplos de 3 o 5,
obtenemos 3,5,6 y 9. La suma de estos múltiplos es 23. Encuentre la suma de todos los
múltiplos de 3 o 5 menores a 1000."""
