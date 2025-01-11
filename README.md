# Inmobiliaria - Gestión de Venta y Arriendo de Viviendas

Este proyecto es una aplicación gráfica desarrollada en Python que permite gestionar los datos de una inmobiliaria. 
Utiliza estructuras de datos avanzadas como **Árboles Binarios de Búsqueda** para organizar y manejar la información 
de las viviendas en venta y arriendo.

## Características
- Gestión de datos de viviendas (venta y arriendo).
- Organización eficiente mediante un Árbol Binario de Búsqueda.
- Interfaz gráfica interactiva usando **PyQt6**.

## Estructura de Datos: Árbol Binario de Búsqueda
El Árbol Binario de Búsqueda (ABB) es utilizado para:
- Insertar viviendas en el sistema de manera ordenada según sus características.
- Realizar búsquedas eficientes.
- Aplicar recorridos para listar propiedades en diferentes órdenes (inorden, preorden, postorden).

### Implementación del Árbol Binario
1. **`arbol_binario.py`**: Define la estructura base de un árbol binario.
2. **`arbol_binario_busqueda.py`**: Extiende el árbol binario como un ABB, con métodos para:
   - Agregar claves en orden.
   - Buscar y recorrer nodos eficientemente.

## Tecnologías Utilizadas
- **Python 3.10+**
- **PyQt6**: Para la interfaz gráfica.
- **Estructuras de Datos**: Árbol Binario y Árbol Binario de Búsqueda.

## Instrucciones de Instalación
1. Clona el repositorio o descarga el proyecto.
   ```bash
   git clone https://github.com/alegria666/Inmobiliaria-Arboles.git
   cd INMOBILIARIA
   ```
2. Instala las dependencias necesarias.
   ```bash
   pip install PyQt6
   ```
3. Ejecuta la aplicación.
   ```bash
   python inmobiliaria.py
   ```

## Uso
1. Inicia la aplicación ejecutando el archivo `inmobiliaria.py`.
2. Usa la interfaz gráfica para registrar propiedades con sus datos relevantes.
3. Observa cómo se organizan las propiedades en el árbol binario.
4. Realiza consultas sobre propiedades disponibles o en venta.

## Estructura del Proyecto
```
INMOBILIARIA/
├── inmobiliaria.py                 # Archivo principal
├── ed/
│   └── jerarquicas/
│       ├── arbol_binario.py        # Implementación de Árbol Binario
│       ├── arbol_binario_busqueda.py # Extensión como Árbol Binario de Búsqueda
│       ├── excepciones.py          # Gestión de excepciones
│       ├── inmueble.py             # Clase para manejar datos de viviendas
│       ├── nodo_ab.py              # Nodo de Árbol Binario
│       ├── recorridos.py           # Métodos de recorrido de árboles
├── imagenes/                       # Recursos visuales
│   ├── casa.png
│   ├── consulta.png
│   ├── fondo.png
│   └── registrar.png
```

## Créditos
- **Daniel Esteban Alegría Zamora** - Desarrollo, diseño e implementación de estructuras de datos.

## Notas
Este proyecto es una demostración académica y no está destinado para un uso en producción.
