# 🎥 Entrega 2 - Script de Presentación (Demostración de Video)

**Duración:** 8-12 minutos  
**Formato:** Demostración en video (grabación de pantalla + narración)  
**Equipo:** Gabriel Fallas & Valeria Chinchilla

---

## 📋 ESTRUCTURA DEL GUIÓN

**Total: ~12 minutos**

- Introducción: 1 min
- Datos: 2-3 min
- Diseño del Clasificador: 3-4 min
- Predicciones: 2-3 min
- Resultados: 2-3 min
- Conclusión: 1 min

---

## 🎬 GUIÓN DETALLADO POR PERSONA

### **PERSONA 1**

**[MIN 0:00-0:30] INTRODUCCIÓN**

_"Hola, somos Gabriel Fallas y Valeria Chinchilla. En esta demostración vamos a mostrarles el sistema de detección de phishing que hemos desarrollado para el curso de Redes._

_El phishing es uno de los ataques más comunes en internet. Los delincuentes crean sitios web falsos para robar contraseñas y datos sensibles. Nuestro objetivo es crear un clasificador automático que identifique si una URL pertenece a un sitio de phishing o si es legítimo._

_Vamos a mostrarles tres cosas:_

1. _Los datos que usamos_
2. _El diseño de nuestro clasificador_
3. _Los resultados que obtuvimos"_

---

**[MIN 0:30-2:30] DATASET OVERVIEW** _(Mostrar output del demo.py - sección DATASET)_

_"Estamos usando el dataset UCI Phishing Websites, que es uno de los más reconocidos en este área._

_Algunos datos importantes:_

- _Tenemos 11,055 muestras de sitios web_
- _Cada sitio web está descrito con 30 características o features_
- _44.3% son sitios de phishing, 55.7% son legítimos_
- _El dataset está muy balanceado, lo que es perfecto para entrenar"_

**[MOSTRAR EN PANTALLA: Output de "Dataset Statistics"]**

_"Las 30 características están organizadas en 4 categorías:_

1. _Address Bar based: Características de la URL y el dominio (12 features)_
2. _Abnormal based: Indicadores de comportamiento anormal (6 features)_
3. _HTML & JavaScript based: Análisis del código del lado del cliente (5 features)_
4. _Domain based: Métricas de reputación del dominio (7 features)"_

**[MOSTRAR EN PANTALLA: Primera muestra de datos + Feature Values]**

_"Veamos un ejemplo. Aquí está una muestra de los datos. Cada feature tiene 3 posibles valores:_

- _-1: Indicador de phishing_
- _0: Sospechoso_
- _1: Indicador legítimo_

_Por ejemplo, si una URL tiene una dirección IP en lugar de un nombre de dominio (having_IP_Address = -1), es un indicador fuerte de phishing."_

---

**[MIN 2:30-4:00] PREPROCESAMIENTO**

_"Antes de entrenar los modelos, preparamos los datos con el siguiente pipeline:_

1. _Cargamos el archivo ARFF (formato de datos)_
2. _Codificamos el target de {-1, 1} a {0, 1}_
3. _Estandarizamos todas las features para tener media 0 y desviación estándar 1_
4. _Dividimos los datos en:_
   - _70% para entrenamiento (7,737 muestras)_
   - _15% para validación (1,659 muestras)_
   - _15% para pruebas (1,659 muestras)"_

---

**[MIN 4:00-5:30] DISEÑO DEL CLASIFICADOR**

_"Implementamos dos clasificadores diferentes:_

**Primer Clasificador: Random Forest**

- _Usamos un ensamble de 100 árboles de decisión_
- _El enfoque de bagging lo hace muy robusto_
- _Maneja bien la no-linealidad y las interacciones entre features_
- _Es rápido en predicciones_

\*_Segundo Clasificador: Support Vector Machine (SVM)_

- _Usamos kernel RBF (Radial Basis Function)_
- _Encuentra el hiperplano óptimo que separa las dos clases_
- _Excelente para espacios de alta dimensionalidad (30 features)_
- _Muy efectivo para clasificación binaria"_

**[MOSTRAR EN PANTALLA: Sección "CLASSIFIER DESIGN" del demo.py]**

_"Las métricas que usamos para evaluar son:_

- _Accuracy: Exactitud general (¿cuántos predijo correctamente?)_
- _Precision: De los que predijo como phishing, ¿cuántos eran realmente phishing?_
- _Recall: De todos los sitios de phishing, ¿cuántos encontró nuestro modelo?_
- _F1-Score: Media armónica entre precision y recall_
- _AUC-ROC: Área bajo la curva ROC (0-1, donde 1 es perfecto)"_

---

### **PERSONA 2**

**[MIN 5:30-7:00] PREDICCIONES DE MUESTRA** _(Mostrar output - sección SAMPLE PREDICTIONS)_

_"Aquí pueden ver 10 predicciones de nuestro modelo en el conjunto de pruebas._

_Para cada sitio web, mostramos:_

- _La etiqueta verdadera (es realmente phishing o legítimo)_
- _La predicción del Random Forest_
- _La predicción del SVM_
- _Si ambos modelos acertaron (✓) o no (✗)"_

**[MOSTRAR EN PANTALLA: Tabla de predicciones]**

_"Como ven, en estos 10 ejemplos, ambos modelos acertaron en todos. Esto es muy buena señal. Algunos ejemplos:_

- _Un sitio legítimo fue clasificado como legítimo por ambos modelos ✓_
- _Un sitio de phishing fue detectado como phishing ✓_

_Esto demuestra que nuestros clasificadores están funcionando muy bien."_

---

**[MIN 7:00-9:30] EVALUACIÓN DEL MODELO** _(Mostrar output - sección MODEL EVALUATION)_

_"Veamos los resultados detallados en el conjunto de pruebas:_

**Random Forest - Resultados:**

- _Accuracy: 97.17% - Acertó en 1,612 de 1,659 muestras_
- _Precision: 96.90% - De los que predijo como phishing, 96.9% realmente lo eran_
- _Recall: 98.05% - Encontró el 98% de los sitios de phishing_
- _F1-Score: 97.47% - Excelente balance entre precision y recall_
- _AUC-ROC: 0.9959 - Casi perfecto"_

**[MOSTRAR EN PANTALLA: Matriz de confusión + números]**

_"La matriz de confusión nos muestra:_

- _706 Verdaderos Negativos (legítimos que identificó como legítimos)_
- _29 Falsos Positivos (legítimos que identificó como phishing) ← Queremos minimizar esto_
- _18 Falsos Negativos (phishing que identificó como legítimos) ← Crítico minimizar esto_
- _906 Verdaderos Positivos (phishing que identificó correctamente)_

_Con solo 18 falsos negativos de 924 sitios de phishing en el conjunto de pruebas, estamos capturando el 98% de los ataques."_

---

**[MIN 9:30-11:00] VISUALIZACIONES**

**[MOSTRAR EN PANTALLA: Confusion Matrix]**

_"Esta es la matriz de confusión del Random Forest. El color más oscuro indica más muestras. Pueden ver que la diagonal principal (predicciones correctas) es mucho más fuerte que el resto."_

**[MOSTRAR EN PANTALLA: ROC Curve]**

_"Esta es la curva ROC. El área bajo la curva (AUC) es 0.9959, lo que indica un clasificador excelente. Mientras más cerca esté la curva de la esquina superior izquierda, mejor es el modelo. La línea punteada diagonal representa un clasificador aleatorio (50% de accuracy)."_

_"Comparado con el SVM que obtuvo AUC de 0.9874, el Random Forest es ligeramente superior."_

---

**[MIN 11:00-12:00] CONCLUSIONES**

_"En resumen:_

1. **El dataset**: 11,055 sitios web con 30 características que describen aspectos de la URL y el dominio

2. **El clasificador**: Dos modelos robustos (Random Forest y SVM) con un pipeline de preprocesamiento bien diseñado

3. **Los resultados**: Random Forest con 97.17% de accuracy y 98.05% de recall es excelente para detectar phishing

4. **Lo siguiente**: En la próxima entrega vamos a implementar un componente de tiempo real (API REST) para poder clasificar URLs nuevas instantáneamente.

Este es un buen punto de partida para un sistema de detección de phishing automático. Gracias por ver nuestra demostración. ¿Alguna pregunta?"\*

---

## 📹 INSTRUCCIONES TÉCNICAS PARA GRABAR

### Preparación

1. **Abre una terminal** en la carpeta del proyecto:

   ```bash
   cd /Users/vchinchilla/Documents/UCR/Redes/PF3325-Phishing-Websites
   ```

2. **Activa el ambiente virtual:**

   ```bash
   source .venv/bin/activate
   ```

3. **Ejecuta el script de demostración:**
   ```bash
   python src/demo.py
   ```

### Grabación en macOS

**Opción 1: Usando QuickTime (Recomendado)**

1. Abre **QuickTime Player**
2. Ve a **File → New Screen Recording**
3. Selecciona el área de la terminal
4. Presiona **Grabar** para comenzar

**Opción 2: Usando OBS Studio** (Más control)

1. Descarga OBS Studio (gratis)
2. Configura una escena con tu pantalla + micrófono
3. Presiona **Start Recording**

### Narración

- **Dividan el guión** entre ustedes dos
- **Hablen claro y lentamente** - el video es educativo
- **Usen las pantallas del output** para apoyar lo que dicen
- **Muestren las gráficas generadas** (confusion_matrix.png, roc_curve.png)
- **No lean literalmente el guión** - adaptenlo de forma natural

### Duración y Timing

- Total: 8-12 minutos
- Si necesitan acortar: omitan detalles técnicos menores
- Si necesitan extender: profundicen en ejemplos específicos

### Archivos de Apoyo

Los siguientes archivos se generan automáticamente:

- `reports/confusion_matrix.png` - Mostrar en min 9:30
- `reports/roc_curve.png` - Mostrar en min 9:45
- Output del script - Usar durante toda la presentación

---

## ✅ CHECKLIST ANTES DE ENTREGAR

- [ ] Guión practicado y ttiempos verificados
- [ ] Ambiente virtual configurado y dependencias instaladas
- [ ] Script `src/demo.py` se ejecuta sin errores
- [ ] Gráficas generadas en `reports/`
- [ ] Video grabado con buena calidad de audio
- [ ] Video editado (opcional) - recortes, títulos
- [ ] Duración total entre 8-12 minutos
- [ ] Archivos de video listos para entregar (MP4 o similar)

---

## 🎯 PREGUNTAS QUE RESPONDE LA PRESENTACIÓN

✅ **¿Cuáles son sus datos?**

- 11,055 muestras de URLs
- 30 características de URL y dominio
- 44.3% phishing, 55.7% legítimos

✅ **¿Qué aspectos de diseño y funcionalidad del clasificador?**

- Random Forest (100 árboles) vs SVM (kernel RBF)
- Pipeline de preprocesamiento (estandarización, split 70/15/15)
- Evaluación con 5 métricas: Accuracy, Precision, Recall, F1, AUC-ROC

✅ **¿Cuáles son las posibles salidas del clasificador?**

- Clasificación binaria: **Phishing** o **Legítimo**
- Con probabilidad asociada
- Matriz de confusión: TP, TN, FP, FN

✅ **¿Qué cosas de la implementación funcionan?**

- Carga de datos desde ARFF: ✅
- Preprocesamiento y normalización: ✅
- Entrenamiento de ambos modelos: ✅
- Predicciones con 97%+ accuracy: ✅
- Visualización de resultados: ✅
