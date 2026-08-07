# Formulación de un Sudoku mediante Programación Lineal Entera Binaria (BILP) en Julia y Python

**Investigación Operativa**  
*Licenciatura en Matemática Aplicada · FAMAF, Universidad Nacional de Córdoba (Junio 2026)*  
**Autores:** Noelia Bocco, Luciana Ruiz

---

## 📌 Descripción

Este trabajo aborda la formulación y resolución del juego **Sudoku ($9 \times 9$)** transformándolo en un problema de **Programación Lineal Entera Binaria (BILP)**. 

Las reglas clásicas del juego (unicidad de dígitos por celda, fila, columna y subcuadrícula $3 \times 3$) se traducen formalmente a un sistema de restricciones lineales sobre variables de decisión binarias $x_{i,j,k} \in \{0, 1\}$, permitiendo resolver el tablero mediante solvers de optimización matemática sin necesidad de algoritmos heurísticos o de *backtracking* dedicados.

---

## 🔬 Modelo Matemático (BILP)

Sea la variable binaria $x_{i,j,k} = 1$ si la celda en la fila $i$ y columna $j$ contiene el número $k$, y $0$ en otro caso ($i, j, k \in \{1, \dots, 9\}$):

1. **Unicidad por Celda:** Cada celda contiene exactamente un número.
   $$\sum_{k=1}^9 x_{i,j,k} = 1 \quad \forall i, j$$

2. **Unicidad por Fila:** Cada número aparece exactamente una vez por fila.
   $$\sum_{j=1}^9 x_{i,j,k} = 1 \quad \forall i, k$$

3. **Unicidad por Columna:** Cada número aparece exactamente una vez por columna.
   $$\sum_{i=1}^9 x_{i,j,k} = 1 \quad \forall j, k$$

4. **Unicidad por Subcuadrícula ($3 \times 3$):** Cada número aparece una vez por bloque.
   $$\sum_{i=3a-2}^{3a} \sum_{j=3b-2}^{3b} x_{i,j,k} = 1 \quad \forall k, \; a,b \in \{1,2,3\}$$

5. **Pistas Iniciales:** Fijación de variables $x_{i,j,k} = 1$ para los valores predeterminados del tablero.

---

## 🛠️ Herramientas Utilizadas

- **Lenguajes:** Julia, Python 3
- **Librerías de Optimización:** `JuMP.jl`, `PuLP`
- **Documentación:** LaTeX
