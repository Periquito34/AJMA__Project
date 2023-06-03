import streamlit as st
from graphviz import Digraph


def binomial_tree(root, children):
    """Crea un árbol binomial con una raíz y sus hijos"""
    G = Digraph(graph_attr={"rankdir": "TB", "rank": "center"})
    G.node(root)
    for child in children:
        G.node(child)
        G.edge(root, child)
    return G


def agregar_hijos(G, parent, nivel_actual, niveles_totales):
    if nivel_actual >= niveles_totales:
        return

    agregar_hijos_checkbox = st.checkbox(f"Agregar hijos para {parent}")
    if agregar_hijos_checkbox:
        num_hijos = st.number_input(
            f"Número de hijos para {parent}", min_value=0, step=1)
        for i in range(num_hijos):
            child = st.text_input(f"Hijo {i+1} de {parent}")
            if child:
                G.node(child)
                G.edge(parent, child)
                agregar_hijos(G, child, nivel_actual + 1, niveles_totales)


def graficarArbol():
    # Obtener la raíz del árbol binomial
    root = st.text_input("Raíz del árbol")

    # Obtener el número total de niveles del árbol
    niveles_totales = st.number_input(
        "Número total de niveles del árbol", min_value=1, step=1)

    aplicar = st.button("Aplicar")

    if aplicar:
        # Crear el árbol con la raíz inicial
        G = binomial_tree(root, [])

        # Guardar el árbol en el estado de la sesión
        st.session_state["arbol"] = G
        st.session_state["nodos"] = {root}
        st.success("El árbol ha sido generado correctamente.")


def agregar_hijo():
    # Obtener el árbol desde el estado de la sesión
    G = st.session_state.get("arbol")
    nodos = st.session_state.get("nodos")

    if not G:
        st.warning(
            "No se ha generado un árbol aún. Por favor, genere un árbol primero.")
        return

    padre = st.selectbox(
        "Seleccione el padre al que desea agregar un hijo", list(nodos))
    hijo = st.text_input("Ingrese el nombre del hijo a agregar")
    aplicar = st.button("Aplicar",  key="aplicandoAndo")

    if aplicar and hijo:
        G.node(hijo)
        G.edge(padre, hijo)
        nodos.add(hijo)
        # Actualizar el árbol en el estado de la sesión
        st.session_state["arbol"] = G
        # Actualizar el conjunto de nodos en el estado de la sesión
        st.session_state["nodos"] = nodos
        st.success(f"El hijo {hijo} ha sido agregado correctamente.")

    # Obtener el árbol desde el estado de la sesión
    G = st.session_state.get("arbol")
    nodos = st.session_state.get("nodos")

    if not G:
        st.warning(
            "No se ha generado un árbol aún. Por favor, genere un árbol primero.")
        return

    nodo = st.selectbox("Seleccione el nodo que desea eliminar", list(nodos))
    aplicar = st.button("Aplicar")

    if aplicar:
        G_copy = G.copy()  # Crear una copia del objeto Digraph

        # Eliminar el nodo y sus aristas del árbol copiado
        G_copy.node(nodo, None)
        G_copy.edges([edge for edge in G_copy.edges() if edge[0] != nodo])

        G_copy.remove_node(nodo)

        nodos.remove(nodo)  # Eliminar el nodo del conjunto de nodos
        # Actualizar el árbol en el estado de la sesión
        st.session_state["arbol"] = G_copy
        # Actualizar el conjunto de nodos en el estado de la sesión
        st.session_state["nodos"] = nodos
        st.success(f"El nodo {nodo} ha sido eliminado correctamente.")


def ver_grafico_arbol_general():
    # Obtener el árbol desde el estado de la sesión
    G = st.session_state.get("arbol")

    if not G:
        st.warning(
            "No se ha generado un árbol aún. Por favor, genere un árbol primero.")
        return

    st.graphviz_chart(G.source)

# Menú de opciones


def menu():
    option = st.selectbox("Seleccione una opción", ("Crear Arbol", "Agregar hijo",
                                                     "Ver Arbol"))

    if option == "Crear Arbol":
        graficarArbol()
    elif option == "Agregar hijo":
        agregar_hijo()
    elif option == "Ver Arbol":
        ver_grafico_arbol_general()
