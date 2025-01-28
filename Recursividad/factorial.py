def factorial(num):
    if num == 1 or num == 0:
      return 1
    else:
        return num*(factorial(num-1))

"""
Python maneja la recursividad usando el principio LIFO (Last In, First Out).
Cada vez que la función se llama a sí misma, su estado actual se almacena en un stack.
Este proceso continúa hasta alcanzar la condición base, que detiene las llamadas recursivas.
A partir de ahí, se empiezan a resolver las llamadas en orden inverso,
eliminando cada estado del stack hasta que se vacía completamente.
"""
