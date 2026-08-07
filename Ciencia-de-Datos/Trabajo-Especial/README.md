# Diseño de Geometría de Datos en $\mathbb{R}^5$ para Clasificación Comparativa

**Ciencia de Datos — Trabajo Especial**  
*Licenciatura en Matemática Aplicada · FAMAF, Universidad Nacional de Córdoba*  
**Autores:** Luciana Ruiz

---

## 📌 Descripción del Problema

El objetivo fundamental de este trabajo consiste en **diseñar sintéticamente la geometría y distribución de dos clases de datos en $\mathbb{R}^5$** para generar un comportamiento predeterminado en las métricas de tres algoritmos de clasificación:

1. **Regresión Logística (LR):** Obtener un *Accuracy* cercano al **$60\%$** ($\approx 0.60$).
2. **Random Forest (RF):** Mejorar sensiblemente hasta alcanzar un *Accuracy* cercano al **$85\%$** ($\approx 0.85$).
3. **Support Vector Machine (SVM):** Superar significativamente a los dos anteriores, logrando un rendimiento óptimo (**$> 85\%$**).

---

## 🔬 Planteo Geométrico y Justificación

Para cumplir con estas métricas específicas, se construyó una frontera de decisión no lineal compleja mediante las siguientes estrategias:

* **Incapacidad del Modelo Lineal (LR $\approx 0.60$):**  
  La Regresión Logística asume separabilidad mediante un hiperplano lineal en $\mathbb{R}^5$. Al introducir **no-linealidad severa y solapamiento intencional entre las clases**, el hiperplano queda limitado y solo logra clasificar correctamente cerca del $60\%$ de los puntos.

* **Aprovechamiento de Patrones Ortogonales (RF $\approx 0.85$):**  
  Random Forest captura relaciones no lineales mediante cortes ortogonales a los ejes coordenados. Al construir una geometría con estructuras tipo hipercubo o patrones no lineales por ejes, los árboles de decisión segmentan el espacio de manera mucho más eficiente alcanzando un $85\%$ de precisión.

* **Transformación mediante Kernel RBF (SVM $> 0.85$):**  
  Al proyectar los datos a un espacio de mayor dimensión mediante un **Kernel Gaussiano (RBF)**, la frontera de decisión suave y continua se vuelve hiperplana en dicho espacio transformado. Esto le permite a SVM adaptarse a superficies curvas en $\mathbb{R}^5$, superando significativamente las decisiones rígidas en forma de "caja" de Random Forest.

---

## 📊 Métricas de Rendimiento Esperadas

| Modelo | Comportamiento Geométrico | Target Accuracy |
| :--- | :--- | :---: |
| **Regresión Logística** | Hiperplano rígido en datos no separables linealmente | **$\approx 0.60$** |
| **Random Forest** | Umbrales ortogonales por ejes (Cortes en árbol) | **$\approx 0.85$** |
| **SVM (Kernel RBF)** | Frontera continua no lineal mediante mapeo suave | **$> 0.85$** |

---

## 🛠️ Tecnologías y Métodos Utilizados

* **Lenguaje:** Python 3
* **Librerías:** `numpy`, `pandas`, `scikit-learn` (`LogisticRegression`, `RandomForestClassifier`, `SVC`, `accuracy_score`, `roc_auc_score`)
* **Parámetros del Dataset:** $N = \text{DNI} / 100$ muestras generadas en $\mathbb{R}^5$.
