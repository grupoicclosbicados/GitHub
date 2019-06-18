#n es la figura
# x son las dimensiones
#cuando el programa detecte la figura, llamará a la función correspondiente (habrá un def function para cada figura)
n = str(input("Escriba la figura que desea dibujar (Cuadrado/Triángulo/Círculo/Rectángulo/Recta):  "))
if n == "Cuadrado":
    import cuadrado
    x = int(input("Ingrese las dimensiones del cuadrado:  "))
    y = x
    cuadrado.funcioncuadrado(x, y)
    print()
elif n == "Triángulo":
    import borrador
    x = int(input("Ingrese la longitud de un lado del triángulo rectángulo: "))
    borrador.triangulo(x)
    print()
elif n == "Círculo":
    import tamaños_circulo
    x = str(input("Ingrese el tamaño deseado del círculo (Pequeño, Mediano, Grande):  "))
    tamaños_circulo.tamaño(x)
    print()
elif n == "Rectángulo":
    import rectánguloborrador
    x = int(input("Ingrese la altura del rectángulo:  "))
    y = int(input("Ingrese la base del rectángulo:  "))
    rectánguloborrador.rectangulo(x, y)
    print()
elif n == "Recta":
    import Rectaborrador
    x = int(input("Ingrese la longitud de la línea recta:  "))
    Rectaborrador.recta(x)
    print()
else:
    print("Figura incorrecta, por favor ingrese la figura redactada correctamente")
