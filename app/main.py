import streamlit as st
from utils import direct_dynamic as dd
from utils import obj_joints_links as jl
import matplotlib.pyplot as plt

#Funcines
def plot_points(joints_list):
    for point in joints_list:
        ax.scatter(point[0], point[1], point[2], color='g')

def plot_vector(joints_list):
    ax.quiver(0, 0, 0, joints_list[0][0], joints_list[0][1], joints_list[0][2], color='b')

    if len(joints_list) >= 2:
        for n in range(len(joints_list) - 1):
            ax.quiver(joints_list[n][0], joints_list[n][1], joints_list[n][2], 
                      joints_list[n+1][0] - joints_list[n][0], 
                      joints_list[n+1][1] - joints_list[n][1], 
                      joints_list[n+1][2] - joints_list[n][2], color='b')

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

        num_links = st.number_input("Número de eslabones", min_value=1, max_value=10, value=1)
        links_list = []
        with st.expander("Configuración de eslabones"):
            for i in range(num_links):
                st.markdown(f"**Eslabón {i+1}**")
                length = st.number_input(f"Longitud del eslabón {i+1}", min_value=0.1, max_value=10.0, value=1.0)
                axis = st.selectbox(f"Eje donde posa el eslabón{i+1}", ['theta', 'phi', 'ro'])
                links_list.append(jl.Link(length, axis))
                st.markdown("---")

        num_joints = num_links
        joints_list = []
        with st.expander("Configuración de juntas"):
            for i in range(num_joints):
                st.markdown(f"**Junta {i+1}**")
                angle = st.number_input(f"Ángulo de la junta {i+1}", min_value=0.0, max_value=360.0, value=0.0)
                #axis = st.selectbox(f"Eje de rotación de la junta {i+1}", ['theta', 'phi', 'ro'])
                joints_list.append(jl.Joint(angle, axis))
                st.markdown("---")

        # Mostrar datos ingresados
        with st.expander("Datos ingresados"):
            for i in range(num_links):
                st.write(links_list[i])
            for i in range(num_joints):
                st.write(joints_list[i])

        #Calculamos el movimiento de los eslabones y juntas
        point_list = dd.transformation_relative_to_origin_frame(links_list, joints_list)        

        # Plot VECTORS
        fig = plt.figure(figsize=(10, 6))
        ax = fig.add_subplot(111, projection='3d')
        ax.set_xlim([-5, 5])
        ax.set_ylim([5, -5])
        ax.set_zlim([0, 5])

        # Plot points
        ax.scatter(0, 0, 0, color='r')  # Origin

        # Plot vector
        plot_points(point_list)
        plot_vector(point_list)

        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        st.pyplot(fig, use_container_width=True)