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
        st.write("En esta aplicación puedes visualizar la animación de robots en movimiento ingresado número de juntas, eslabones, y su respectivas rotaciones y longitudes.")

    with middle_column:
        st.subheader("Configuración de Eslabones y Juntas")

        num_links = st.number_input("Número de eslabones", min_value=2, max_value=10, value=2)
        links_list = []
        with st.expander("Configuración de eslabones"):
            for i in range(num_links):
                st.markdown(f"**Eslabón {i+1}**")
                length = st.number_input(f"Longitud del eslabón {i+1}", min_value=0.1, max_value=10.0, value=1.0)
                links_list.append(length)
                st.markdown("---")

        num_joints = num_links + 1
        joints_list = []
        with st.expander("Configuración de juntas"):
            for i in range(num_joints):
                st.markdown(f"**Junta {i}**")
                #CAMPTURAMOS LOS ÁNGULOS
                theta = st.number_input(f"Ángulo theta del eslabón {i}", min_value=-360.0, max_value=360.0, value=0.0)
                phi = st.number_input(f"Ángulo phi del eslabón {i}", min_value=-360.0, max_value=360.0, value=0.0)
                ro = st.number_input(f"Ángulo ro del eslabón {i}", min_value=-360., max_value=360.0, value=0.0)
                
                # CAPTURAMOS EL DESPLAZAMIENTO DE ACUERDO A LA LONGITUD DE LOS ESLABONES    
                # Operamos sobre las matrices para conocer los movimientos y posiciones correspondientes
                if i == 0: # Eslabón 0
                    joints_list.append(j.Eslabon(phi, ro, theta))
                    T_rslt = joints_list[0]  
                else : 
                    # punto3 = punto1 + vector_unitario * longitud_total    !VECTORES!
                    Vunit_x, _, _= T_rslt.unit_vect()
                    x, y, z = Vunit_x + Vunit_x * links_list[i-1]
                    
                    next_mov = j.Eslabon(phi, ro, theta, x, y, z) # nueva rotación y traslación

                    T_rslt = T_rslt @ next_mov # rotamos y nos trasladamos
                    joints_list.append(T_rslt)
                st.markdown("---")

        # Mostrar datos ingresados
        with st.expander("Datos ingresados"):
            for i in range(num_links):
                st.write(links_list[i])
            for i in range(num_joints):
                st.write(joints_list[i])

        # GRAFICAMOS EL ROBOT
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        points = []
        for eslabon in joints_list:
            # Obtiene los vectores unitarios y la posición del frame
            Xvect, Yvect, Zvect = eslabon.unit_vect()
            frame_ptn = eslabon.frame_position()
            points.append(frame_ptn) # Almacenamos las posiciones
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
        ax.plot(x_values, y_values, z_values, color='black', marker='*', markerfacecolor='black')

        # Configura los límites de los ejes
        ax.set_xlim([-8, 8])
        ax.set_ylim([8, -8])
        ax.set_zlim([0, 8])
        # Etiquetas de los ejes
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        # Muestra la gráfica en Streamlit
        st.pyplot(fig)