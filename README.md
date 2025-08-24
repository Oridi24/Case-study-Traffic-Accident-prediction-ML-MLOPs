# 🚦 *Predicción de la gravedad de los accidentes de tráfico*

⚠️ Actualmente trabajando en su desarrollo...
---


### 📌 *Objetivo*

*Desarrollar un sistema de clasificación predictiva que apoye en la toma de decisiones de seguridad vial, identificando patrones de riesgo en función de diversas variables (condiciones climáticas, defectos en la vía, alumbrado, hora, día y mes del accidente, entre otras)..*

### 📫 *Contenidos*

1. *Caso de estudio*: *Planteamiento del problema y objetivos del análisis.*
2. *Metodología de desarrollo*: *Enfoque de trabajo, fases del proyecto y técnicas aplicadas.*
3. *Desarrollo del análisis predictivo*: *Descripción del dataset (fuente: Kaggle), exploración inicial y preprocesamiento, ingeniería de características, codificación, balanceo, entrenamiento y validación del modelo.*
4. *Desarrollo de API*: *Creación de una API en FastAPI para exponer el modelo entrenado y despliegue del algoritmo.*
5. *Presentación del proyecto*: *Slides resumen con objetivos, metodología, resultados y conclusiones.*
6. *Grabación de la presentación*: *Video con la exposición del proyecto.*



 ### *Flujo de trabajo*
 
 1. ***EDA***: *análisis exploratorio y visualización de distribución de variables.*
 2. ***Preprocesamiento:***
     - *Codificación de variables categóricas con OneHotEncoder.*
     - *Transformación de variables temporales (hora, mes) a representación cíclica (seno y coseno).*
     - *Normalización de características.*
3. ***Entrenamiento de modelos de clasificación para predecir injury_severity.***
4. ***Evaluación y comparación de modelos.***

---
⚠️ ***Disclaimer***

*Este proyecto tiene fines únicamente académicos y de investigación. Los resultados obtenidos no deben interpretarse como una herramienta oficial de predicción de accidentes ni reemplazar el criterio de autoridades competentes en seguridad vial.*

*Los datos utilizados fueron obtenidos a través de Kaggle y el crédito de su extracción corresponde a su respectivo propietario.*

*Los modelos y análisis aquí presentados pueden contener limitaciones y no garantizan precisión en escenarios del mundo real.*
