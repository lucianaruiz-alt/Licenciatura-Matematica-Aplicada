# Sistema Predictivo de Deserción Universitaria y Perfilado de Estudiantes en Riesgo

**Ciencia de Datos**  
*Licenciatura en Matemática Aplicada · FAMAF, Universidad Nacional de Córdoba (Agosto 2026)*  
**Autores:** Noelia Bocco, Luciana Ruiz

---

## 📌 Descripción

Este proyecto aborda la identificación de factores clave asociados al abandono escolar, la permanencia y la graduación de estudiantes universitarios mediante técnicas de **Machine Learning**. 

A partir de un conjunto de datos heterogéneo con información académica, socioeconómica y demográfica de diversas disciplinas (Agronomía, Diseño, Educación, Periodismo, Administración, Servicios Sociales y Tecnología), se desarrolló un pipeline completo de análisis de datos para caracterizar y predecir el perfil de estudiantes en riesgo.

---

## 🔬 Flujo de Trabajo y Metodología

1. **Limpieza y Preparación de Datos:** 
   - Tratamiento de datos faltantes, codificación de variables categóricas y normalización/escalado de atributos numéricos.
2. **Análisis Exploratorio de Datos (EDA) y Visualización:** 
   - Estudio de correlaciones entre el rendimiento académico previo, situación socioeconómica y la tasa de retención.
3. **Reducción de Dimensionalidad:** 
   - Identificación de los atributos con mayor poder explicativo para reducir el ruido en el espacio de características.
4. **Modelado Predictivo (Clasificación Multiclase):** 
   - Entrenamiento de algoritmos supervisados para clasificar el estado final del estudiante (*Abandonó*, *En Cursada / Permanente*, *Graduado*).
   - Evaluación y ajuste mediante métricas como Accuracy, Precision, Recall y F1-Score macro/micro.

---

## 🛠️ Herramientas Utilizadas

- **Lenguaje:** Python 3
- **Librerías de Ciencia de Datos:** `pandas`, `numpy`, `scikit-learn`, `matplotlib`, `seaborn`
- **Entorno de Trabajo:** Jupyter Notebooks (`Abandono escolar.ipynb`)
- **Documentación:** LaTeX
