import matplotlib.pyplot as plt
import networkx as nx
import streamlit as st

def grafos():
    # Crear un grafo vacío
    G = nx.Graph()

    cantidadCiudades = st.number_input("Ingrese el número de ciudades que va a registrar: ", step=1)

    ciudades = []
    for i in range(int(cantidadCiudades)):
        ciudad_container = st.empty()  # Contenedor para la entrada de la ciudad

        ciudad = ciudad_container.text_input(f"Ingrese el Nombre de la Ciudad {i+1}", key=f"conexion_input_{i}")
        ciudades.append(ciudad)

        if ciudad:
            G.add_node(ciudad)
            st.success("Ciudad Agregada")
        else:
            st.warning("La Ciudad ya existe en el grafo")
            break
        ciudad_container.empty()

    conexiones = []

    # Conectar ciudades seleccionadas
    for i in range(int(cantidadCiudades)-1):

        seleccionadas = st.multiselect("Seleccione las ciudades para conectar", ciudades, key=f"ciudad_input_{i}")
        peso = st.number_input("Ingrese el peso para la conexión:", step=1, value=1, key=f"ciudad_peso_{i}")
        for j in range(len(seleccionadas) - 1):
            origen = seleccionadas[j]
            destino = seleccionadas[j + 1]
            G.add_edge(origen, destino, weight=peso)
            conexiones.append((origen, destino))


    # Visualizamos el grafo
    pos = nx.spring_layout(G)
    nx.draw_networkx_nodes(G, pos, node_size=500)
    nx.draw_networkx_edges(G, pos)
    nx.draw_networkx_labels(G, pos, font_size=5, font_family="sans-serif")
    nx.draw_networkx_edges(G, pos, edgelist=conexiones, edge_color='r', width=2)  # Conexiones en rojo
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    plt.axis("off")

    # Mostramos la visualización en Streamlit
    st.pyplot()

