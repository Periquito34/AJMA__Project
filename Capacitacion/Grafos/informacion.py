import matplotlib.pyplot as plt
import networkx as nx
import streamlit as st
from PIL import Image
import requests
from io import BytesIO

st.set_option('deprecation.showPyplotGlobalUse', False)

# Obtener la URL de la imagen
url1 = "https://cdn.urbantecno.com/rootear/2015/02/ejemplografo.jpg"

# Obtener la imagen desde la URL
response = requests.get(url1)
image1 = Image.open(BytesIO(response.content))


def info():
    st.header('¿Que es un Grafo?')
    st.write("Es una estrucura que consta de vertices y de aristas que conectan entre si esos vertices.")
    st.image(image1, use_column_width=True)
    st.write("Existen muchos tipos de Grafos, aqui tienes todos los tipos de grafos y sus definiciones:")
    st.subheader("Tipos de Grafos")
    tipografo = st.selectbox(f"Seleccione uno de los tipos de grafo: ", options=["Grafo simple", "Multigrafo", "Multigrafo Conexo", "Pseudografos","Grafos dirigidos","Multigrafo dirigido","Grafo no dirigido","Grafos bipartitos","Grafos bipartitos completos","Grafos ponderados","Grafos planos"], index=2, key=f"tipoarbol_")
    
    if tipografo == "Grafo simple":
        return st.subheader("Grafo simple") and st.write(" Consta de vertices y aristas no dirigidas; ademas cada arista conecta dos vertices distintos y no hay dos aristas que conecten un mismo par de vertices.") # Máxima prioridad
    elif tipografo == "Multigrafo":
        return st.subheader("Multigrafo") and st.write("Consta de vertices y aristas no dirigidas entre esos vertices , admite la existencia de aristas multiples entre pares de vertices (todo grafo simple es un multigrafo, pero no todos los multigrafos son grafos simples).") 
    elif tipografo == "Multigrafo Conexo":
        return st.subheader("Multigrafo Conexo") and st.write("contiene un circuito euleriano si, y solo si, cada uno de sus vertices tiene grado par; pero tiene un camino euleriano si, y solo si, tiene exactamente dos vertices de grado impar).") 
    elif tipografo == "Pseudografos":
        return st.subheader("Pseudografos") and st.write("Consta de aristas que pueden conectar un vertice consigo mismo (se necesitan asociar aristas a conjuntos que contengan un solo vertice).")
    elif tipografo == "Grafos dirigidos":
        return st.subheader("Grafos dirigidos") and st.write("Son pares ordenados donde se admiten bucles. Pares ordenados con sus dos elementos iguales, pero (NO se admiten aristas multiples en la misma direccion entre dos vertices).")
    elif tipografo == "Multigrafo dirigido":
        return st.subheader("Multigrafo dirigido") and st.write("Son aquellos que pueden tener aristas dirigidas multiples, desde un vertice a un segundo vertice.")
    elif tipografo == "Grafo no dirigido":
        return st.subheader("Grafo no dirigido") and st.write("Pueden tener aristas multiples y bucles.") 
    elif tipografo == "Grafos bipartitos":
        return st.subheader("Grafos bipartitos") and st.write("Tiene la propiedad de que su conjunto de vertices se puede dividir en dos subconjuntos disjuntos tales que cada arista conecta un vertice de uno de esos subconjuntos con un vertice del otro subconjunto.") 
    elif tipografo == "Grafos bipartitos completos":
        return st.subheader("Grafos bipartitos completos") and st.write("Es el grafo cuyo conjunto de vertices esta formado por dos subconjuntos con m y n vertices, respectivamente. Y hay una arista entre dos vertices si, y solo si, un vertice esta en el primer subconjunto y el otro vertice esta en el segundo subconjunto.") 
    elif tipografo == "Grafos ponderados":
        return st.subheader("Grafos ponderados") and st.write("Son aquellos en los que se asigna un numero a cada una de las aristas.") 
    elif tipografo == "Grafos planos":
        return st.subheader("Grafos planos") and st.write("El nivel de un nodo en un árbol indica su posición o profundidad dentro de la estructura. El nivel 0 es el nodo raíz y a medida que nos movemos hacia abajo, los niveles aumentan en incrementos de uno. El nivel de un nodo proporciona información sobre su posición relativa y distancia desde el nodo raíz.") 
    else:
        return 5
def aplicaciones():

    st.header("Aplicaciones de Grafos en la logistica")
    st.subheader("Rutas de transporte:")
    st.write("Los grafos pueden utilizarse para modelar y optimizar las rutas de transporte entre diferentes ubicaciones, como almacenes, centros de distribución, puntos de entrega y clientes. Los nodos del grafo representan las ubicaciones y las aristas representan las conexiones entre ellas. Con algoritmos de búsqueda de rutas, es posible encontrar la ruta óptima para la entrega de mercancías, minimizando la distancia recorrida o el tiempo de viaje.")
  




