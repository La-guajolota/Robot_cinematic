"""
Simulación de Movimiento de Robots

Este script utiliza Streamlit para crear una interfaz gráfica que permite la configuración y visualización
de la animación de robots en movimiento. Los usuarios pueden ingresar el número de juntas y eslabones, así
como sus respectivas rotaciones y longitudes, para ver cómo se desplaza el robot en un espacio tridimensional.

Autor: Adrián Silva Palafox
Fecha: 11 Marzo 2025
"""

import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from utils import joint_obj as j

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
        st.write("En esta aplicación puedes visualizar la animación de robots en movimiento ingresando el número de juntas, eslabones, y sus respectivas rotaciones y longitudes.")

    with middle_column:
        st.subheader("Configuración de Eslabones y Juntas")

        # Configuración de eslabones
        num_links = st.number_input("Número de eslabones", min_value=2, max_value=10, value=2)
        links_list = []
        with st.expander("Configuración de eslabones"):
            for i in range(num_links):
                st.markdown(f"**Eslabón {i+1}**")
                length = st.number_input(f"Longitud del eslabón {i+1}", min_value=0.1, max_value=10.0, value=1.0)
                links_list.append(length)
                st.markdown("---")

        # Configuración de juntas
        num_joints = num_links + 1
        joints_list = []
        with st.expander("Configuración de juntas"):
            for i in range(num_joints):
                st.markdown(f"**Junta {i}**")
                theta = -st.number_input(f"Ángulo theta del eslabón {i}", min_value=-360.0, max_value=360.0, value=0.0)
                phi = -st.number_input(f"Ángulo phi del eslabón {i}", min_value=-360.0, max_value=360.0, value=0.0)
                ro = -st.number_input(f"Ángulo ro del eslabón {i}", min_value=-360., max_value=360.0, value=0.0)
                
                # Capturamos el desplazamiento de acuerdo a la longitud de los eslabones
                if i == 0:  # Eslabón 0
                    joints_list.append(j.Eslabon(phi, ro, theta))
                    T_rslt = joints_list[0]  
                else:
                    # Calculamos el desplazamiento utilizando vectores unitarios
                    Vunit_x, _, _ = joints_list[i-1].unit_vect()
                    x, y, z = Vunit_x + Vunit_x * links_list[i-1]
                    
                    next_mov = j.Eslabon(phi, ro, theta, x, y, z)  # Nueva rotación y traslación
                    T_rslt = next_mov @ T_rslt  # Rotamos y nos trasladamos
                    joints_list.append(T_rslt)
                st.markdown("---")

        # Mostrar datos ingresados
        with st.expander("Datos ingresados"):
            for i in range(num_links):
                st.write(links_list[i])
            for i in range(num_joints):
                st.write(joints_list[i])

        # Graficamos el robot
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        points = []
        for eslabon in joints_list:
            # Obtiene los vectores unitarios y la posición del frame
            Xvect, Yvect, Zvect = eslabon.unit_vect()
            frame_ptn = eslabon.frame_position()
            points.append(frame_ptn)  # Almacenamos las posiciones
            print(f"{eslabon} - Frame position:", frame_ptn)

            # Grafica los vectores unitarios
            ax.quiver(frame_ptn[0], frame_ptn[1], frame_ptn[2], Xvect[0], Xvect[1], Xvect[2], color='r')
            ax.quiver(frame_ptn[0], frame_ptn[1], frame_ptn[2], Yvect[0], Yvect[1], Yvect[2], color='b')
            ax.quiver(frame_ptn[0], frame_ptn[1], frame_ptn[2], Zvect[0], Zvect[1], Zvect[2], color='g') 
        print()

        # Unimos los puntos
        x_values = [point[0] for point in points]
        y_values = [point[1] for point in points]
        z_values = [point[2] for point in points]
        ax.plot(x_values, y_values, z_values, color='black', marker='o', markersize=5, markerfacecolor='black')

        # Imprime el último punto
        if points:
            st.write(f"Último punto: {points[-1]}")

        # Configura los límites de los ejes
        ax.set_xlim([-5, 5])
        ax.set_ylim([5, -5])
        ax.set_zlim([0, 5])
        # Etiquetas de los ejes
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        # Muestra la gráfica en Streamlit
        st.pyplot(fig) 