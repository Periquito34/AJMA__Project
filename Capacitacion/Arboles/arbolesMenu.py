import matplotlib.pyplot as plt
import networkx as nx
import streamlit as st
from Capacitacion.Arboles.informacion import info, Aplicaciones_de_arboles
from Capacitacion.Arboles.arbolesTDA import menu
st.set_option('deprecation.showPyplotGlobalUse', False)
# Creamos el grafo


def arboles_menu():

    st.subheader('Arboles')

    options = ["Paso 1: Conceptos",
               "Paso 2: Aplicaciones", "Paso 3: Graficar Arbol"]
    selected_option = st.selectbox("Seleccione el paso a realizar", options)

    if selected_option == "Paso 1: Conceptos":
        info()
    elif selected_option == "Paso 2: Aplicaciones":
        Aplicaciones_de_arboles()
    elif selected_option == "Paso 3: Graficar Arbol":
        menu()
