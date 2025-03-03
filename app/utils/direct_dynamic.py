#import matplotlib
#matplotlib.use('Qt5Agg')
import matplotlib.pyplot as plt
import numpy as np
#import obj_joints_links as jll
    
def transformation_relative_to_current_frame(links_list, joints_list):
    pass

def transformation_relative_to_origin_frame(links_list, joints_list):
    np.set_printoptions(precision=2, suppress=True)
    joints_positions = []
    toggle = False

    # Primera matriz de rotación y traslación
    matrix_rsl = np.dot(joints_list[0].rotation_matrix, links_list[0].translation_matrix)
    print (matrix_rsl)
    joints_positions.append(matrix_rsl[:, 3])
    # Demás trnasformaciónes rot->trans->rot->trans
    for i in range(len(links_list)-1):
        for dos in range(2):
            if toggle:
                matrix_rsl = np.dot(matrix_rsl, links_list[i+1].translation_matrix)
                joints_positions.append(matrix_rsl[:, 3]) # Extraemos el vector de posición
            else:
                matrix_rsl = np.dot(matrix_rsl, joints_list[i+1].rotation_matrix)
            print (matrix_rsl)   
            toggle ^= True

    # DEBUG
    print(joints_positions)
    return joints_positions

# if __name__ == "__main__":
#     J0 = jll.Joint(45, 'ro')
#     L0 = jll.Link(1)
#     J1 = jll.Joint(35, 'theta')
#     L1 = jll.Link(2)
#     J2 = jll.Joint(12, 'phi')
#     L2 = jll.Link(2)

#     links_list = [L0, L1, L2]
#     joints_list = [J0, J1, J2]
#     #point = np.array([[0], [0], [0], [1]])

#     np.set_printoptions(precision=2, suppress=True)
#     point_list = transformation_relative_to_origin_frame(links_list, joints_list)        

#     # Plot VECTORS
#     fig = plt.figure()
#     ax = fig.add_subplot(111, projection='3d')
#     ax.set_xlim([-10, 10])
#     ax.set_ylim([-10, 10])
#     ax.set_zlim([0, 10])
    
#     # Plot points
#     ax.scatter(0, 0, 0, color='r') # Origin

#     # Plot vector
#     plot_vector(point_list)

#     ax.set_xlabel('X')
#     ax.set_ylabel('Y')
#     ax.set_zlabel('Z')
#     plt.show()

