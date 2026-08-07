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

## 🔬 Modelos Estudiados y Comparativa

Se analizó la convergencia en discretizaciones temporales con $N = \{5, 10, 20, 40, 60, 80, 100, 200\}$ pasos para los siguientes parámetros de mercado:
$S_0 = 100$, $K = 100$, $r = 5\%$, $\sigma = 30\%$, $T = 4\text{ meses}$.

### 1. Modelos Binomiales (CRR vs. Tian Modificado - BIN)
| Aspecto | CRR (Clásico) | BIN (Tian Modificado) |
| :--- | :--- | :--- |
| **Varianza** | Correcta solo cuando $h \to 0$ | Correcta para cualquier $h$ |
| **3er Momento (Asimetría)** | No ajustado | Ajustado correctamente ($p u^3 + q d^3 = M^3 V^3$) |
| **Velocidad de Convergencia** | Más lenta | Más rápida |
| **Sensibilidad a volatilidad alta** | Se distorsiona | Se mantiene estable |

### 2. Modelos Trinomiales (Boyle vs. Tian Modificado - TRIN2)
| Aspecto | Boyle (Clásico) | TRIN2 (Tian Modificado) |
| :--- | :--- | :--- |
| **Precisión con pocos pasos $N$** | Estable | Más precisa (captura asimetría real) |
| **Costo Computacional** | $O(N^2)$ | $O(N^2)$ |
| **Probabilidades de Riesgo Neutral** | $p_u, p_m, p_d$ balanceados | $p_u, p_m, p_d$ adaptativos y desiguales |

---

## 📊 Conclusiones Principales

1. **Aceleración de Convergencia:** El ajuste de los tres momentos reduce sensiblemente las oscilaciones y el error relativo en función de $N$ respecto a la solución continua de Black-Scholes.
2. **Eficiencia Trinomial:** Aunque cada paso requiere mayor cómputo, los métodos trinomiales (especialmente **TRIN2**) ofrecen la mejor relación costo-beneficio computacional, alcanzando la exactitud deseada con muchos menos pasos que los binomiales.
3. **Opciones Americanas:** El modelo **BIN** ofrece mayor estabilidad que CRR para la opción *Put* americana en valores moderados de $N$, mientras que los esquemas trinomiales muestran la menor variabilidad temporal.

---

## 🛠️ Tecnologías Utilizadas

- **Lenguaje:** Python 3 (`numpy`, `scipy`, `matplotlib`)
- **Documentación:** LaTeX
