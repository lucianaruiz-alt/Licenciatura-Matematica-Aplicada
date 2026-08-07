# Evaluación de Generadores Pseudoaleatorios en la Simulación de un Sistema de Colas No Homogéneo

**Trabajo Práctico Especial — Modelos y Simulación**  
*Licenciatura en Matemática Aplicada · FAMAF, Universidad Nacional de Córdoba (Junio 2025)*  
**Autores:** Luciana Gimena Ruiz, Tiago Nesteruc

---

## 📌 Descripción

Estudio comparativo sobre el desempeño e impacto estadístico de tres generadores de números pseudoaleatorios (PRNG) en una simulación estocástica de eventos discretos:

1. **LCG** (Generador Congruencial Lineal)
2. **XORShift** (Operaciones de desplazamiento de bits)
3. **Mersenne Twister** (MT19937)

El modelo de aplicación corresponde a un **sistema de colas $M(t)/M/1$** simulado durante un periodo continuo de 48 horas. Las llegadas siguen un **proceso de Poisson no homogéneo** con tasa variable periódica $\lambda(t) = 30 + 30\sin\left(\frac{2\pi t}{24}\right)$ clientes/hora (simulado mediante el *método de rechazo*), y los tiempos de atención presentan una **distribución exponencial** ($\mu = 40$ clientes/hora).

---

## 🔬 Metodología e Implementación

- **Reimplementación de PRNGs:** Código desde cero para LCG ($a=16807, m=2^{31}-1$) y XORShift de 32 bits, comparados contra MT19937.
- **Simulación de Eventos Discretos:** Modelado de cola ilimitada con disciplina FIFO y servidor único.
- **Métricas Evaluadas:**
  - Porcentaje de utilización del servidor.
  - Tiempos de espera y tiempo total en el sistema.
  - Dinámica temporal de la longitud de la cola.
- **Validación Estadística:** Evaluación del ajuste de las distribuciones simuladas mediante la **prueba de Kolmogorov-Smirnov (K-S)**.

---


## 🛠️ Herramientas Utilizadas

- **Lenguaje:** Python 3
- **Librerías:** `numpy`, `math`, `matplotlib`, `scipy` (para validación estadística)
