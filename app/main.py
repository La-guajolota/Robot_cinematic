import streamlit as st
import matplotlib.pyplot as plt

#Funcines

# Configuración de la página
st.set_page_config(
    page_title="Animación de robots",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Diseño y contenido
with st.container():
    left_column, middle_column = st.columns([1,3])

    with left_column:
        st.header("Simulación de movimiento de robots 🤖")
        st.write("En esta aplicación puedes visualizar la animación de robots en movimiento ingresado número de juntas, eslabones, y su respectivas rotaciones y longitudes.")

    with middle_column:
        st.subheader("Configuración de Eslabones y Juntas")

        num_links = st.number_input("Número de eslabones", min_value=2, max_value=10, value=1)
        links_list = []
        with st.expander("Configuración de eslabones"):
            for i in range(num_links):
                st.markdown(f"**Eslabón {i+1}**")
                length = st.number_input(f"Longitud del eslabón {i+1}", min_value=0.1, max_value=10.0, value=1.0)
                axis = st.selectbox(f"Eje donde posa el eslabón{i+1}", ['theta', 'phi', 'ro'])
                st.markdown("---")

        num_joints = num_links
        joints_list = []
        with st.expander("Configuración de juntas"):
            for i in range(num_joints):
                st.markdown(f"**Junta {i+1}**")
                angle = st.number_input(f"Ángulo de la junta {i+1}", min_value=0.0, max_value=360.0, value=0.0)
                st.markdown("---")

        # Mostrar datos ingresados
        with st.expander("Datos ingresados"):
            for i in range(num_links):
                st.write(links_list[i])
            for i in range(num_joints):
                st.write(joints_list[i])