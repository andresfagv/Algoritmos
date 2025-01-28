def powerSet(s):
    """
        Genera todos los subconjuntos posibles de un conjunto dado.

        Concepto de subset:
        Un subconjunto es cualquier combinación de elementos que se pueden formar a partir
        del conjunto original, incluyendo el conjunto vacío y el conjunto completo. Por ejemplo,
        para el conjunto [1, 2], los subconjuntos serían: [], [1], [2], [1, 2].

        Lógica detrás del algoritmo:
        - Usamos recursividad para ir dividiendo el conjunto en partes más pequeñas.
        - Para cada elemento, tomamos dos decisiones:
          1. Incluirlo en el subconjunto.
          2. No incluirlo en el subconjunto.
        - La recursión sigue hasta que el conjunto se reduce a vacío (caso base).
        - Luego, combinamos los subconjuntos sin el último elemento con los que incluyen dicho elemento.
        """

    if len(s) == 0:
        return [[]]  # Caso base: el conjunto vacío tiene un único subconjunto (él mismo)
    else:
        smaller_set = powerSet(s[:-1])  # Recursión con el conjunto sin el último elemento
        last_item = s[-1]  # Último elemento del conjunto
        subsets = []
        for item in smaller_set:
            subsets.append(item + [last_item])  # Añadir el último elemento a cada subconjunto
        return smaller_set + subsets  # Combinar subconjuntos sin y con el último elemento

# Prueba del código
S1 = [1, 2, 3]
print(powerSet(S1))
