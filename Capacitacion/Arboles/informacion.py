import streamlit as st

from PIL import Image
import requests
from io import BytesIO

st.set_option('deprecation.showPyplotGlobalUse', False)

# Obtener la URL de la imagen
url1 = "https://www.oscarblancarteblog.com/wp-content/uploads/2014/08/tiposdenodos.png"

# Obtener la imagen desde la URL
response = requests.get(url1)
image1 = Image.open(BytesIO(response.content))    
def info():

    st.header('¿Que es un Arbol?')
    st.write("Un arbol es un grafo no dirigido, conexo sin ciclos, un grafo no dirigido es un arbol si y solo si, hay un unico camino entre cada pareja de vertices.")
    st.image(image1, use_column_width=True)
    st.write("Existen muchos tipos de Grafos, aqui tienes todos los tipos de Arboles y sus definiciones:")
    st.subheader("Tipos de Arboles")
    tipoarbol = st.selectbox(f"Seleccione uno de los tipos de arboles: ", options=["Arbol con raiz", "Arbol Ordenado con Raiz", "Arboles de Decision", "Algoritmos de ordenamiento","Arboles descendientes","Arboles de Ancestros","Arboles de hoja","Nodos internos","Grado de Nodos","Rama de grado","Nivel de nodos","Altura del arbol","Profundida del nodo","Sub-Arbol","Bosque"], index=2, key=f"tipoarbol_")
    
    if tipoarbol == "Arbol con raiz":
        return st.subheader("Arbol con raiz") and st.write(" Es un arbol en el que uno de sus vertices ha sido designado como la raiz y todas las aristas estan orientadas de modo que se alejan de la raiz.") # Máxima prioridad
    elif tipoarbol == "Arbol Ordenado con Raiz":
        return st.subheader("Arbol Ordenado con Raiz") and st.write("Es un arbol con raiz en el que los hijos de cada vertice interno estan ordenados.") 
    elif tipoarbol == "Arboles de Decision":
        return st.subheader("Arboles de Decision") and st.write("Los arboles con raiz pueden utilizarce para modelar problemas en los que una serie de decisiones lleva a una solucion.") 
    elif tipoarbol == "Algoritmos de ordenamiento":
        return st.subheader("Algoritmos de ordenamiento") and st.write("Un algoritmo de ordenacion basado en comparaciones binarias requiere al menos 'log n!' comparaciones.")
    elif tipoarbol == "Arboles descendientes":
        return st.subheader("Arboles descendientes") and st.write("Un árbol descendiente o un arbol de decisión es una estructura que se utiliza para tomar decisiones o clasificar objetos en función de características o atributos. Se parece a un árbol invertido, donde cada nodo es una pregunta o una condición sobre una característica. Las respuestas o condiciones conducen a ramas diferentes hasta llegar a una decisión final en los nodos hoja. Se construyen seleccionando características relevantes y dividiendo los datos en subconjuntos puros.  manejan diferentes tipos de datos y son útiles para clasificar objetos o tomar decisiones.")
    elif tipoarbol == "Arboles de Ancestros":
        return st.subheader("Arboles de Ancestros") and st.write("Un árbol de ancestros es una estructura jerárquica donde cada elemento tiene un único ancestro directo (excepto el nodo raíz) y puede tener varios descendientes. Muestra las relaciones de ascendencia entre los elementos y se utiliza en aplicaciones como genealogía o sistemas de archivos. Ayuda a encontrar el ancestro común más cercano y proporciona información sobre los ancestros de cada elemento.")
    elif tipoarbol == "Arboles de hoja":
        return st.subheader("Arboles de hoja") and st.write("Un árbol de hojas es una estructura jerárquica donde cada nodo tiene solo nodos descendientes, y los nodos terminales se llaman nodos hoja. Cada nodo hoja representa una entidad o elemento final en la estructura y no tiene nodos adicionales debajo de ellos. Los árboles de hojas se utilizan para organizar y clasificar información de manera jerárquica, donde las categorías más específicas se encuentran en los nodos hoja. \n Para concluir, un árbol de hojas es una estructura en la que los nodos terminales son los nodos hoja, representando las entidades o elementos finales de la clasificación jerárquica. Proporciona una forma organizada de estructurar y clasificar información en categorías específicas.") 
    elif tipoarbol == "Nodos internos":
        return st.subheader("Nodos internos") and st.write("Los nodos internos son puntos de ramificación en una estructura de árbol. Son aquellos nodos que tienen al menos un nodo descendiente y se encuentran entre el nodo raíz y los nodos hoja. Los nodos internos contienen información clave para organizar la jerarquía de los datos en el árbol y ayudan a dirigir el flujo de navegación dentro de la estructura.") 
    elif tipoarbol == "Grado de Nodos":
        return st.subheader("Grado de Nodos") and st.write("El grado de nodos en una estructura de árbol o grafo indica cuántos nodos están conectados directamente a ese nodo. Puede ser de entrada o de salida en un grafo dirigido, o la suma total de las conexiones en un grafo no dirigido. El grado de los nodos ayuda a comprender la conectividad y la estructura de la red. Nodos con un grado alto tienen más conexiones, mientras que nodos con un grado bajo están menos conectados.") 
    elif tipoarbol == "Rama de grado":
        return st.subheader("Rama de grado") and st.write("La rama de grado de un árbol es el número máximo de conexiones que se pueden seguir desde un nodo hasta los nodos hoja sin retroceder ni repetir nodos. Nos indica la profundidad máxima y la longitud máxima de los caminos en el árbol. Es útil para comprender la estructura y la altura máxima del árbol.") 
    elif tipoarbol == "Nivel de nodos":
        return st.subheader("Nivel de nodos") and st.write("El nivel de un nodo en un árbol indica su posición o profundidad dentro de la estructura. El nivel 0 es el nodo raíz y a medida que nos movemos hacia abajo, los niveles aumentan en incrementos de uno. El nivel de un nodo proporciona información sobre su posición relativa y distancia desde el nodo raíz.") 
    elif tipoarbol == "Altura del arbol":
        return st.subheader("Altura del arbol") and st.write("La altura de un árbol es la longitud máxima del camino desde la raíz hasta cualquier nodo hoja. Representa la profundidad máxima del árbol y puede afectar la eficiencia de las operaciones en el árbol.") 
    elif tipoarbol == "Profundida del nodo":
        return st.subheader("Profundida del nodo") and st.write("La profundidad de un nodo en un árbol indica la distancia desde la raíz hasta ese nodo en particular, contando la cantidad de aristas o conexiones necesarias para llegar a él. Es una medida útil para entender la posición y la jerarquía de los nodos en el árbol.") 
    elif tipoarbol == "Sub-Arbol":
        return st.subheader("Sub-Arbol") and st.write("Un subárbol es una porción de un árbol que se deriva de un nodo raíz y contiene todos sus descendientes. Es una estructura de árbol independiente dentro del árbol original y se utiliza para analizar y manipular partes específicas del árbol.") 
    elif tipoarbol == "Profundida del nodo":
        return st.subheader("Arbol Ordenado con Raiz") and st.write("Es un arbol con raiz en el que los hijos de cada vertice interno estan ordenados.") 
    elif tipoarbol == "Bosque": #bosque
        return st.subheader("Bosque") and st.write("Un bosque es un conjunto de árboles independientes. Cada árbol en el bosque se trata como una entidad separada con su propia raíz y estructura jerárquica. Los bosques se utilizan en situaciones donde se necesitan trabajar con múltiples estructuras de árbol independientes al mismo tiempo.") 
    else:
        return 5  # Prioridad por defecto
    
def Aplicaciones_de_arboles():
    st.subheader("Apliciones de arboles")
    st.write("tienen diversas aplicaciones en diferentes áreas. Aquí hay algunas aplicaciones comunes de los árboles")
    aplicacionarbol = st.selectbox(f"Seleccione una de las aplicaiones: ", options=["Algoritmos de búsqueda", "Redes de comunicación", "Estructuras de datos", "Análisis de algoritmos","Optimización","Inteligencia artificial y aprendizaje automático","Compresión de datos","Representación de conocimiento"], index=2, key=f"tipoarbol_")
    
    if aplicacionarbol == "Algoritmos de búsqueda":
        return st.subheader("Algoritmos de búsqueda") and st.write("Los árboles se utilizan en algoritmos de búsqueda como el árbol de búsqueda binaria y el árbol de búsqueda binaria equilibrada (como el árbol AVL o el árbol rojo-negro). Estos árboles permiten realizar búsquedas eficientes, inserciones y eliminaciones en conjuntos de datos ordenados.") # Máxima prioridad
    if aplicacionarbol == "Redes de comunicación":
        return st.subheader("Redes de comunicación") and st.write("Los árboles se utilizan para modelar y diseñar redes de comunicación, como redes de transmisión de datos, árboles de enrutamiento en protocolos de comunicación o estructuras de jerarquía en redes de distribución de contenido.") # Máxima prioridad
    if aplicacionarbol == "Estructuras de datos":
        return st.subheader("Estructuras de datos") and st.write("Los árboles se utilizan como estructuras de datos para organizar y almacenar información jerárquica. Por ejemplo, los árboles de directorios en sistemas operativos representan la estructura jerárquica de los archivos y las carpetas en una computadora.") # Máxima prioridad
    if aplicacionarbol == "Análisis de algoritmos":
        return st.subheader("Análisis de algoritmos") and st.write("Los árboles se utilizan para analizar la complejidad de los algoritmos. Por ejemplo, el árbol de recursión es una herramienta utilizada para analizar el tiempo y el espacio requerido por los algoritmos recursivos.") # Máxima prioridad
    if aplicacionarbol == "Optimización":
        return st.subheader("Optimización") and st.write("Los árboles se utilizan en problemas de optimización combinatoria, como el árbol de búsqueda binario balanceado en el problema de búsqueda binaria óptima. Estos árboles ayudan a encontrar soluciones eficientes en problemas de búsqueda y optimización.") # Máxima prioridad
    if aplicacionarbol == "Inteligencia artificial y aprendizaje automático":
        return st.subheader("Inteligencia artificial y aprendizaje automático") and st.write("Los árboles de decisión y los bosques aleatorios (conjuntos de árboles) se utilizan en algoritmos de aprendizaje automático para tareas como clasificación, regresión y detección de anomalías. Estos modelos son populares debido a su capacidad para manejar datos con características categóricas y numéricas, y su interpretabilidad.") # Máxima prioridad
    if aplicacionarbol == "Compresión de datos":
        return st.subheader("Compresión de datos") and st.write("Los árboles se utilizan en algoritmos de compresión de datos, como el algoritmo de compresión de Huffman. Estos árboles se construyen utilizando las frecuencias de los símbolos en los datos para lograr una compresión eficiente.") # Máxima prioridad
    if aplicacionarbol == "Representación de conocimiento":
        return st.subheader("Representación de conocimiento") and st.write("Los árboles se utilizan en representación de conocimiento y ontologías para organizar y estructurar la información de dominio. Estos árboles permiten establecer relaciones y jerarquías entre los conceptos y facilitan la búsqueda y el razonamiento.") # Máxima prioridad
