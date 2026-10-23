# 📦 Sistema de Inventario con NumPy

Un simulador sencillo y eficiente para la gestión y análisis de inventario de productos desarrollado en Python utilizando la librería **NumPy**.

---

## 📋 Descripción

Este proyecto pone en práctica los conceptos fundamentales de manipulación de arrays multidimensionales y operaciones vectorizadas con **NumPy** aplicados a la lógica de almacén:

1. **Identificadores de productos:** Genera un arreglo de IDs únicos para 10 productos con `np.arange`.
2. **Inicialización:** Inicializa el inventario en 0 unidades con `np.zeros`.
3. **Registro de stock inicial:** Asigna existencias iniciales aleatorias (entre 1 y 100 unidades) con `np.random.randint`.
4. **Llegada de mercancía:** Simula el reabastecimiento sumando vectores elemento a elemento.
5. **Cálculo del total:** Obtiene la cantidad total de unidades almacenadas mediante `np.sum`.
6. **Alerta de reposición:** Detecta los índices de aquellos productos cuyo stock se encuentra por debajo del umbral mínimo (< 50 unidades) mediante `np.where`.

---

## 📁 Estructura del Proyecto

```text
Sistema de inventario con Numpy/
│
├── main.py              # Script principal con la lógica del inventario
├── requirements.txt     # Dependencias requeridas (numpy)
├── LICENSE              # Licencia de código abierto MIT
├── .gitignore           # Archivos y carpetas ignorados por Git
└── README.md            # Documentación del proyecto
```

---

## 🛠️ Requisitos Previos

- **Python 3.8 o superior** instalado en el sistema.
- Gestor de paquetes **pip**.

---

## 🚀 Instalación

1. **Abrir la terminal** en la carpeta del proyecto:
   ```bash
   cd "Sistema de inventario con Numpy"
   ```

2. **Crear un entorno virtual (recomendado):**
   - **En Windows:**
     ```powershell
     python -m venv venv
     .\venv\Scripts\activate
     ```
   - **En macOS / Linux:**
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```

3. **Instalar dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

---

## ▶️ Uso y Ejecución

Con el entorno virtual activado, ejecuta el script principal:

- **En Windows:**
  ```powershell
  py main.py
  # o también:
  python main.py
  ```

- **En macOS / Linux:**
  ```bash
  python3 main.py
  ```

### Ejemplo de Salida

```text
(array([2, 5]),)
```

> **Interpretación:** La salida de `np.where(inventario < 50)` devuelve una tupla con los índices (en base 0) de los productos que tienen menos de 50 unidades en stock y necesitan reposición.

---

## 📚 Funciones de NumPy Utilizadas

| Función | Propósito |
| :--- | :--- |
| `np.arange(1, 11)` | Crea una secuencia de identificadores para los productos. |
| `np.zeros(10)` | Inicializa el arreglo del inventario con ceros. |
| `np.random.randint(low, high, size)` | Genera números enteros pseudoaleatorios dentro de un rango determinado. |
| `np.sum(inventario)` | Calcula la suma de todos los elementos del arreglo. |
| `np.where(condición)` | Encuentra las posiciones donde se cumple una condición lógica. |

---

## 📄 Licencia

Este proyecto está bajo la Licencia **MIT**. Consulta el archivo [LICENSE](LICENSE) para más detalles.
