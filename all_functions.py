def circulo(x):
    if x == "Pequeño":
        print("             * * *             ")
        print("            *     *            ")
        print("            *     *            ")
        print("             * * *             ")
    elif x == "Mediano":
        print("           * * * *          ")
        print("        * *       * *       ")
        print("       *             *      ")
        print("      *               *     ")
        print("      *               *     ")
        print("      *               *     ")
        print("       *             *      ")
        print("        * *       * *       ")
        print("           * * * *          ")
    elif x == "Grande":
        print("          * * * *              ")
        print("       * *       * *           ")
        print("    * *             * *        ")
        print("   *                   *       ")
        print("  *                     *      ")
        print("  *                     *      ")
        print("  *                     *      ")
        print("  *                     *      ")
        print("   *                   *       ")
        print("    * *             * *        ")
        print("       * *       * *           ")
        print("          * * * *              ")
        print("                               ")
    else:
        print("Por favor, ingrese el tamaño redactado correctamente")

def recta(x):
    for i in range(x):
        print(" x ",end="")
    print()

def rectangulo(x,y):
    for i in range(x):
        for j in range(y):
            print(" x ",end="")
        print()

#triángulo
def triangulo(x):
    for i in range(1,x+1):
        for j in range(i):
            print(" x ",end="")
        print()

def cuadrado(x, y):
    for i in range(0,x):
        for j in range (x):
            print(" x ",end="")
        print()

n = 0
def start(n):
    if n == "cuadrado":
        x = int(input("Ingrese las dimensiones del cuadrado:  "))
        y = x
        cuadrado(x, y)
        print()
    elif n == "triangulo":
        x = int(input("Ingrese la longitud de un lado del triángulo rectángulo: "))
        triangulo(x)
        print()
    elif n == "circulo":
        x = str(input("Ingrese el tamaño deseado del círculo (Pequeño, Mediano, Grande):  "))
        circulo(x)
        print()
    elif n == "rectangulo":
        x = int(input("Ingrese la altura del rectángulo:  "))
        y = int(input("Ingrese la base del rectángulo:  "))
        rectangulo(x, y)
        print()
    elif n == "recta":
        x = int(input("Ingrese la longitud de la línea recta:  "))
        recta(x)
        print()
    else:
        print("Figura incorrecta, por favor ingrese la figura redactada correctamente")
