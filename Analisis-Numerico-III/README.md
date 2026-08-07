# Las Bases Químicas de la Morfogénesis: Patrones de Turing y Sistemas Reacción-Difusión

**Análisis Numérico III**  
*Licenciatura en Matemática Aplicada · FAMAF, Universidad Nacional de Córdoba (Noviembre 2024)*  
**Autores:** Noelia Bocco, Luciana Ruiz

---

## 📌 Descripción

Este trabajo estudia la teoría de **sistemas de reacción-difusión** expuesta por Alan Turing (1952) para explicar la morfogénesis biológica. El proyecto aborda cómo la interacción entre la cinética química no lineal y la difusión espacial de morfógenos puede generar patrones espaciales heterogéneos y estables a partir de inestabilidades impulsadas por la difusión ($D_A \neq D_B$).

Se realiza el proceso completo de **adimensionalización** del **modelo de Schnakenberg (1979)**, así como revisiones analíticas de los modelos de Gierer-Meinhardt (1972) y Thomas (1975).

---

## 🔬 Adimensionalización y Modelo Matemático

A partir del sistema bidimensional de reacción-difusión:
$$\frac{\partial A}{\partial t} = F(A,B) + D_A \nabla^2 A$$
$$\frac{\partial B}{\partial t} = G(A,B) + D_B \nabla^2 B$$

Aplicando el cambio de variables y escalado del modelo de Schnakenberg, se deriva el sistema adimensionalizado de ecuaciones acopladas:
$$\frac{\partial u}{\partial t} = a - u + u^2 v + \nabla^2 u$$
$$\frac{\partial v}{\partial t} = b - u^2 v + d \nabla^2 v$$

Donde:
- **$a, b$:** Fuentes constantes de producción de morfógenos.
- **$-u$:** Degradación lineal.
- **$u^2 v$:** Término no lineal de reacción/interacción clave para la inestabilidad de Turing.
- **$\nabla^2 u$, $d\nabla^2 v$:** Difusión espacial lineal y escala de difusión relativa ($d = D_v / D_u$).

---

## 💻 Implementación Numérica

El modelo bidimensional se implementó mediante el **Método de Líneas (Method of Lines)**:

1. **Discretización Espacial:** 
   - Esquema de **Diferencias Finitas centradas en 2D** para el operador Laplaciano $\nabla^2$.
   - **Condiciones de borde periódicas** integradas directamente en los límites del dominio.
2. **Integración Temporal:**
   - Resolución del sistema acoplado de EDOs resultantes mediante el método adaptativo **RK45** (`scipy.integrate.solve_ivp`).
3. **Simulaciones Interactivas:**
   - Exploración visual de cuencas y dinámicas de patrones mediante **VisualPDE**.

---

## 🛠️ Tecnologías Utilizadas

- **Lenguaje:** Python 3 (`numpy`, `scipy`, `matplotlib`)
- **Simulación Visual:** VisualPDE
- **Documentación:** LaTeX
