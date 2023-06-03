import streamlit as st


from Capacitacion.Monticulos.monticulos import agregar_persona, mostrar_lista

def monticulos_main():
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

    st.markdown('<p class="custom-header">PRIORIDADES EPS</p><br>', unsafe_allow_html=True)

    option = st.selectbox("Seleccione una opción", ("Agregar Persona","Ver lista (Cola de prioridad)"))

    if option == "Agregar Persona":
        agregar_persona()
    elif option == "Ver lista (Cola de prioridad)":
        mostrar_lista()
