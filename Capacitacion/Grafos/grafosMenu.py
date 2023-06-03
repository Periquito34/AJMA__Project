import streamlit as st
from Capacitacion.Grafos.grafos import grafos
from Capacitacion.Grafos.informacion import info, aplicaciones
from Capacitacion.Grafos.grafosej import grafos
st.set_option('deprecation.showPyplotGlobalUse', False)
# Creamos el grafo

def grafos_menu():

    options = ["Paso 1: Conceptos", "Paso 2: Aplicaciones","Paso 3: Graficar Grafo"]
    selected_option = st.selectbox("Seleccione el paso a realizar", options)

    if selected_option == "Paso 1: Conceptos":
        # Código para la opción 1
        info()
    elif selected_option == "Paso 2: Aplicaciones":
        aplicaciones()
    elif selected_option == "Paso 3: Graficar Grafo":
        grafos()

    
