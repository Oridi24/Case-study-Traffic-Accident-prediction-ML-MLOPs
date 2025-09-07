#  *Predicción de la gravedad de los accidentes de tráfico* 🚦

## 🔎 *Descripción del caso de estudio*
*La siniestralidad vial es un problema con gran impacto social y económico. Poder anticipar la **severidad de un accidente** permite a las autoridades y servicios de emergencia **optimizar la asignación de recursos** y diseñar medidas de prevención más efectivas.*  

*Este proyecto desarrolla un modelo predictivo robusto de clasificación binaria con técnicas de **Machine Learning** capaz de predecir si un accidente de tráfico será **leve (0)** o **grave (1)**, a partir de información contextual (condiciones de la vía, hora, día de la semana, número de vehículos implicados, etc.)*. *El modelo final se despliega mediante **FastAPI**, ofreciendo un servicio accesible para realizar predicciones en tiempo real.*
*Esto permite:*
 - *Identificar accidentes de alto riesgo.*
 - *Priorizar recursos de atención y prevención vial.*
 - *Integrar un modelo ML en un sistema de alerta en tiempo real.*

---

## 📂 *Estructura del Repositorio*: *Contenidos*

1. *Caso de estudio*: *Planteamiento del problema y objetivos del análisis.*
2. *Metodología de desarrollo*: *Enfoque de trabajo, fases del proyecto y técnicas aplicadas.*
3. *Desarrollo del análisis predictivo*: *Descripción del dataset (fuente: Kaggle), exploración inicial y preprocesamiento, ingeniería de características, codificación, balanceo, entrenamiento y validación del modelo.*
4. *Desarrollo de API*: *Creación de una API en FastAPI para exponer el modelo entrenado y despliegue del algoritmo.*
5. *Presentación del proyecto*: *Slides resumen con objetivos, metodología, resultados y conclusiones.*
6. *Grabación de la presentación*: *Video con la exposición del proyecto.*

---

##  💾 *Dataset*

*El dataset incluye **167.444 registros** de accidentes, con variables como:*

- *Características del accidente: tipo de choque, número de unidades involucradas.*
- *Condiciones de tráfico: control de tráfico, visibilidad, superficie de la carretera.*
- *Condiciones climáticas: lluvia, nieve, niebla, hielo.*
- *Variables temporales: hora, día de la semana, mes.*

⚠️ ***Observación:** Dataset desbalanceado (~80% leve, ~20% grave).*

---

## 🧠 *Desarrollo*

### 1. ***Preprocesamiento:***
   - *Selección de variables relevantes.*
   - *Codificación de variables categóricas y temporales.*
   - *No se gestionaron outliers para evitar eliminar la clase minoritaria.*
     
  
### 2. ***Métricas de evaluación:***  
| ***Métrica***                 | ***Explicación Breve*** |
|---------------------------|-----------------|
| *Precision*               | *Mide la proporción de predicciones positivas que fueron correctas. Responde a la pregunta: "De todas las que mi modelo dijo que eran positivas, ¿cuántas lo fueron realmente?"* |
| *Recall (Sensibilidad)*   | *Mide la proporción de casos positivos reales que el modelo identificó correctamente. Responde a la pregunta: "De todos los casos positivos que había, ¿cuántos encontró mi modelo?"* |
| *F1-score*                | *Es la media armónica de Precision y Recall. Es útil para encontrar un equilibrio entre ambas métricas, especialmente en clases desbalanceadas, ofreciendo un solo valor que las resume.* |
| *ROC-AUC*                 | *Mide la capacidad del modelo para distinguir entre clases. El valor representa la probabilidad de que el modelo clasifique un ejemplo positivo elegido al azar por encima de un ejemplo negativo elegido al azar. Un valor de 1.0 es perfecto, 0.5 es aleatorio.* |
| *Average Precision (AP)*  | *Mide el área bajo la curva de Precision-Recall. Es especialmente relevante para clases desbalanceadas (como la clase "grave"), ya que se centra en la capacidad del modelo para identificar correctamente los casos positivos sin importar cuántos negativos se predigan.* |


### 3. ***Modelos evaluados:***
| ***Modelo***             | ***Explicación Breve** |
|-------------------|-----------------|
| *Decision Tree*    | *Un modelo que toma decisiones secuenciales al dividir los datos según diferentes características. Funciona como un diagrama de flujo, donde cada nodo representa una prueba sobre una característica y cada rama la salida de esa prueba. Es fácil de interpretar.* |
| *Random Forest*    | *Un "bosque" de árboles de decisión. Construye múltiples árboles y promedia sus resultados para obtener una predicción final. Reduce el sobreajuste y mejora la precisión en comparación con un solo árbol de decisión.* |
| *Gradient Boosting*| *Un modelo de conjunto que construye árboles de decisión de forma secuencial. Cada nuevo árbol se entrena para corregir los errores del árbol anterior. Se centra en los errores de las predicciones previas, mejorando el rendimiento de forma incremental.* |
| *XGBoost (eXtreme Gradient Boosting)* | *Una implementación optimizada y altamente eficiente de Gradient Boosting. Es conocido por su velocidad y rendimiento, ya que incluye regularización para evitar el sobreajuste y maneja bien los valores perdidos.* |
| *LogReg class_weight* | *Un método para la regresión logística (LogReg) que ajusta los pesos de las clases. Se utiliza para dar más importancia a la clase minoritaria durante el entrenamiento, lo que ayuda a mitigar el problema del desequilibrio de clases.* |
| *LogReg SMOTE*     | *Un método que combina la regresión logística con SMOTE (Synthetic Minority Over-sampling Technique). SMOTE crea ejemplos sintéticos de la clase minoritaria para equilibrar el conjunto de datos antes de entrenar el modelo, mejorando su capacidad para predecir correctamente la clase minoritaria.* |
| *Balanced RF*      | *Una variante de Random Forest que aborda el desequilibrio de clases. Durante la construcción de cada árbol, utiliza un subconjunto de la clase mayoritaria de forma aleatoria para igualar el número de ejemplos con la clase minoritaria.* |
| *Easy Ensemble*    | *Un algoritmo de conjunto que crea varios subconjuntos de datos, cada uno con una fracción de la clase mayoritaria y todos los ejemplos de la clase minoritaria. Entrena un clasificador para cada subconjunto y combina sus predicciones para la clasificación final.* |


### 4. ***Técnicas de validación cruzada:***
   - ***StratifiedKFold** para modelos de ensamble con clase minoritaria.*
   - ***GridSearchCV** para búsqueda de hiperparámetros en Logistic Regression y Random Forest.*

---


##  📌 *Conclusiones generales:*

| ***Modelo***                     | ***Split*** | ***Accuracy*** | ***F1-score*** | ROC-AUC | ***Average Precision*** | ***Interpretación Breve*** |
|----------------------------|-------|----------|----------|---------|-----------------|--------------------|
| *Balanced Random Forest*   | Train | 0.8873   | 0.7700   | 0.9987  | 0.9937          | *Alta capacidad de detección de accidentes graves (recall ~0.88). Sobreajuste moderado debido al desbalance; mitigable con técnicas como SMOTE si se requiere.* |
|                            | Test  | 0.7681   | 0.5920   | 0.8600  | 0.4644          | *Predicción robusta para clase minoritaria, buen equilibrio entre precisión y recall.* |
| *Easy Ensemble*            | Test  | 0.7490   | 0.6038   | 0.8563  | 0.4575          | *Resultados similares a Balanced RF, menor estabilidad y capacidad de generalización.* |
| *Logistic Regression*      | Test  | 0.7492   | 0.6039   | 0.8640  | 0.4838          | *Buena detección de la clase minoritaria pero menor flexibilidad frente a patrones complejos.* |
| *Random Forest*            | Test  | 0.8084   | 0.3901   | 0.8084  | 0.6348          | *Buen desempeño en la clase mayoritaria, pobre para la minoritaria.* |
| *Gradient Boosting*        | Test  | 0.8200   | 0.3045   | 0.8200  | 0.6006          | *Similar a Random Forest, útil para patrones generales pero limitado en clases desbalanceadas.* |


- *Balanced RF se identifica como el modelo más efectivo para este caso de estudio, equilibrando la detección de accidentes graves y leves.*  
- *Los modelos de ensemble (Balanced RF, Easy Ensemble) superan a modelos individuales en datasets desbalanceados.*  
- *Las métricas de ROC-AUC y Average Precision confirman la capacidad de discriminación de los modelos en la clase minoritaria.*  
- *Se recomienda considerar técnicas de oversampling como SMOTE si se desea reducir el sobreajuste y mejorar recall de la clase minoritaria.*  
- *Logistic Regression balanceada es simple y efectiva pero menos flexible para patrones complejos de accidentes.*  
- *Random Forest y Gradient Boosting funcionan bien para la clase mayoritaria, pero requieren ajustes o técnicas adicionales para la minoritaria.*


---

##  🚀 *Despliegue con FastAPI*

- *El modelo se expone a través de un endpoint REST `/predict`.*
- *Se reciben inputs de las variables seleccionadas y se devuelve:*
  - *Predicción: 0 = leve, 1 = grave*
  - *Probabilidad de accidente grave*


---
## ⚠️ *Disclaimer*

- *Los datos utilizados en este proyecto provienen de la plataforma [Kaggle](https://www.kaggle.com/) y se emplearon únicamente con fines investigativos.*  
- *El modelo desarrollado está basado en los datos disponibles y su desempeño refleja únicamente las características de ese dataset.*  
- *No se recomienda utilizar este modelo en entornos reales de seguridad vial sin una validación adicional exhaustiva y sin considerar la normativa y protocolos locales.*  
- *El modelo puede contener errores o generar predicciones incorrectas, especialmente en situaciones no representadas en los datos de entrenamiento, y no garantizan precisión en escenarios del mundo real.*
- *Cualquier uso del modelo debe hacerse bajo responsabilidad del usuario y con precauciones adecuadas.*  


