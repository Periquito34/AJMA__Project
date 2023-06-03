import matplotlib.pyplot as plt
import networkx as nx
import streamlit as st

G = nx.Graph()  # Grafo vacío

def add_port():
    puerto_nombre = st.text_input("Ingrese el nombre puerto")
    puerto_lugar = st.text_input("Ingrese el lugar donde se encuentra el puerto")
    puerto = f"{puerto_nombre} ({puerto_lugar})"
    
    
    aplicar = st.button("Aplicar")
    
    if aplicar:
        G.add_node(puerto)
        st.success(f"El puerto '{puerto}' ha sido agregado correctamente.")

def make_connection():
    puertos = list(G.nodes())
    seleccionados = st.multiselect("Seleccione los puertos para conectar", puertos)

    aplicar = st.button("Aplicar")
    
    if aplicar:
        for i in range(len(seleccionados) - 1):
            origen = seleccionados[i]
            destino = seleccionados[i + 1]
            G.add_edge(origen, destino)

        st.success("Las conexiones han sido creadas correctamente.")

def add_distance():
    conexiones = list(G.edges())
    seleccionadas = st.multiselect("Seleccione las conexiones a las que agregar distancia", conexiones)
    distancia = st.number_input("Ingrese la distancia:", step=1, value=1)

    aplicar = st.button("Aplicar")
    
    if aplicar:
        for conexion in seleccionadas:
            origen, destino = conexion
            G.edges[origen, destino]['weight'] = distancia

        st.success("Las distancias han sido actualizadas correctamente.")

def remove_element():
    option = st.selectbox("Seleccione el elemento a eliminar", ("Puerto", "Conexión"))

    if option == "Puerto":
        puerto = st.selectbox("Seleccione el puerto a eliminar", list(G.nodes()))
        
        aplicar = st.button("Aplicar")
        
        if aplicar:
            G.remove_node(puerto)
            st.success(f"El puerto '{puerto}' ha sido eliminado correctamente.")
    elif option == "Conexión":
        conexion = st.selectbox("Seleccione la conexión a eliminar", list(G.edges()))
        
        aplicar = st.button("Aplicar")
        
        if aplicar:
            G.remove_edge(*conexion)
            st.success("La conexión ha sido eliminada correctamente.")

def shortest_path():
    origen = st.selectbox("Seleccione el puerto de origen", list(G.nodes()))
    destino = st.selectbox("Seleccione el puerto de destino", list(G.nodes()))

    aplicar = st.button("Aplicar")
    
    if aplicar:
        shortest_path = nx.dijkstra_path(G, origen, destino)
        shortest_weight = nx.dijkstra_path_length(G, origen, destino)

        # Crear un grafo para mostrar el camino más corto
        shortest_path_graph = nx.Graph()
        shortest_path_graph.add_nodes_from(shortest_path)
        for i in range(len(shortest_path) - 1):
            origen = shortest_path[i]
            destino = shortest_path[i + 1]
            shortest_path_graph.add_edge(origen, destino, weight=G.edges[origen, destino]['weight'])

        # Visualizar el grafo del camino más corto
        pos = nx.spring_layout(shortest_path_graph)
        nx.draw_networkx(shortest_path_graph, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=10)
        labels = nx.get_edge_attributes(shortest_path_graph, 'weight')
        nx.draw_networkx_edge_labels(shortest_path_graph, pos, edge_labels=labels)
        plt.title("Camino más corto")
        plt.axis("off")
        st.pyplot()

def ver_grafo():
    # Visualizar el grafo general
    pos = nx.spring_layout(G)
    nx.draw_networkx(G, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=10)
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    plt.title("Grafo General")
    plt.axis("off")
    st.pyplot()

# Menú de opciones

def grafos():
    st.markdown(
    """
    <style>
    .custom-header {
        color: #31333F;
        font-size: 45px;
        font-weight: bold;
        text-align: center;
    }
    </style>
    """,
    unsafe_allow_html=True
    )

    st.markdown('<p class="custom-header">LOGISTICA DE RUTAS</p><br>', unsafe_allow_html=True)

    option = st.selectbox("Seleccione una opción", ("Añadir puerto", "Hacer conexión", "Añadir distancia",
                                                    "Eliminar elemento", "Camino más corto", "Ver grafo"))

    if option == "Añadir puerto":
        add_port()
    elif option == "Hacer conexión":
        make_connection()
    elif option == "Añadir distancia":
        add_distance()
    elif option == "Eliminar elemento":
        remove_element()
    elif option == "Camino más corto":
        shortest_path()
    elif option == "Ver grafo":
        ver_grafo()

