# Valoración de Opciones Financieras mediante Árboles de Tian

**Matemática Financiera**  
*Licenciatura en Matemática Aplicada · FAMAF, Universidad Nacional de Córdoba (Noviembre 2025)*  
**Autores:** Noelia Bocco, Luciana Ruiz

---

## 📌 Descripción

Estudio comparativo y análisis numérico de los modelos discretos de **Árboles Binomiales y Trinomiales Modificados de Tian (1993)** frente a los esquemas clásicos de **Cox-Ross-Rubinstein (CRR)** y **Boyle**. 

El trabajo evalúa la aceleración de convergencia, la precisión numérica y la estabilidad del cálculo en la valoración de:
- **Opciones Europeas (Call y Put):** Comparadas analíticamente con la solución continua del modelo de **Black-Scholes**.
- **Opciones Americanas (Put):** Analizando el comportamiento numérico ante la posibilidad de ejercicio anticipado.

Las versiones modificadas de Tian ajustan explícitamente los tres primeros momentos (media, varianza y asimetría) del proceso lognormal subyacente, manteniendo la estabilidad aun con un número reducido de pasos ($N$).

---

## 🛠️ Tecnologías Utilizadas

- **Lenguaje:** Python 3 (`numpy`, `scipy`, `matplotlib`)
- **Documentación:** LaTeX
