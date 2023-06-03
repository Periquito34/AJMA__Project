import streamlit as st

from Capacitacion.Arboles.arbolesMenu import arboles_menu
from Capacitacion.Grafos.grafosMenu import grafos_menu

def menu_capacitacion():
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

    st.markdown('<p class="custom-header">CAPACITACIONES</p><br>', unsafe_allow_html=True)

    option = st.selectbox("Seleccione una opción", ("Grafos","Arboles"))

    if option == "Grafos":
        grafos_menu()
    elif option == "Arboles":
        arboles_menu()

    


