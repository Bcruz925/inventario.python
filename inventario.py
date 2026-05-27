# -----------------------------------------
# Programa de control de inventario
# Fundamentos de Programación - UNAD
# -----------------------------------------

# Función para calcular cuánto se debe pedir
def calcular_pedido(stock_actual, stock_minimo):

    if stock_actual < stock_minimo:
        return stock_minimo - stock_actual
    else:
        return 0


# Matriz del inventario
inventario = [

    [101, "Martillo", 12, 30],
    [203, "Puntilla", 5000, 3000],
    [305, "Lija", 50, 30],
    [405, "Pintura", 90, 100],
    [604, "Brocha", 20, 5],
    [109, "Destornillador", 4, 20],
    [365, "Yeso", 14, 50]

]

# Mostrar cantidad de artículos
print("Cantidad de artículos en el inventario:", len(inventario))

print("\nListado de productos y cantidad a solicitar\n")

# Recorrer la matriz
for articulo in inventario:

    codigo = articulo[0]
    nombre = articulo[1]
    stock_actual = articulo[2]
    stock_minimo = articulo[3]

    cantidad_pedir = calcular_pedido(stock_actual, stock_minimo)

    print("Código:", codigo)
    print("Artículo:", nombre)
    print("Cantidad a solicitar:", cantidad_pedir)
    print("-----------------------------")