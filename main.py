import numpy as np

# Sistema de inventario con Numpy
# Crear una lista de identificadores para los productos.
# Inicializar el inventario con cero unidades.
# Registrar las unidades iniciales de cada producto.
# Simular la llegada de mercancía.
# Calcular cuántas unidades hay en total.
# Identificar qué productos necesitan reponerse.


productos = np.arange(1,11)
inventario = np.zeros(10)
inventario[:] = np.random.randint(1, 101, 10) # Números aleatorios del 1 al 100 para diez productos
inventario = inventario + np.random.randint(1,101,10)
total = np.sum(inventario)
reponer = np.where(inventario < 50)
print(reponer)