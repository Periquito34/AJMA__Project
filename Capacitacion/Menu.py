import matplotlib.pyplot as plt
import networkx as nx
import streamlit as st

from Capacitacion.Codificador.codificador import codificador
from Capacitacion.Grafos.grafos import grafos
from Capacitacion.Monticulos.monticulos_menu import monticulos_main
from Capacitacion.Menu_capacitacion.main_menu import menu_capacitacion


def run():

    st.markdown(
    """
    <style>
    body{
        background-color: #D0D0D0; /* Cambia el color aquí */
        color: #000000
    }
    </style>
    """,
    unsafe_allow_html=True
    )

    st.markdown(
    """
    <style>
    #MainMenu {
        visibility:hidden;
    }
    </style>
    """,
    unsafe_allow_html=True
    )

    st.markdown(
    """
    <style>
    header {
        visibility: hidden;
    }
    </style>
    """,
    unsafe_allow_html=True
    )

    st.set_option('deprecation.showPyplotGlobalUse', False)

    st.markdown(
    """
    <style>

    .css-6qob1r {
        background-color: #C8E2E8; /* Cambia el color aquí */
        z-index: 1;
    }
    .sidebar-title {
        color: #31333F;
        font-size: 24px;
        font-weight: bold;
        text-align: center;
    }
    .title-main{
        color: #31333F;
        font-size: 70px;
        text-align: center;
    
    }
    .sidebar-radio {
        margin-top: 30px;
        color: #C8E2E8;
        font-size: 24px;
        font-weight: bold;
        text-align: center;
    }
    </style>
    """,
    unsafe_allow_html=True
    )

    st.sidebar.markdown('<div class="sidebar"><p class="title-main">AJMA</p><h2 class="sidebar-title">Menu Principal</h2></div>', unsafe_allow_html=True)

    pagina = st.sidebar.radio('', ('Logistica','EPS', 'Decodificador','Capacitaciones'))

    if pagina == 'Logistica':
        grafos()
      
    elif pagina == 'EPS':
        monticulos_main()
    elif pagina == 'Decodificador':
        codificador()
    
    else:
        menu_capacitacion()
    
    
   
    st.sidebar.markdown('</div>', unsafe_allow_html=True)
