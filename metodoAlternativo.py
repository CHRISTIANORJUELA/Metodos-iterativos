import math
#Funciones
def funcion(x):
    return math.pow(x,3) - x - 1
def funcionDerivada(x):
    return (3*math.pow(x,2)) - 1
#Error
error = 0.001
#Variables
x = 1
xnuevo = 0
errorAprox = 100

for i in range(100):
    print("Iteracion: " + str(i))
    xnuevo = x - (funcion(x))/(funcionDerivada(x))
    print("X: " + str(xnuevo))
    errorAprox = (xnuevo-x)/xnuevo
    print("Error Aproximado: " +str(errorAprox*100))
    x = xnuevo
    if(errorAprox*100)<error:
      break