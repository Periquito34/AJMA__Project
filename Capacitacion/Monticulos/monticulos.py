import matplotlib.pyplot as plt
import networkx as nx
import streamlit as st
import heapq
import time
import pytz
import datetime

queue = []

def get_priority(item):
    urgency = item[5]  # Obtener la urgencia del paciente
    order = item[6]  # Obtener el campo adicional de orden (por ejemplo, hora de registro)
    
    if urgency == "Resucitacion (Codigo Rojo)":
        return (0, order)  # Máxima prioridad
    elif urgency == "Emergencia (Codigo Naranja)":
        return (1, order)  # Segunda prioridad
    elif urgency == "Urgencia (Codigo Amarillo)":
        return (2, order)  # Tercera prioridad
    elif urgency == "Urgencia Menor (Codigo Verde)":
        return (3, order)  # Cuarta prioridad
    elif urgency == "Sin Urgencia (Codigo Azul)":
        return (4, order)  # Cuarta prioridad
    else:
        return (5, order)  # Prioridad por defecto
    
def get_return(urgency):
    if urgency == "Resucitacion (Codigo Rojo)":
        return "Atencion de forma inmediata"  # Máxima prioridad
    elif urgency == "Emergencia (Codigo Naranja)":
        return "10-15 Min"  # Segunda prioridad
    elif urgency == "Urgencia (Codigo Amarillo)":
        return "60 Min"  # Tercera prioridad
    elif urgency == "Urgencia Menor (Codigo Verde)":
        return "2 Horas"  # Cuarta prioridad
    elif urgency == "Sin Urgencia (Codigo Azul)":
        return "4 Horas"  # Cuarta prioridad
    else:
        return 5  # Prioridad por defecto
    
def agregar_persona():
    # Mostrar el formulario para agregar personas
    with st.form("AgregarPersonaForm", clear_on_submit=True):
        st.subheader("Agregar un nuevo paciente")
        nuevo_nombre = st.text_input("Nombre")
        nuevo_apellido = st.text_input("Apellido")
        nuevo_identificacion = st.text_input("ID")
        nuevo_caso = st.text_input("Descripción de Urgencia")
        nuevo_urgencia = st.selectbox("Urgencia", options=["Resucitacion (Codigo Rojo)", "Emergencia (Codigo Naranja)", "Urgencia (Codigo Amarillo)", "Urgencia Menor (Codigo Verde)","Sin Urgencia (Codigo Azul)"], index=2)

        agregar_persona = st.form_submit_button("Agregar persona")

    # Verificar si se ha activado el botón "Agregar persona"
    if agregar_persona:
        # Obtener la hora de registro actual
        hora_registro = datetime.datetime.now()

        nuevo_item = (get_priority((0, 0, 0, 0, 0, nuevo_urgencia, hora_registro)), nuevo_nombre, nuevo_apellido, nuevo_identificacion, nuevo_caso, nuevo_urgencia, hora_registro)
        heapq.heappush(queue, nuevo_item)
        nuevo_nombre = ""
        nuevo_apellido = ""
        nuevo_identificacion = ""
        nuevo_caso = ""

        # Crear un espacio vacío para la alerta
        alert_placeholder = st.empty()
        # Mostrar la alerta de persona añadida correctamente
        alert_placeholder.success("Paciente agregado exitosamente.")
        # Esperar 3 segundos y luego limpiar la alerta
        time.sleep(3)
        alert_placeholder.empty()


def mostrar_lista():
    if len(queue) > 0:
        st.write("Pacientes en orden de prioridad:")

        for i, item in enumerate(queue):
            prioridad, nombre, apellido, identificacion, caso, urgencia, hora_registro = item

            hora_registro_str = hora_registro.strftime("%Y-%m-%d %H:%M:%S")

            st.write(
                f"| Nombre: {nombre} \n| Apellido: {apellido} \n| ID: {identificacion} \n| Urgencia: {urgencia} \n|"
                f"\n| Caso: {caso} | Tiempo de respuesta: {get_return(urgencia)} |"
                f"\n| Hora de Registro: {hora_registro_str} |"
            )

            # Generar clave única para el botón "Atender Paciente"
            key = f"atender_paciente_{i}"

            if st.button(f"Atender Paciente", key=key):
                queue.pop(i)

                alert_placeholder = st.empty()
                alert_placeholder.success("Atendiendo Paciente...")
                time.sleep(1.2)
                alert_placeholder.empty()

                st.experimental_rerun()

    else:
        st.write("No hay pacientes en la cola de prioridad.")


"""

def get_priority(urgency):
    if urgency == "Resucitacion (Codigo Rojo)":
        return 0  # Máxima prioridad
    elif urgency == "Emergencia (Codigo Naranja)":
        return 1  # Segunda prioridad
    elif urgency == "Urgencia (Codigo Amarillo)":
        return 2  # Tercera prioridad
    elif urgency == "Urgencia Menor (Codigo Verde)":
        return 3  # Cuarta prioridad
    elif urgency == "Sin Urgencia (Codigo Azul)":
        return 4  # Cuarta prioridad
    else:
        return 5  # Prioridad por defecto
    
def get_return(urgency):
    if urgency == "Resucitacion (Codigo Rojo)":
        return "Atencion de forma inmediata"  # Máxima prioridad
    elif urgency == "Emergencia (Codigo Naranja)":
        return "10-15 Min"  # Segunda prioridad
    elif urgency == "Urgencia (Codigo Amarillo)":
        return "60 Min"  # Tercera prioridad
    elif urgency == "Urgencia Menor (Codigo Verde)":
        return "2 Horas"  # Cuarta prioridad
    elif urgency == "Sin Urgencia (Codigo Azul)":
        return "4 Horas"  # Cuarta prioridad
    else:
        return 5  # Prioridad por defecto
    
def agregar_persona():
    # Mostrar el formulario para agregar personas
    with st.form("AgregarPersonaForm", clear_on_submit=True):
        st.subheader("Agregar un nuevo paciente")
        nuevo_nombre = st.text_input("Nombre")
        nuevo_apellido = st.text_input("Apellido")
        nuevo_identificacion = st.text_input("ID")
        nuevo_caso = st.text_input("Descripción de  Urgencia")
        nuevo_urgencia = st.selectbox("Urgencia", options=["Resucitacion (Codigo Rojo)", "Emergencia (Codigo Naranja)", "Urgencia (Codigo Amarillo)", "Urgencia Menor (Codigo Verde)","Sin Urgencia (Codigo Azul)"], index=2)

        agregar_persona = st.form_submit_button("Agregar persona")

    # Verificar si se ha activado el botón "Agregar persona"
    if agregar_persona:
        # Obtener la hora de registro actual
        hora_registro = datetime.datetime.now()

        nuevo_item = (get_priority(nuevo_urgencia), nuevo_nombre, nuevo_apellido, nuevo_identificacion, nuevo_caso, nuevo_urgencia, hora_registro)
        heapq.heappush(queue, nuevo_item)
        nuevo_nombre = ""
        nuevo_apellido = ""
        nuevo_identificacion = ""
        nuevo_caso = ""

        # Crear un espacio vacío para la alerta
        alert_placeholder = st.empty()
        # Mostrar la alerta de persona añadida correctamente
        alert_placeholder.success("Paciente agregado exitosamente.")
        # Esperar 3 segundos y luego limpiar la alerta
        time.sleep(3)
        alert_placeholder.empty()


def mostrar_lista():
    if len(queue) > 0:
        st.write("Pacientes en orden de prioridad:")

        for i, item in enumerate(queue):
            prioridad, nombre, apellido, identificacion, caso, urgencia, hora_registro = item

            hora_registro_str = hora_registro.strftime("%Y-%m-%d %H:%M:%S")

            st.write(
                f"| Nombre: {nombre} \n| Apellido: {apellido} \n| ID: {identificacion} \n| Urgencia: {urgencia} \n|"
                f"\n| Caso: {caso} | Tiempo de respuesta: {get_return(urgencia)} |"
                f"\n| Hora de Registro: {hora_registro_str} |"
            )

            # Generar clave única para el botón "Atender Paciente"
            key = f"atender_paciente_{i}"

            if st.button(f"Atender Paciente", key=key):
                queue.pop(i)

                alert_placeholder = st.empty()
                alert_placeholder.success("Atendiendo Paciente...")
                time.sleep(1.2)
                alert_placeholder.empty()

                st.experimental_rerun()

    else:
        st.write("No hay pacientes en la cola de prioridad.")


def mostrar_lista():
    if len(queue) > 0:
        st.write("Pacientes en orden de prioridad:")

        # Mostrar los datos de las personas en orden de prioridad
        for i, item in enumerate(queue):
            prioridad, nombre, apellido, identificacion, caso, urgencia, hora_registro = item

            # Formatear la hora de registro como una cadena de texto
            hora_registro_str = hora_registro.strftime("%Y-%m-%d %H:%M:%S")

            st.write(
                f"| Nombre: {nombre} \n| Apellido: {apellido} \n| ID: {identificacion} \n| Urgencia: {urgencia} \n|"
                f"\n| Caso: {caso} | Tiempo de respuesta: {get_return(urgencia)} |"
                f"\n| Hora de Registro: {hora_registro_str} |"
            )

            # Verificar si se ha activado el botón "Atender Paciente"
            
            if st.button(f"Atender Paciente", key="atender_paciente"):
                # Eliminar la persona de la cola de prioridad
                queue.pop(i)
                # Recargar la página para actualizar la interfaz

                alert_placeholder = st.empty()
                # Mostrar la alerta de eliminación exitosa
                alert_placeholder.success("Atendiendo Paciente...")
                # Esperar 3 segundos y luego limpiar la alerta
                time.sleep(1.2)
                alert_placeholder.empty()     
                st.experimental_rerun()

    else:
        st.write("No hay pacientes en la cola de prioridad.")

"""