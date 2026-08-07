import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

def laplaciano(L, h):
    '''
    Implementa el operador Lapaciano en 2D
    Para cada punto de A, se calula la derivada segunda de x, y
    Condiciones de borde periodicas: los valores fuera del dominio
                                    se conectan con el otro extremo

    '''
    A = np.zeros(L.shape)

      #Discretización en x
    A[1:-1, :] += (L[:-2, :] - 2 * L[1:-1, :] + L[2:, :]) / h**2

    A[0, :] += (L[-1, :] - 2 * L[0, :] + L[1, :]) / h**2  # Borde inferior
    A[-1, :] += (L[-2, :] - 2 * L[-1, :] + L[0, :]) / h**2  # Borde superior

      #Discretización en y
    A[:, 1:-1] += (L[:, :-2] - 2 * L[:, 1:-1] + L[:, 2:]) / h**2

    A[:, 0] += (L[:, -1] - 2 * L[:, 0] + L[:, 1]) / h**2  # Borde izquierdo
    A[:, -1] += (L[:, -2] - 2 * L[:, -1] + L[:, 0]) / h**2  # Borde derecho

    return A

def modelo_schnakenberg(t, U0, a , b , D_u, D_v):
        U, V = U0.reshape((2, m+1, m+1))

          # Laplaciano
        Lu = laplaciano(U, h)
        Lv = laplaciano(V, h)

          # Definimos las ecuaciones de reacción
        f_U = a - U + U**2 * V
        f_V = b - U**2 * V

          #Modelo
        dU = D_u * Lu + f_U 
        dV = D_v * Lv + f_V

        return np.concatenate([dU.ravel(), dV.ravel()])

  
  #Parámetros del modelo

A, B = 0, 100  # Dominio espacial
T = 20  # Tiempo total de simulación
m, n = 100, 200  # Pasos espaciales y temporales
h = (B - A) / m  # Tamaño del paso en el espacio

#Parametros para crear 
a, b, D_u, D_v = 0.01, 2, 1, 30 #Figura para "rayas"
#a, b, D_u, D_v = 0.01, 2, 1, 100 #Figura para "manchas"


  #Inicializar soluciones
# m es cantidad de intervalos
U_sol = np.zeros((m+1, m+1, n + 1))
V_sol = np.zeros((m+1, m+1, n + 1))

  #Condiciones iniciales en t=0
U_sol[:, :, 0] = np.random.rand(m+1, m+1) 
V_sol[:, :, 0] = np.ones((m+1, m+1)) 

  #condiciones iniciales para solve_ivp
  #.ravel convierte la matriz en un vector unidimensional
U0 = np.concatenate([U_sol[:, :, 0].ravel(), V_sol[:, :, 0].ravel()]) 

  #Resolver el sistema
t_span = (0, T)
t_eval = np.linspace(0, T, n + 1)
sol = solve_ivp(modelo_schnakenberg, t_span, U0, t_eval=t_eval,args=(a, b, D_u, D_v),method='RK45')

  #Reconstruir las soluciones en 3D
U_sol = sol.y[:(m+1)*(m+1), :].reshape((m+1, m+1, n + 1))
V_sol = sol.y[(m+1)*(m+1):, :].reshape((m+1, m+1, n + 1))

# GRAFICAMOS 
import matplotlib.animation as animation

duracion = 20 # en segundos, del render de la animación

fig = plt.figure()
ax_list = [fig.add_subplot(1,2,i+1, xlim=(A, B), ylim=(A, B)) for i in range(2)]

u_zero = U_sol[:,:,0]
v_zero = V_sol[:,:,0]

ax_list[0].set_title(f"Concentración de u")
ax_list[1].set_title(f"Concentración de v")

vmin = min(np.min(U_sol), np.min(V_sol))
vmax = max(np.max(U_sol), np.max(V_sol))

im_u = ax_list[0].imshow(u_zero, cmap='viridis', vmin=vmin, vmax=vmax)
im_v = ax_list[1].imshow(v_zero, cmap='viridis',  vmin=vmin, vmax=vmax)

def animate(k):
	im_u.set_array(U_sol[:,:,k])
	im_v.set_array(V_sol[:,:,k])
	return (im_u,im_v)

ani = animation.FuncAnimation(
	fig, animate, U_sol.shape[2], interval=duracion*1000/U_sol.shape[2], blit=True)

plt.show()