# Regiones de Convergencia y Fractales en Sistemas No Lineales

**Análisis Numérico II**  
*Licenciatura en Matemática Aplicada · FAMAF, Universidad Nacional de Córdoba (2024)*

---

## 📌 Descripción

Estudio de la extensión del **Método de Newton para sistemas de ecuaciones no lineales en $\mathbb{R}^2$** y su aplicación al **Problema de Cayley** en el plano complejo. 

El trabajo analiza el comportamiento dinámico de las iteraciones del método al aproximar raíces complejas de polinomios de la forma $f(z) = z^n - 1$, evaluando sus cuencas de atracción y generando mapas de convergencia (fractales) que evidencian fronteras de comportamiento caótico (conjuntos de Julia y Fatou).

---

## 🔬 Metodología e Implementación Numérica

1. **Generalización de Newton a varias variables:**
   - Formulaci\u00f3n en $\mathbb{R}^2$: $J(x_k, y_k) \cdot \Delta X_k = -F(x_k, y_k)$, donde $J$ representa la matriz Jacobiana.
   - Reescritura de funciones complejas $f(z) = u(x,y) + i\,v(x,y)$ como sistemas de dos ecuaciones con dos incógnitas mediante la equivalencia topológica entre $\mathbb{C}$ y $\mathbb{R}^2$.

2. **Resolución del Problema de Cayley:**
   - Cálculo explícito del Jacobiano y resolución del sistema para $f(z) = z^3 - 1$.
   - Mapeo de convergencia sobre una grilla de puntos del plano complejo asignando colores según la raíz alcanzada ($z_1 = 1$, $z_2 = -\frac{1}{2} + \frac{\sqrt{3}}{2}i$, $z_3 = -\frac{1}{2} - \frac{\sqrt{3}}{2}i$).
   - Generalización para la función $f(z) = z^5 - 1$.

---

## 📊 Resultados y Visualización

- **Rápida convergencia:** Confirmación del orden cuadrático del método, alcanzando tolerancias de $\varepsilon < 10^{-6}$ en menos de 10 iteraciones.
- **Geometría fractal:** Generación de mapas de cuencas de atracción coloreadas por raíz final, revelando patrones fractales autosimilares y límites caóticos en los bordes de decisión.

---

## 🛠️ Palabras Clave y Herramientas

- **Conceptos:** Método de Newton, Sistemas No Lineales, Problema de Cayley, Cuencas de Atracción, Fractales (Julia/Fatou).
- **Lenguaje/Herramientas:** Python 3 (`numpy`, `matplotlib`), LaTeX.
