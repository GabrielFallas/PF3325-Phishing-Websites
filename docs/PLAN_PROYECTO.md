# Plan del Proyecto – PF3325

## Detección de Phishing Websites mediante Redes Neuronales

> **Curso:** PF3325 – Redes  
> **Dataset:** [UCI ML Repository – Phishing Websites (ID: 327)](https://archive.ics.uci.edu/dataset/327/phishing+websites)  
> **Archivo de datos:** `Training Dataset.arff`  
> **Fecha del documento:** Marzo 2026

---

## Índice

1. [Descripción General del Proyecto](#1-descripción-general-del-proyecto)
2. [Dataset y Configuración del Entorno](#2-dataset-y-configuración-del-entorno)
3. [Entrega 1 – ¿Qué queremos hacer y de dónde vienen los datos?](#3-entrega-1--qué-queremos-hacer-y-de-dónde-vienen-los-datos-8-de-abril)
4. [Entrega 2 – Demostración en Clase](#4-entrega-2--demostración-en-clase-29-de-abril)
5. [Entregas 3 y 4 – Contexto y Marco Teórico](#5-entregas-3-y-4--contexto-y-marco-teórico)
6. [Entregas 5 y 6 – Detección en Tiempo Real y Entrega Final](#6-entregas-5-y-6--detección-en-tiempo-real-y-entrega-final)
7. [Resumen de Fechas](#7-resumen-de-fechas)
8. [Estructura del Repositorio](#8-estructura-del-repositorio)

---

## 1. Descripción General del Proyecto

### Tema

Detección automática de sitios web de phishing mediante el uso de **Redes Neuronales Artificiales (ANN)**, aplicando técnicas de aprendizaje supervisado sobre el conjunto de datos UCI Phishing Websites.

### Objetivo Principal

Construir un pipeline completo de detección de phishing que:

1. Procese y prepare el dataset de características de URLs.
2. Entrene una red neuronal capaz de clasificar URLs como legítimas o de phishing.
3. Extienda el sistema hacia una **detección en tiempo real** (clasificación sincrónica).

### Contexto del Problema

El phishing es uno de los ataques de ingeniería social más prevalentes. Los atacantes crean sitios web fraudulentos que imitan páginas legítimas para robar credenciales y datos sensibles. Existen dos enfoques clásicos de detección: (1) **basados en listas negras**, que no escalan ante sitios nuevos creados en segundos, y (2) **basados en heurísticas**, que analizan características de la URL y el contenido de la página para identificar patrones de phishing sin requerir listas previas.

El dataset UCI Phishing Websites fue construido por Mohammad et al. (2012, 2014) mediante herramientas de extracción automática (scripts JavaScript y PHP) que analizaron páginas de PhishTank y definieron reglas precisas para 30 características. **Nuestro proyecto no rehace esa extracción de características.** En cambio, tomamos el dataset ya construido como punto de partida y aportamos lo siguiente: (1) aplicar **redes neuronales profundas (MLP)** para clasificación — algo que los autores originales no implementaron en el trabajo fundacional —, (2) un análisis comparativo riguroso de arquitecturas, y (3) un **componente de detección en tiempo real** (API REST + extractor simplificado) que ninguno de los trabajos fundacionales contempló.

---

## 2. Dataset y Configuración del Entorno

### Descripción del Dataset

- **Fuente:** UCI Machine Learning Repository – Phishing Websites (ID: 327)
- **Archivo local:** `Training Dataset.arff`
- **Instancias:** 11,055 muestras (ampliado desde los 2,500 del estudio piloto de 2012)
- **Features:** 30 atributos extraídos automáticamente con herramientas JavaScript y PHP
- **Target:** `Result` → `-1` (phishing) / `1` (legítimo)

### Codificación de Features

Las features **NO** son puramente binarias. El paper original define un sistema **ternario**:

| Valor | Significado |
| ----- | ----------- |
| `1`   | Legítimo    |
| `0`   | Sospechoso  |
| `-1`  | Phishing    |

Algunos features solo toman valores `{-1, 1}` (ej. `having_IP_Address`), mientras que otros usan los tres valores `{-1, 0, 1}` (ej. `URL_Length`, `having_Sub_Domain`, `SSLfinal_State`). Esta escala ordinal debe tenerse en cuenta durante el preprocesamiento.

### Características del Dataset (30 features)

Las características siguen exactamente las 4 categorías definidas por Mohammad et al. (2012). La asignación correcta es:

| Categoría                     | Features del Dataset UCI                                                                                                                                                                                                         |
| ----------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Address Bar based**         | `having_IP_Address`, `URL_Length`, `Shortining_Service`, `having_At_Symbol`, `double_slash_redirecting`, `Prefix_Suffix`, `having_Sub_Domain`, `SSLfinal_State`, `Domain_registeration_length`, `Favicon`, `port`, `HTTPS_token` |
| **Abnormal based**            | `Request_URL`, `URL_of_Anchor`, `Links_in_tags`, `SFH`, `Submitting_to_email`, `Abnormal_URL`                                                                                                                                    |
| **HTML and JavaScript based** | `Redirect`, `on_mouseover`, `RightClick`, `popUpWidnow`, `Iframe`                                                                                                                                                                |
| **Domain based**              | `age_of_domain`, `DNSRecord`, `web_traffic`, `Page_Rank`, `Google_Index`, `Links_pointing_to_page`, `Statistical_report`                                                                                                         |

> **Nota importante:** El paper de 2012 describió inicialmente 17 features. El dataset completo de 30 features publicado en UCI corresponde al trabajo expandido (Mohammad et al., 2014). Debemos citar ambas publicaciones en nuestro trabajo relacionado.

### Configuración del Entorno

```bash
pip install ucimlrepo pandas numpy scikit-learn tensorflow keras matplotlib seaborn scipy
```

### Importación del Dataset

```python
from ucimlrepo import fetch_ucirepo

# Cargar el dataset desde UCI
phishing_websites = fetch_ucirepo(id=327)

# Datos como DataFrames de pandas
X = phishing_websites.data.features
y = phishing_websites.data.targets

# Metadata y variables
print(phishing_websites.metadata)
print(phishing_websites.variables)
```

---

## 3. Entrega 1 – ¿Qué queremos hacer y de dónde vienen los datos? (8 de abril)

### Formato

- **Reunión de 15 minutos con el profesor** (mientras el resto de la clase trabaja de forma asincrónica)
- **Fecha:** Miércoles 8 de abril

### Objetivo

Demostrar que se tiene una propuesta madura y estudiada: descripción de la entrada de datos, opciones para el clasificador y la salida esperada.

---

### 3.1 Descripción de la Entrada de Datos

**¿De dónde vienen los datos?**

- Dataset público del UCI Machine Learning Repository: _Phishing Websites_ (ID 327).
- Disponible también como archivo local `Training Dataset.arff`.
- Cada instancia representa una URL analizada, con 30 features binarias/ternarias extraídas de forma automática.

**Preprocesamiento a describir:**

- Los valores de las features son categóricos: `{-1, 0, 1}` o `{-1, 1}`.
- No hay valores faltantes (dataset limpio).
- Se aplicará **normalización/estandarización** para la red neuronal.
- Se realizará análisis exploratorio (distribución de clases, correlación entre features).
- División del dataset: **70% entrenamiento, 15% validación, 15% prueba** (estratificada para mantener la proporción de clases).

---

### 3.2 Opciones Valoradas para el Clasificador

Se evaluarán las siguientes arquitecturas de red neuronal:

| Opción                         | Descripción                                      | Justificación                                       |
| ------------------------------ | ------------------------------------------------ | --------------------------------------------------- |
| **MLP básico**                 | Red densa con 2-3 capas ocultas (ReLU + Dropout) | Línea base, simplicidad                             |
| **MLP profundo**               | Red con 4-5 capas, Batch Normalization           | Mayor capacidad representacional                    |
| **Comparativa con ML clásico** | Random Forest, SVM                               | Para contextualizar el desempeño de la red neuronal |

**Hiperparámetros a explorar:**

- Número de capas ocultas: {2, 3, 4}
- Neuronas por capa: {64, 128, 256}
- Función de activación: ReLU, Leaky ReLU
- Optimizador: Adam, SGD con momentum
- Tasa de aprendizaje: {0.001, 0.0001}
- Dropout: {0.2, 0.3, 0.5}
- Épocas: hasta convergencia con Early Stopping

---

### 3.3 Salidas del Clasificador

- **Salida primaria:** Clasificación binaria → `Phishing` (-1) o `Legítimo` (1)
- **Salida secundaria:** Probabilidad de que una URL sea phishing (`sigmoid` output)
- **Umbral ajustable:** Para balancear precisión vs. recall según el caso de uso

**Métricas de evaluación:**

- Exactitud (Accuracy)
- Precisión, Recall, F1-Score
- Curva ROC y AUC
- Matriz de confusión

---

### 3.4 Material para la Reunión

**Puntos a cubrir en los 15 minutos:**

1. Presentación del problema (phishing, impacto, motivación) — _3 min_
2. Descripción del dataset: origen, tamaño, features, distribución de clases — _4 min_
3. Propuesta de arquitectura de la red neuronal — _4 min_
4. Salidas esperadas y métricas de evaluación — _2 min_
5. Preguntas del profesor — _2 min_

**Artefactos a preparar:**

- Notebook de análisis exploratorio del dataset (EDA).
- Diagrama de la arquitectura de red neuronal propuesta.
- Tabla comparativa de features del dataset.

---

## 4. Entrega 2 – Demostración en Clase (29 de abril)

### Formato

- **Video de 8 a 12 minutos** de duración
- **Fecha:** Miércoles 29 de abril

### Objetivo

Demostrar qué partes de la implementación **ya están funcionando**: datos cargados, preprocesamiento, modelo entrenado con resultados preliminares.

---

### 4.1 Contenido del Video

**Sección 1 – ¿Cuáles son sus datos? (2-3 min)**

- Carga del dataset con `ucimlrepo` y desde el archivo `.arff`.
- Visualización del EDA: distribución de clases, heatmap de correlación, boxplots.
- Demostración del preprocesamiento: normalización, split train/val/test.

**Sección 2 – Diseño y funcionalidad del clasificador (4-5 min)**

- Arquitectura de la red neuronal (código + diagrama).
- Proceso de entrenamiento: curvas de loss y accuracy por época.
- Técnicas implementadas: Dropout, Early Stopping, BatchNormalization.
- Comparación preliminar con un baseline (ej. Logistic Regression o Random Forest).

**Sección 3 – Posibles salidas del clasificador (2-3 min)**

- Demo de predicción en vivo: dado un vector de features, la red devuelve la clasificación.
- Métricas obtenidas hasta el momento: matriz de confusión, F1-Score, AUC-ROC.
- Discusión de resultados preliminares y próximos pasos.

---

### 4.2 Tareas de Implementación para Esta Entrega

```
[ ] EDA completo con visualizaciones (matplotlib/seaborn)
[ ] Pipeline de preprocesamiento (StandardScaler, LabelEncoder si aplica)
[ ] Implementación de la red neuronal con Keras/TensorFlow
[ ] Entrenamiento con Early Stopping y guardado del mejor modelo
[ ] Evaluación sobre conjunto de validación
[ ] Script de inferencia: dada una URL procesada, devuelve predicción
[ ] Grabación del video de demostración
```

---

### 4.3 Código Base (Estructura del Clasificador)

```python
import tensorflow as tf
from tensorflow import keras
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report, roc_auc_score

# --- Preprocesamiento ---
X_train, X_temp, y_train, y_temp = train_test_split(X, y, test_size=0.30, random_state=42, stratify=y)
X_val, X_test, y_val, y_test = train_test_split(X_temp, y_temp, test_size=0.50, random_state=42, stratify=y_temp)

scaler = StandardScaler()
X_train_sc = scaler.fit_transform(X_train)
X_val_sc   = scaler.transform(X_val)
X_test_sc  = scaler.transform(X_test)

# Convertir etiquetas de {-1, 1} a {0, 1}
y_train_bin = (y_train == 1).astype(int)
y_val_bin   = (y_val == 1).astype(int)
y_test_bin  = (y_test == 1).astype(int)

# --- Arquitectura de la Red Neuronal ---
model = keras.Sequential([
    keras.layers.Input(shape=(30,)),
    keras.layers.Dense(128, activation='relu'),
    keras.layers.BatchNormalization(),
    keras.layers.Dropout(0.3),
    keras.layers.Dense(64, activation='relu'),
    keras.layers.BatchNormalization(),
    keras.layers.Dropout(0.2),
    keras.layers.Dense(32, activation='relu'),
    keras.layers.Dense(1, activation='sigmoid')
])

model.compile(optimizer='adam',
              loss='binary_crossentropy',
              metrics=['accuracy'])

# --- Entrenamiento ---
callbacks = [
    keras.callbacks.EarlyStopping(patience=10, restore_best_weights=True),
    keras.callbacks.ModelCheckpoint('best_model.keras', save_best_only=True)
]

history = model.fit(
    X_train_sc, y_train_bin,
    validation_data=(X_val_sc, y_val_bin),
    epochs=100,
    batch_size=64,
    callbacks=callbacks
)

# --- Evaluación ---
y_pred = (model.predict(X_test_sc) > 0.5).astype(int)
print(classification_report(y_test_bin, y_pred, target_names=['Phishing', 'Legítimo']))
print("AUC-ROC:", roc_auc_score(y_test_bin, model.predict(X_test_sc)))
```

---

## 5. Entregas 3 y 4 – Contexto y Marco Teórico

### Puntos requeridos por el profesor

- **a.** Motivación y descripción clara del problema a resolver.
- **b.** Soluciones existentes en el trabajo relacionado y comparación con la propuesta.
- **c.** Marco teórico necesario para entender el proyecto.

---

## 5.1 Entrega 3 – Presentación en Clase (20 de mayo)

### Formato

- **Presentación oral en clase**
- **Fecha:** Miércoles 27 de mayo

### Estructura de la Presentación

**Diapositiva 1: Portada**

- Título del proyecto, nombres del equipo, fecha.

**Diapositivas 2-4: (a) Motivación y Problema**

- Estadísticas de phishing: prevalencia, impacto económico (APWG, FBI IC3 reports).
- ¿Por qué las listas negras son insuficientes? Limitaciones de los métodos tradicionales.
- Pregunta de investigación: ¿Puede una red neuronal detectar phishing de manera efectiva basándose solo en características de la URL y página?
- Definición formal del problema: clasificación binaria supervisada.

**Diapositivas 5-8: (b) Trabajo Relacionado**

| Paper / Trabajo                        | Técnica                                                     | Dataset                | Resultado clave                                                      | Año  |
| -------------------------------------- | ----------------------------------------------------------- | ---------------------- | -------------------------------------------------------------------- | ---- |
| Mohammad et al. (**este dataset**)     | Extracción automática de features + análisis de frecuencias | 2,500 URLs (PhishTank) | Definición de 17 reglas de extracción; no entrena clasificador final | 2012 |
| Mohammad et al. (dataset completo UCI) | Neural Network auto-estructurada (SSNN), J48, RF            | 11,055 URLs (UCI)      | Accuracy ~97% con SSNN                                               | 2014 |
| Basnet et al.                          | ANN (backpropagation)                                       | URLs                   | ~93% accuracy                                                        | 2008 |
| Sahingoz et al.                        | Random Forest, NLP features                                 | 73,575 URLs            | 97.32%                                                               | 2019 |
| Vrbančič et al.                        | Ensemble, XGBoost                                           | Múltiples datasets     | ~97.6%                                                               | 2020 |
| Chatterjee & Namin                     | Deep Learning (CNN) raw URLs                                | URLs                   | ~96%                                                                 | 2019 |

> **Posicionamiento crítico:** Mohammad et al. (2012) **no entrenó un clasificador de producción** — su paper es sobre ingeniería de features (definir las reglas de extracción y medir la frecuencia de cada feature). El trabajo de clasificación con ML clásico vino después (2014). Nuestra propuesta se diferencia al aplicar arquitecturas de **deep learning comparadas sistemáticamente**, a las cuales se agrega el componente de **detección en tiempo real** como contribución original al pipeline.

- **Gap que abordamos:** ninguno de los trabajos fundacionales construyó un sistema end-to-end de detección en tiempo real servido como API. Los clasificadores existentes son experimentos offline.

**Diapositivas 9-12: (c) Marco Teórico**

- **Phishing:** definición, tipos (URL-based, content-based, DNS-based).
- **Aprendizaje Supervisado:** clasificación binaria, función de pérdida binaria.
- **Redes Neuronales:** perceptrón multicapa (MLP), función de activación, backpropagation, gradient descent.
- **Regularización:** Dropout, Batch Normalization, Early Stopping.
- **Métricas:** Accuracy, Precision, Recall, F1, AUC-ROC, matriz de confusión.

**Diapositiva 13: Resultados Preliminares**

- Mostrar métricas del modelo entrenado (Entrega 2).

**Diapositiva 14: Conclusiones y Trabajo Futuro**

- Resumen de lo logrado y lo que viene (tiempo real).

---

## 5.2 Entrega 4 – Documento Escrito (3 de junio)

### Formato

- **≈3 páginas, formato IEEE doble columna**
- **Fecha:** Miércoles 10 de junio

### Estructura del Documento (IEEE format)

```
Título: Detection of Phishing Websites Using Artificial Neural Networks
Autores: [Nombre(s)]
Abstract (≈150 palabras)
```

**I. Introduction** (~0.5 página)

- Contexto del problema de phishing.
- Motivación para usar ML/redes neuronales.
- Contribución del trabajo.
- Estructura del artículo.

**II. Related Work** (~0.75 página)

- Tabla comparativa de trabajos existentes (ver tabla en sección 5.1).
- **Punto crítico a destacar:** el paper fundacional (Mohammad 2012) es sobre _feature engineering_, no sobre clasificación. El clasificador con ML clásico viene en el paper de 2014. Nuestra diferenciación es el uso de deep learning + sistema en tiempo real.
- Análisis de limitaciones de trabajos previos: experimentos offline, sin API de servicio, sin análisis ablativo de hiperparámetros.

**III. Theoretical Framework** (~0.75 página)

- **Phishing Websites:** definición, tipos (URL-based, content-based, DNS-based), impacto.
- **El dataset UCI y su construcción:** las 4 categorías de features de Mohammad et al. (2012, 2014), reglas de extracción automática, codificación ternaria `{-1, 0, 1}`.
- **Multilayer Perceptron (MLP):** arquitectura, funciones de activación (ReLU, sigmoid), backpropagation, gradient descent.
- **Regularización:** Dropout, Batch Normalization, Early Stopping.

**IV. Proposed Approach** (~0.5 página)

- Descripción del pipeline: carga del dataset → preprocesamiento → entrenamiento → evaluación.
- Aclaración explícita: no reconstruimos el extractor de features de Mohammad et al.; usamos el dataset pre-extraído como dado.
- Diagrama de flujo del sistema.

**References** (IEEE style)

---

### Referencias Clave a Citar

1. Mohammad, R. M., Thabtah, F., & McCluskey, L. (2012). _An assessment of features related to phishing websites using an automated technique_. ICITST-2012. **(paper sobre feature engineering — citar para explicar el origen del dataset)**
2. Mohammad, R. M., Thabtah, F., & McCluskey, L. (2014). _Predicting phishing websites based on self-structuring neural network_. Neural Computing and Applications. **(paper con clasificador; citar para baseline y resultado de referencia)**
3. Sahingoz, O. K., et al. (2019). _Machine learning based phishing detection from URLs_. Expert Systems with Applications.
4. Vrbančič, G., Fister, I., & Podgorelec, V. (2020). _Datasets for phishing websites detection_. Data in Brief.
5. LeCun, Y., Bengio, Y., & Hinton, G. (2015). _Deep learning_. Nature.
6. UCI ML Repository: Phishing Websites Dataset. <https://archive.ics.uci.edu/dataset/327/phishing+websites>

---

## 6. Entregas 5 y 6 – Detección en Tiempo Real y Entrega Final

### Componente de Detección en Tiempo Real

El proyecto debe incorporar un componente **sincrónico**: clasificar tráfico/URLs en tiempo real, no solo sobre un dataset estático.

---

## 6.1 Entrega 5 – Presentación Final (1 de julio)

### Formato

- **Presentación de 10-12 minutos**
- **Fecha:** Miércoles 1 de julio

### Estructura de la Presentación

**a. Motivación / Problema / Trabajo Relacionado (breve) — ~2 min**

- Resumen ejecutivo de los puntos de las entregas 3/4.

**b. Implementación — ~6 min**

_Parte asincrónica (clasificación offline):_

- Pipeline completo: carga de datos → preprocesamiento → entrenamiento → evaluación.
- Arquitectura definitiva de la red neuronal.
- Comparación de experimentos (ablation study: con/sin Dropout, diferentes profundidades, etc.).
- Métricas finales en el conjunto de prueba.

_Parte sincrónica (tiempo real):_

- Descripción del componente en tiempo real implementado. Opciones:
  - **Opción A – Extensión de navegador / Proxy HTTP:** Intercepta peticiones del navegador, extrae features de la URL en tiempo real y llama al modelo para bloquear o permitir el acceso.
  - **Opción B – Sistema de monitoreo de red:** Captura tráfico con `Scapy` o `mitmproxy`, extrae features de las URLs que aparecen y las clasifica.
  - **Opción C – API REST con FastAPI/Flask:** Servicio que recibe una URL como input, extrae sus features y devuelve la clasificación en tiempo real.

**Demo en vivo recomendada:** API REST que recibe una URL, extrae características automáticamente y retorna `{url, features, prediction, confidence}`.

**c. Resultados y Análisis — ~3 min**

- Tabla de resultados comparativa (MLP vs. baseline).
- Curva ROC + AUC.
- Análisis de errores: ¿qué tipos de URLs engañan al modelo?
- Latencia del sistema en tiempo real.

---

### 6.1.1 Plan de Implementación del Componente en Tiempo Real

**Tecnología propuesta: API REST con FastAPI**

```python
# api_phishing.py
from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
import joblib
import tensorflow as tf

app = FastAPI(title="Phishing Detection API")
model = tf.keras.models.load_model("best_model.keras")
scaler = joblib.load("scaler.joblib")

class URLFeatures(BaseModel):
    features: list[float]  # 30 features del dataset

class URLInput(BaseModel):
    url: str  # URL cruda (requiere extractor de features)

@app.post("/predict/features")
def predict_from_features(data: URLFeatures):
    X = np.array(data.features).reshape(1, -1)
    X_sc = scaler.transform(X)
    prob = float(model.predict(X_sc)[0][0])
    label = "Legítimo" if prob > 0.5 else "Phishing"
    return {"prediction": label, "confidence": prob}

# Ejecutar: uvicorn api_phishing:app --reload
```

**Extractor de Features en Tiempo Real:**

- Dado que el dataset UCI ya tiene las features pre-extraídas, se deben implementar los 30 extractores de características para analizar URLs nuevas.
- Se puede usar `tldextract`, `requests`, `bs4 (BeautifulSoup)` para extraer features de URLs reales.

```bash
pip install fastapi uvicorn tldextract requests beautifulsoup4 joblib
```

---

## 6.2 Entrega 6 – Documento Final (5 de julio)

### Formato

- **Artículo científico, formato IEEE doble columna, 6 páginas incluyendo referencias**
- **Fecha:** Domingo 5 de julio

### Estructura del Artículo Final

```
Título: Real-Time Phishing Website Detection Using Artificial Neural Networks
Autores: [Nombre(s)]
Abstract (≈150-200 palabras) — Problema, método, resultados clave
Keywords: phishing detection, neural networks, machine learning, cybersecurity
```

**I. Introduction** (~0.5 página)

- Contexto ampliado del phishing.
- Motivación y pregunta de investigación.
- Contribuciones del trabajo:
  1. Pipeline de clasificación con MLP sobre UCI Phishing Dataset.
  2. Análisis comparativo de arquitecturas.
  3. Sistema prototipo de detección en tiempo real.
- Estructura del artículo.

**II. Related Work** (~0.75 página)

- Tabla actualizada del trabajo relacionado (incluir la distinción entre Mohammad 2012 —feature engineering— y Mohammad 2014 —clasificación—).
- Discusión crítica: limitaciones de clasificadores offline, falta de sistemas en tiempo real servibles.
- Posicionamiento de la propuesta: deep learning + sistema en tiempo real como gap no cubierto.

**III. Theoretical Background** (~0.5 página)

- Phishing websites: definición, técnicas comunes (URL spoofing, typosquatting, homograph attacks).
- Construcción del dataset UCI: las 4 categorías de features, reglas de extracción automática, codificación ternaria.
- Redes neuronales artificiales (MLP): arquitectura, training, regularización.

**IV. System Design and Implementation** (~1.5 páginas)

- Diagrama general del sistema (offline + tiempo real).
- _A. Dataset y Preprocesamiento:_ UCI dataset, normalización, split.
- _B. Red Neuronal:_ Arquitectura final, hiperparámetros, entrenamiento.
- _C. Componente en Tiempo Real:_ Descripción de la API/proxy, extracción de features online, integración con el modelo.

**V. Results and Analysis** (~1.5 páginas)

- _A. Resultados Clasificación Offline:_ tabla de métricas (Acc, Prec, Recall, F1, AUC), curva ROC, matriz de confusión.
- _B. Comparación de Arquitecturas:_ tabla de experimentos (MLP-2L vs MLP-3L vs Baseline RF/SVM).
- _C. Análisis del Sistema en Tiempo Real:_ latencia de inferencia, throughput, análisis de casos de error.
- Discusión de resultados.

**VI. Conclusions and Future Work** (~0.5 página)

- Resumen de logros y hallazgos.
- Limitaciones del sistema.
- Trabajo futuro: feature extraction automática desde URLs crudas, detección adversarial, zero-shot phishing.

**References** (IEEE, ≥8 referencias)

---

## 7. Resumen de Fechas

| Entrega | Descripción                                                                       | Fecha                 | Formato                |    Estado    |
| :-----: | --------------------------------------------------------------------------------- | --------------------- | ---------------------- | :----------: |
|  **1**  | Reunión con profesor: descripción de datos, diseño del clasificador y salidas     | Miércoles 8 de abril  | Reunión 15 min         | ⬜ Pendiente |
|  **2**  | Video de demostración: datos, implementación funcionando, resultados preliminares | Miércoles 29 de abril | Video 8-12 min         | ⬜ Pendiente |
|  **3**  | Presentación en clase: motivación, trabajo relacionado, marco teórico             | Miércoles 20 de mayo  | Presentación oral      | ⬜ Pendiente |
|  **4**  | Documento escrito: motivación, trabajo relacionado, marco teórico                 | Miércoles 3 de junio  | ~3 págs IEEE           | ⬜ Pendiente |
|  **5**  | Presentación final: implementación completa + tiempo real + resultados            | Miércoles 1 de julio  | Presentación 10-12 min | ⬜ Pendiente |
|  **6**  | Documento final: artículo completo con todo el trabajo                            | Domingo 5 de julio    | 6 págs IEEE            | ⬜ Pendiente |

---

## 8. Estructura del Repositorio

```
phishing-detection-pf3325/
│
├── data/
│   ├── Training Dataset.arff          # Dataset original
│   └── processed/                     # Datos preprocesados
│
├── notebooks/
│   ├── 01_eda.ipynb                   # Análisis exploratorio (Entrega 1/2)
│   ├── 02_preprocessing.ipynb         # Preprocesamiento del dataset
│   ├── 03_model_training.ipynb        # Entrenamiento de la red neuronal (Entrega 2)
│   ├── 04_experiments.ipynb           # Comparación de arquitecturas (Entrega 5)
│   └── 05_evaluation.ipynb            # Evaluación final y métricas
│
├── src/
│   ├── preprocess.py                  # Pipeline de preprocesamiento
│   ├── model.py                       # Definición de la arquitectura
│   ├── train.py                       # Script de entrenamiento
│   ├── evaluate.py                    # Métricas y visualizaciones
│   ├── feature_extractor.py           # Extractor de features de URLs reales
│   └── api_phishing.py                # API REST (FastAPI) para tiempo real
│
├── models/
│   ├── best_model.keras               # Mejor modelo entrenado
│   └── scaler.joblib                  # Scaler guardado
│
├── reports/
│   ├── entrega4_contexto.pdf          # Documento IEEE 3 páginas
│   └── entrega6_final.pdf             # Artículo IEEE 6 páginas
│
├── presentations/
│   ├── entrega3_presentacion.pptx
│   ├── entrega5_presentacion.pptx
│   └── entrega2_video_script.md
│
├── requirements.txt
├── README.md
└── PLAN_PROYECTO.md                   # Este documento
```

### `requirements.txt`

```
ucimlrepo
pandas
numpy
scikit-learn
tensorflow>=2.12
keras
matplotlib
seaborn
scipy
fastapi
uvicorn
tldextract
requests
beautifulsoup4
joblib
```

---

## Apéndice – Notas Técnicas Importantes

### Diferenciación con el Trabajo Original (Mohammad et al.)

| Aspecto               | Mohammad et al. 2012                      | Mohammad et al. 2014                | **Nuestro proyecto**                                  |
| --------------------- | ----------------------------------------- | ----------------------------------- | ----------------------------------------------------- |
| Objetivo              | Definir reglas de extracción de features  | Clasificación con ML clásico y SSNN | Clasificación con **deep learning (MLP comparativo)** |
| Dataset               | 2,500 URLs (PhishTank)                    | 11,055 URLs (UCI dataset publicado) | **Mismo UCI dataset** (no generamos datos nuevos)     |
| Feature extraction    | Construyeron el extractor (JS + PHP)      | Usaron el dataset ya construido     | **No reconstruimos el extractor**                     |
| Clasificador          | Análisis de frecuencias (no clasificador) | J48, Random Forest, SSNN (~97%)     | MLP con estudio ablativo de hiperparámetros           |
| Tiempo real           | No                                        | No                                  | **Sí — API REST funcional**                           |
| Entorno de deployment | N/A                                       | N/A                                 | **FastAPI + servicio HTTP**                           |

### Manejo de Etiquetas

El dataset UCI Phishing usa las etiquetas `{-1, 1}` para el target `Result`:

- `-1` → Phishing
- `1` → Legítimo

Las **features** individuales usan codificación ternaria `{-1, 0, 1}`:

- `1` → Indica patrón legítimo
- `0` → Indica patrón sospechoso
- `-1` → Indica patrón de phishing

Para la capa de salida con `sigmoid`, convertir el **target** a `{0, 1}`:

```python
y_binary = (y == 1).astype(int)  # 1=Legítimo, 0=Phishing
```

> **Las features NO se deben convertir a binario.** El valor `0` (suspicious) es información válida diferente a `-1` y `1`. Aplicar `StandardScaler` directamente sobre los valores `{-1, 0, 1}` es el enfoque correcto.

### Carga del Archivo .arff

```python
from scipy.io import arff
import pandas as pd

data, meta = arff.loadarff('Training Dataset.arff')
df = pd.DataFrame(data)
# Decodificar columnas de tipo bytes
df = df.applymap(lambda x: x.decode() if isinstance(x, bytes) else x)
```

### Carga Alternativa con ucimlrepo

```python
from ucimlrepo import fetch_ucirepo
phishing_websites = fetch_ucirepo(id=327)
X = phishing_websites.data.features  # DataFrame con 30 features
y = phishing_websites.data.targets   # DataFrame con columna 'Result'
```

---

_Documento generado como guía de planificación del proyecto PF3325 – Detección de Phishing Websites con Redes Neuronales._

