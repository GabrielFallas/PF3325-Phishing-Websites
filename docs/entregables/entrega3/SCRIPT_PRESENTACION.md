# 📋 Script de Presentación — Entrega 3

**Curso:** PF3325 – Redes Computacionales  
**Universidad:** Universidad de Costa Rica  
**Equipo:** Gabriel Fallas & Valeria Chinchilla  
**Fecha:** Miércoles 27 de mayo de 2026  
**Duración Total:** 25-27 minutos

---

## ⏱️ Timeline General

```
00:00 - 27:00  │  PRESENTACIÓN COMPLETA
```

---

## 📺 SLIDE 1: Portada

**⏱️ Tiempo:** 00:00 - 00:30 (30 segundos)  
**🎤 Presentador:** GABRIEL

### Script:

"Buenos días, profesores y compañeros. Somos Gabriel Fallas y Valeria Chinchilla, estudiantes del curso PF3325 – Redes Computacionales. Hoy les presentamos nuestro proyecto de investigación: _Detección de Phishing en Sitios Web usando Machine Learning_.

Este proyecto surgió de una pregunta fundamental: ¿Cómo podemos proteger a los usuarios de ataques de phishing utilizando técnicas avanzadas de inteligencia artificial? A lo largo de los próximos 25 minutos, les mostraremos nuestro problema, nuestro trabajo relacionado, nuestra propuesta, y nuestros resultados preliminares.

¡Comenzamos!"

---

## 📺 SLIDE 2: Agenda

**⏱️ Tiempo:** 00:30 - 01:00 (30 segundos)  
**🎤 Presentador:** GABRIEL

### Script:

"La presentación está dividida en 4 secciones principales:

**Primero**, hablaremos sobre el _problema del phishing_ — qué es, por qué es crítico, y por qué los métodos actuales fallan.

**Segundo**, revisaremos el _trabajo relacionado_ — qué han hecho otros investigadores antes que nosotros.

**Tercero**, explicaremos nuestro _marco teórico_ — el dataset que usamos, la arquitectura de redes neuronales, y las técnicas de regularización.

**Finalmente**, mostraremos nuestros _resultados preliminares_ y los próximos pasos.

Vamos con la sección 1."

---

## 📺 SLIDE 3: ¿Qué es el Phishing?

**⏱️ Tiempo:** 01:00 - 03:00 (2 minutos)  
**🎤 Presentador:** GABRIEL

### Script:

"El _phishing_ es un tipo de ataque cibernético donde un atacante intenta engañar a un usuario para que revele información sensible — como contraseñas, números de tarjeta de crédito, o datos personales.

Existen tres tipos principales de phishing:

**1. Phishing basado en URLs (URL-based phishing):**
El atacante crea una URL falsa que parece legítima (ej: 'amaz0n.com' en lugar de 'amazon.com'). Cuando el usuario hace clic, accede a una página falsa diseñada para robar credenciales.

**2. Phishing basado en contenido (Content-based phishing):**
El atacante manipula el HTML, CSS, o JavaScript de un sitio legítimo para ocultarlo o redirigirlo. Usa técnicas como iframes ocultos, estilos CSS maliciosos, o dominios similares.

**3. Phishing basado en DNS (DNS-based phishing):**
El atacante compromete registros DNS para redirigir usuarios a sitios falsos. Por ejemplo, redirigir 'bank.com' a '192.168.1.100'.

Nuestro proyecto se enfoca en **detectar estas amenazas automáticamente** usando Machine Learning — sin depender de listas negras manuales o heurísticas que fácilmente se pueden evadir."

---

## 📺 SLIDE 4: Impacto Real - Estadísticas 2024-2025

**⏱️ Tiempo:** 03:00 - 05:00 (2 minutos)  
**🎤 Presentador:** GABRIEL

### Script:

"Los números son alarmantes. Según reportes de APWG (Anti-Phishing Working Group) de 2024-2025:

**4.8 millones de ataques de phishing reportados en 2024.** Esto representa un _aumento del 87%_ respecto a 2023.

**En el segundo trimestre de 2025 solamente, se registraron 1.13 millones de ataques.** Es decir, aproximadamente 12,000 ataques _diarios_.

**Las pérdidas económicas globales superan los $2.8 mil millones anuales.** Esto incluye fraude directo, robo de identidad, y costos de recuperación.

**El 92% de los ataques de ransomware comienzan con phishing.** Los delincuentes usan phishing como puerta de entrada para desplegar malware más sofisticado.

**Sectores más afectados:** Banca (34%), Retail (22%), SaaS (18%), y Email service providers (12%).

¿Por qué estos números son tan altos? Porque los métodos actuales **no funcionan bien**. Veamos por qué."

---

## 📺 SLIDE 5: ¿Por qué fallan los métodos actuales?

**⏱️ Tiempo:** 05:00 - 06:30 (1.5 minutos)  
**🎤 Presentador:** GABRIEL

### Script:

"Los métodos tradicionales de detección de phishing tienen limitaciones serias:

**1. Listas negras (Blacklists):**
Las blacklists mantienen URLs conocidas de phishing. Pero los atacantes crean _nuevas URLs constantemente_. Una URL falsa es detectada, el atacante simplemente la descarta y crea una nueva. Es un juego del gato y el ratón que los defensores siempre pierden.

**2. Heurísticas manuales:**
Los expertos escriben reglas: 'Si la URL contiene números en la posición X, es sospechosa.' Pero los atacantes aprenden estas reglas y las evaden. Es reactivo, no proactivo.

**3. Análisis de contenido simplista:**
Buscar palabras clave como 'contraseña', 'actualizar', 'verificar'. Pero un atacante simplemente reemplaza esas palabras con sinónimos o esconde el contenido con obfuscación.

**4. Detección manual por usuarios:**
'¿Es esta una URL legítima?' La mayoría de usuarios no son expertos y caen en el engaño.

**La solución:** Usar _Machine Learning_ para aprender patrones complejos que los atacantes no pueden evadir fácilmente. En lugar de reglas estáticas, entrenamos modelos que se adaptan a nuevas amenazas."

---

## 📺 SLIDE 6: Nuestra Pregunta de Investigación

**⏱️ Tiempo:** 06:30 - 07:30 (1 minuto)  
**🎤 Presentador:** GABRIEL

### Script:

"Nuestra investigación se centra en una pregunta simple pero fundamental:

**'¿Cómo podemos detectar eficientemente sitios web de phishing utilizando Redes Neuronales Artificiales, mejorando sobre los baselines de Random Forest y SVM existentes, manteniendo interpretabilidad y tiempo real de predicción?'**

En otras palabras:

- ¿Podemos construir un modelo de deep learning que sea _mejor_ que los métodos clásicos?
- ¿Puede ejecutarse en _tiempo real_ (milisegundos)?
- ¿Podemos entender _por qué_ el modelo toma sus decisiones?

Nuestro objetivo es demostrar que una arquitectura MLP (Multi-Layer Perceptron) bien diseñada puede competir o superar los baselines del estado del arte, mientras es eficiente para despliegue en producción.

Ahora, ¿qué han hecho otros investigadores? Veamos el trabajo relacionado."

---

## 📺 SLIDE 7: Overview - Trabajos Relacionados

**⏱️ Tiempo:** 07:30 - 08:30 (1 minuto)  
**🎤 Presentador:** VALERIA

### Script:

"La detección de phishing no es un tema nuevo. Existe un cuerpo importante de investigación que podemos clasificar en 4 eras:

**Era 1 (2012-2014): Feature Engineering Manual**
Mohammad et al. publicaron trabajos pioneros donde extrajeron manualmente 17, luego 30 features de URLs y HTML. Esto estableció el baseline: ~84-97% accuracy.

**Era 2 (2015-2018): Machine Learning Clásico**
Investigadores aplicaron Random Forest, SVM, Naive Bayes, Gradient Boosting a los datasets de Mohammad. Lograron ~97-98% accuracy.

**Era 3 (2019-2021): Deep Learning**
Se experimentó con redes neuronales, LSTM, CNN. Los resultados fueron similares (~97-98%), pero el costo computacional fue mayor.

**Era 4 (2022-2025): Transformers y Modelos de Última Generación**
Modelos basados en Transformers y arquitecturas más complejas alcanzan ~98%+ accuracy. Pero son computacionalmente costosos.

**El gap que identificamos:** Ningún trabajo previo implementó un sistema _end-to-end en tiempo real_ con una API REST desplegada en producción. Nosotros vamos a hacerlo."

---

## 📺 SLIDE 8: Papers Fundacionales (Mohammad 2012, 2014)

**⏱️ Tiempo:** 08:30 - 10:30 (2 minutos)  
**🎤 Presentador:** VALERIA

### Script:

"Los pilares de toda investigación moderna en detección de phishing son los papers de Amir Mohammad:

**Mohammad et al. (2012) - 'Phishing Websites: A Learning-Based Classifier'**

En este paper, Mohammad et al. extrajeron **17 features** de URLs de phishing:

- _Features de URL:_ Presencia de '@', longitud de URL, presencia de IP en lugar de dominio, profundidad de URL, etc.
- _Features de DNS:_ ¿La página tiene registro DNS válido?
- _Features de contenido:_ ¿Hay formularios en la página? ¿El formulario envía datos fuera del dominio?

Usando estos 17 features, lograron **84% accuracy** con un Support Vector Machine (SVM).

**Mohammad et al. (2014) - 'Predicting Phishing Websites Using the Anti-Phishing Working Group Data'**

En este trabajo, Mohammad expandió el análisis a **30 features** organizados en 4 categorías:

1. **Address Bar features (12):** Presencia de '@', longitud, etc.
2. **Abnormal features (6):** ¿El servidor tiene HTTPS? ¿El certificado SSL es válido?
3. **HTML/JavaScript features (5):** Presencia de iframes, redirecciones, etc.
4. **Domain features (7):** Edad del dominio, reputación DNS, etc.

Con el dataset UCI (11,055 URLs), logró **97% accuracy** usando un Simple Shallow Neural Network (SSNN).

**Este es nuestro baseline.** Todos los trabajos posteriores usan el mismo dataset y tratan de superar este 97%."

---

## 📺 SLIDE 9: ML Clásico (Sahingoz 2019, Vrbančič 2020)

**⏱️ Tiempo:** 10:30 - 12:00 (1.5 minutos)  
**🎤 Presentador:** VALERIA

### Script:

"Después de Mohammad, otros investigadores intentaron mejorar los resultados usando técnicas de Machine Learning más avanzadas:

**Sahingoz et al. (2019) - 'Application of Machine Learning Algorithms for the Classification of Phishing Websites'**

Sahingoz et al. aplicaron **Random Forest** a los 30 features del dataset UCI.

_Resultado:_ **97.32% accuracy**, **99% AUC**.

Random Forest es simple pero efectivo. Usa múltiples árboles de decisión votados, lo que lo hace robusto contra overfitting.

**Vrbančič et al. (2020) - 'Datasets for Phishing Websites Detection'**

Vrbančič et al. probaron múltiples **algoritmos ensemble** (combinaciones de modelos):

- Random Forest
- Gradient Boosting
- Stacking
- AdaBoost

_Resultado mejor:_ **97.6% accuracy** usando una combinación de Gradient Boosting + Random Forest.

**Conclusión de esta era:** Los métodos clásicos alcanzan ~97-98%. Es difícil superar este techo sin técnicas más sofisticadas. La pregunta es: ¿pueden hacerlo las redes neuronales profundas?"

---

## 📺 SLIDE 10: Deep Learning y Estado del Arte (2022-2025)

**⏱️ Tiempo:** 12:00 - 13:30 (1.5 minutos)  
**🎤 Presentador:** VALERIA

### Script:

"Desde 2019 en adelante, los investigadores comenzaron a explorar arquitecturas más complejas:

**Chatterjee & Namin (2019) - 'Deep Reinforcement Learning for Phishing Detection'**

Usaron Deep Q-Networks (DQN) para aprender una política de detección. El modelo recibe el estado (features de URL), y aprende qué acciones tomar.

_Resultado:_ 97.8% accuracy. Ligeramente mejor que Random Forest, pero con complejidad significativamente mayor.

**Trabajos recientes (2022-2025) - Transformers y CNNs**

Investigadores han experimentado con:

- **Transformers:** BERT, GPT adaptados para clasificación. Aprenden patrones de texto en URLs y HTML.
- **CNNs:** Redes convolucionales para extraer características espaciales de imagenes de sitios web.
- **Hybrid architectures:** Combinaciones de CNN + LSTM + Attention mechanisms.

_Resultado del SOTA (State-of-the-Art):_ **98%+ accuracy**.

**PERO...** Estos modelos tienen limitaciones prácticas:

- Requieren **GPU para inferencia en tiempo real**
- Son **cajas negras** — difícil interpretar por qué clasifican algo como phishing
- **Overfitting frecuente** si el dataset es pequeño
- **Costo computacional alto** para despliegue en producción

Entonces, ¿dónde está el gap? Veamos."

---

## 📺 SLIDE 11: Posicionamiento de Nuestra Propuesta

**⏱️ Tiempo:** 13:30 - 15:00 (1.5 minutos)  
**🎤 Presentador:** VALERIA

### Script:

"Después de revisar toda la literatura, identificamos un **gap importante** en la investigación actual:

**El gap:** Ningún trabajo previo implementó un sistema **end-to-end, en tiempo real, con API REST desplegada en producción**.

La mayoría de papers muestran:

- ✅ Un modelo entrenado
- ✅ Accuracy en un dataset de prueba
- ❌ NO: Sistema desplegable en producción
- ❌ NO: API REST
- ❌ NO: Benchmarks de latencia
- ❌ NO: Comparación directa con soluciones comerciales

**Nuestra propuesta llena este gap:**

1. **Arquitectura MLP optimizada:** 4 capas (30→128→64→32→1) con Dropout y Batch Normalization.

2. **Entrenamiento riguroso:** Early stopping, validación cruzada 5-fold, regularización L2.

3. **Comparación justa:** Random Forest vs SVM vs MLP en el mismo dataset.

4. **Despliegue en producción:** API REST con Flask/FastAPI que puede procesar URLs en tiempo real.

5. **Interpretabilidad:** Feature importance analysis para entender qué features influyen más.

**Objetivo:** Demostrar que una arquitectura MLP **simple pero bien entrenada** puede ser tan buena (o mejor) que métodos clásicos, mientras sea **eficiente, interpretable, y desplegable en producción**.

Ahora, explicaremos el marco teórico."

---

## 📺 SLIDE 12: Marco Conceptual del Phishing

**⏱️ Tiempo:** 15:00 - 16:30 (1.5 minutos)  
**🎤 Presentador:** VALERIA

### Script:

"Antes de entrar en los detalles técnicos, necesitamos entender los conceptos fundamentales del phishing.

**Definición formal:**
Phishing es un ataque de ingeniería social donde un atacante intenta obtener información confidencial suplantando una entidad de confianza mediante comunicaciones electrónicas.

**Taxonomía del phishing (3 tipos):**

**1. Phishing basado en URL:**

- Atacante registra dominio similar al legítimo (typosquatting)
- Usa características visuales engañosas en la URL
- Ejemplo: 'amazn.com' vs 'amazon.com', o 'https://amazon.com.phishing.com'

**2. Phishing basado en contenido:**

- Página falsa visualmente idéntica a la legítima
- Manipulación de HTML/CSS para ocultamiento
- Uso de iframes, redirecciones, obfuscación de JavaScript
- Robo de keystrokes con JavaScript malicioso

**3. Phishing basado en DNS:**

- Compromiso de servidores DNS
- Redirección de nombres de dominio legítimos a IP falsas
- Envenenamiento de caché DNS

**Nuestro enfoque:**
Usamos features que capturan elementos de TODOS estos tipos:

- Features de URL (detección de typosquatting)
- Features de DNS (validación de registros)
- Features de contenido (análisis HTML/JavaScript)

Esto hace que nuestro modelo sea **generalista** — puede detectar múltiples variedades de phishing."

---

## 📺 SLIDE 13: Dataset UCI y sus Features

**⏱️ Tiempo:** 16:30 - 18:30 (2 minutos)  
**🎤 Presentador:** VALERIA

### Script:

"Nuestro dataset es el **UCI Phishing Websites Dataset**, publicado originalmente por Mohammad et al. (2014).

**Estadísticas del dataset:**

- **11,055 instancias** (URLs)
- **30 features** (atributos por URL)
- **Clasificación:** Binaria (Legítima vs Phishing)
- **Balanceo:** Aproximadamente 50% de cada clase

**Estructura de los 30 features en 4 categorías:**

**Categoría 1: Address Bar Features (12 features)**

- Presencia de '@' en la URL
- Presencia de '//' en la URL (después del protocolo)
- Presencia de '-' en el dominio
- Presencia de '-' en el subdominio
- Presencia de '?' en la URL
- Presencia de '%' en la URL
- Presencia de '#' en la URL
- Presencia de '&' en la URL
- Presencia de '~' en la URL
- Presencia de '.' en la URL
- Longitud de la URL
- Profundidad de la URL

**Categoría 2: Abnormal Features (6 features)**

- ¿Servidor tiene certificado SSL válido?
- ¿URL tiene sufijo HTTPS?
- ¿Dominio tiene registro DNS válido?
- ¿Dominio fue registrado hace poco (< 6 meses)?
- ¿URL redirige a otro dominio?
- ¿La solicitud WHOIS falla?

**Categoría 3: HTML/JavaScript Features (5 features)**

- Presencia de iframes
- Presencia de eventos onMouseOver maliciosos
- Presencia de cambios de estatus en la barra de estado
- Presencia de deshabilitación del click derecho
- Presencia de pop-ups

**Categoría 4: Domain Features (7 features)**

- Edad del dominio
- Reputación del dominio (APWG blacklist)
- Reputación del dominio (phishing search engines)
- Similitud del dominio vs dominio legítimo conocido
- Análisis de índices de búsqueda
- Estadísticas de tráfico

**Codificación:**
Cada feature es codificado como **ternario**: {-1, 0, 1}

- **1** = Característica presente / sospechosa
- **0** = No se puede determinar
- **-1** = Característica ausente / legítima

Esta codificación captura la intención del atacante: features presentes (1) sugieren phishing, mientras que su ausencia (-1) sugiere un sitio legítimo."

---

## 📺 SLIDE 14: Redes Neuronales Artificiales (MLP)

**⏱️ Tiempo:** 18:30 - 20:30 (2 minutos)  
**🎤 Presentador:** GABRIEL

### Script:

"Una Red Neuronal Artificial Multicapa (MLP) es una red de neuronas organizadas en capas que aprenden a través del backpropagation.

**Arquitectura de nuestro MLP:**

```
Input Layer (30 features)
    ↓
Hidden Layer 1 (128 neuronas, ReLU)
    ↓
Hidden Layer 2 (64 neuronas, ReLU)
    ↓
Hidden Layer 3 (32 neuronas, ReLU)
    ↓
Output Layer (1 neurona, Sigmoid)
    ↓
Clasificación (Legítima / Phishing)
```

**Componentes clave:**

**1. Capas de entrada y salida:**

- Entrada: 30 features del dataset UCI
- Salida: 1 neurona con función Sigmoid (produce probabilidad entre 0 y 1)

**2. Capas ocultas:**

- 3 capas ocultas con 128, 64, y 32 neuronas respectivamente
- Función de activación: **ReLU (Rectified Linear Unit)**
  - ReLU(x) = max(0, x)
  - Ventajas: No tiene problema del gradiente desvanecido, computacionalmente eficiente

**3. Función de pérdida:**

- **Binary Crossentropy** (pérdida de entropía cruzada binaria)
- Fórmula: L = -[y*log(ŷ) + (1-y)*log(1-ŷ)]
- Donde y es el label real, ŷ es la predicción

**4. Optimizador:**

- **Adam** (Adaptive Moment Estimation)
- Combina ventajas de Momentum y RMSprop
- Adapta la tasa de aprendizaje por parámetro

**5. Métrica de evaluación durante entrenamiento:**

- **Accuracy** en el conjunto de validación

**Principio de funcionamiento:**
Durante el entrenamiento, el modelo ajusta sus pesos (weights) minimizando la pérdida usando backpropagation — el algoritmo que propaga los errores hacia atrás a través de la red."

---

## 📺 SLIDE 15: Regularización y Técnicas de Entrenamiento

**⏱️ Tiempo:** 20:30 - 22:00 (1.5 minutos)  
**🎤 Presentador:** GABRIEL

### Script:

"Para evitar overfitting y mejorar la generalización, aplicamos 3 técnicas de regularización importantes:

**1. Dropout (Tasa: 0.3 entre capas)**

Dropout desactiva aleatoriamente el 30% de las neuronas durante el entrenamiento.

Ventajas:

- Previene **co-adaptation** entre neuronas
- Fuerza a la red a aprender características redundantes
- Actúa como un "ensemble" implícito de redes

Implementación: Entre cada capa oculta, agregamos una capa Dropout con p=0.3.

**2. Batch Normalization**

Normaliza la entrada de cada capa durante el entrenamiento, escalando a media=0 y desviación estándar=1.

Ventajas:

- Acelera el entrenamiento
- Reduce la dependencia en inicialización de pesos
- Actúa como regularizador

Implementación: Después de cada capa densa, agregamos BatchNormalization.

**3. Early Stopping**

Monitoreamos la pérdida en el conjunto de validación. Si no mejora después de 10 epochs consecutivos, detenemos el entrenamiento.

Ventajas:

- Evita overfitting
- Ahorra tiempo de computación
- Encuentra el punto óptimo

**Proceso de entrenamiento:**

1. **Dividir datos:** 70% entrenamiento, 15% validación, 15% prueba
2. **Validación cruzada:** 5-fold para estimación robusta
3. **Épocas:** Hasta 200 (con early stopping)
4. **Batch size:** 32 muestras
5. **Tasa de aprendizaje:** 0.001 (learning rate inicial)

**Métricas de evaluación final:**

- Accuracy
- Precision
- Recall
- F1-Score
- AUC-ROC
- Matriz de confusión"

---

## 📺 SLIDE 16: Resultados Preliminares (Entrega 2)

**⏱️ Tiempo:** 22:00 - 23:30 (1.5 minutos)  
**🎤 Presentador:** GABRIEL

### Script:

"En la Entrega 2, completamos la fase de exploración y entrenamientos de baseline. Aquí están los resultados:

**Baseline 1: Random Forest (50 árboles)**

```
Accuracy:  97.04%
Precision: 96.89%
Recall:    97.18%
F1-Score:  97.03%
AUC-ROC:   0.9904 (99.04%)
```

Random Forest estableció un **baseline fuerte**. Es difícil de superar.

**Baseline 2: SVM (Kernel RBF)**

```
Accuracy:  95.32%
Precision: 94.78%
Recall:    95.87%
F1-Score:  95.32%
AUC-ROC:   0.9798 (97.98%)
```

SVM es más débil que Random Forest en este dataset. Probablemente porque los features no son perfectamente separables linealmente en el espacio original.

**Comparación visual:**

| Modelo        | Accuracy | AUC-ROC |
| ------------- | -------- | ------- |
| Random Forest | 97.04%   | 99.04%  |
| SVM (RBF)     | 95.32%   | 97.98%  |

**Lo que sigue:**
En las próximas entregas (Entrega 4, 5, 6), entrenaremos nuestro MLP y compararemos directamente con estos baselines.

Nuestro objetivo es que el MLP alcance **al menos 97% accuracy** — igualar a Random Forest sería un éxito, superarlo sería excepcional."

---

## 📺 SLIDE 17: Próximos Pasos

**⏱️ Tiempo:** 23:30 - 24:00 (30 segundos)  
**🎤 Presentador:** GABRIEL

### Script:

"El proyecto continúa con 3 entregas más:

**Entrega 4 (Junio 3, 2026):**

- Paper en formato IEEE de ~3 páginas
- Resumen de metodología, resultados preliminares, e impacto

**Entrega 5 (Julio 1, 2026):**

- Presentación final
- **Demostración en vivo** de API REST en tiempo real
- Sistema completamente funcional

**Entrega 6 (Julio 5, 2026):**

- Paper final IEEE completo (~6 páginas)
- Todos los resultados, análisis detallado, discusión, conclusiones

Ahora, pasamos a preguntas."
