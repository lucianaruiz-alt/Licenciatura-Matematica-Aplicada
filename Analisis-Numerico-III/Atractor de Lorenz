# El Atractor de Lorenz y la Geometría del Caos

**Análisis Numérico III**  
*Licenciatura en Matemática Aplicada · FAMAF, Universidad Nacional de Córdoba*  
**Autores:** Luciana Ruiz

---

## 📌 Descripción

Este trabajo aborda la simulación y análisis numérico del **Sistema de Lorenz**, un modelo dinámico no lineal simplificado para la convección atmosférica. A través de la integración de sus ecuaciones diferenciales ordinarias (EDOs), se explora la aparición de comportamientos caóticos, la sensibilidad extrema a las condiciones iniciales (*Efecto Mariposa*) y la estructura de su atractor extraño.

Además, se implementó un análisis de trayectoria seleccionando puntos de partida arbitrarios en el espacio tridimensional para observar la dinámica de convergencia de las órbitas hacia las dos alas del atractor.

---

## 🔬 Modelo Matemático

El sistema está gobernado por las siguientes tres ecuaciones no lineales acopladas:

$$\frac{dx}{dt} = \sigma (y - x)$$
$$\frac{dy}{dt} = x (\rho - z) - y$$
$$\frac{dz}{dt} = x y - \beta z$$

### Parámetros Clásicos de Lorenz:
- **$\sigma = 10$** (Número de Prandtl)
- **$\rho = 28$** (Número de Rayleigh)
- **$\beta = 8/3$** (Factor geométrico)

Bajo estos parámetros, el sistema carece de un punto fijo de equilibrio estable al que converjan las trayectorias a largo plazo; en su lugar, la solución oscila indefinidamente dentro de una región acotada del espacio de fases $(\mathbb{R}^3)$ llamada **Atractor de Lorenz**.

---

## 💻 Metodología e Implementación

1. **Integración Numérica:**
   - Implementación de esquemas de integración temporal (Runge-Kutta de orden 4 / `solve_ivp` de SciPy) para resolver las trayectorias en $3D$.
2. **Análisis de Sensibilidad y Órbitas:**
   - Selección de condición(es) inicial(es) $(x_0, y_0, z_0)$ para rastrear la evolución temporal $(x(t), y(t), z(t))$.
   - Visualización del proceso de atracción: cómo puntos lejanos del espacio de fases son atraídos rápidamente hacia la estructura con forma de "mariposa" y oscilan entre sus dos lóbulos sin repetirse jamás.

---

## 📊 Resultados y Visualización

- **Visualización 3D:** Generación de gráficos de fase $x-y-z$ que muestran las órbitas completas envolviendo ambos núcleos atractores.
- **Divergencia de Trayectorias:** Comprobación de que dos puntos iniciales infinitamente cercanos terminan separándose exponencialmente en el tiempo debido a la naturaleza caótica del sistema.

