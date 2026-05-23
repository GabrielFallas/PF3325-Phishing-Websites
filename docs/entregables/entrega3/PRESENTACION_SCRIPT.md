# Guión para la Presentación: Detección de Phishing mediante Redes Neuronales Artificiales

**Curso:** PF3325 – Redes Computacionales  
**Expositores:** Gabriel Fallas & Valeria Chinchilla  
**Tiempo Total Estimado:** 15 Minutos (⏱️ ~1:15 min por diapositiva)  

---

## 📋 Recomendaciones Generales antes de Iniciar:
1. **Ritmo:** Mantengan un habla pausada pero firme. 15 minutos pasan rápido, eviten redundancias.
2. **Postura:** Al proyectar en formato síncrono o presencial, no lean la pantalla. El guión complementa la diapositiva, no la duplica.
3. **Señalización:** Utilicen frases como *"Como pueden observar a la derecha de la pantalla..."* para dirigir la atención del público.

---

## 🛝 Diapositiva 1: Portada y Presentación
* **Tiempo:** 0:00 - 1:00  
* **Expositor Principal:** Gabriel Fallas (Introduce el tema, Valeria apoya).
* **Elemento Visual Clave:** Título principal en tipografía serif clásica, colores institucionales (Azul y Crema).

### 🗣️ Texto del Guión:
**Gabriel:** "Muy buenos días profesor y compañeros. Mi nombre es Gabriel Fallas y, junto a mi compañera Valeria Chinchilla, nos complace presentarles nuestro proyecto de investigación para el curso de Redes Computacionales titulado: *'Detección de Phishing mediante Redes Neuronales Artificiales'*. 

Este trabajo se enfoca en cómo la inteligencia artificial, específicamente los modelos basados en redes densas, pueden convertirse en la primera línea de defensa activa ante una de las amenazas más persistentes y dañinas en la infraestructura de la red global actual."

---

## 🛝 Diapositiva 2: Agenda de la Presentación
* **Tiempo:** 1:00 - 2:00  
* **Expositor Principal:** Valeria Chinchilla  
* **Elemento Visual Clave:** Grid de tres bloques que divide la exposición en Motivación, Estado del Arte y Marco Teórico.

### 🗣️ Texto del Guión:
**Gabriel:** "Para aprovechar al máximo este espacio de 15 minutos, hemos dividido nuestra ponencia en tres bloques fundamentales. 

Primero, abordaremos la **Motivación**, donde explicaremos la anatomía de un ataque de phishing y por qué los métodos de detección actuales se están quedando obsoletos. En segundo lugar, revisaremos el **Estado del Arte**, analizando cómo ha evolucionado la literatura científica y los papers que sientan las bases de nuestro diseño. Finalmente, expondremos el **Marco Teórico**, detallando las características de la base de datos de la Universidad de California en Irvine (UCI), la arquitectura de nuestra red neuronal perceptrón multicapa y las métricas preliminares evaluadas."

---

## 🛝 Diapositiva 3: ¿Qué es el Phishing? Conceptos Base
* **Tiempo:** 2:00 - 3:15  
* **Expositor Principal:** Gabriel Fallas  
* **Elemento Visual Clave:** Lista estilizada de vectores de ataque y la gráfica de deconstrucción de una URL maliciosa.

### 🗣️ Texto del Guión:
**Gabriel:** "Antes de profundizar en la matemática del problema, debemos comprender qué estamos combatiendo. El phishing es una técnica de ingeniería social donde un actor malicioso suplanta la identidad de una entidad de confianza —como un banco o un servicio en la nube— con el fin de robar credenciales.

A nivel de red y de arquitectura de software, los atacantes manipulan los protocolos de nombres de dominio de tres formas principales que vemos en pantalla:
1. El **Typosquatting**, que consiste en registrar dominios con errores ortográficos mínimos que engañan al ojo humano, como `paypa1.com`.
2. El uso deliberado de **Subdominios complejos** donde ocultan el verdadero dominio de destino.
3. El uso directo de **Direcciones IP en la URL**, saltándose por completo la resolución DNS legítima. Capturar estos patrones de manera automática es el núcleo de nuestra investigación."

---

## 🛝 Diapositiva 4: Impacto Global (Estadísticas)
* **Tiempo:** 3:15 - 4:30  
* **Expositor Principal:** Valeria Chinchilla  
* **Elemento Visual Clave:** El número gigante de "4.8M" y el recuadro de texto destacado sobre la vida útil de las URLs.

### 🗣️ Texto del Guión:
**Gabriel:** "Para entender la magnitud del problema, observemos los datos duros provistos por el Grupo de Trabajo Antiphishing (APWG). En el último año fiscalizado se reportó la exorbitante cifra de **4.8 millones de ataques globales**. Solo los ataques de tipo BEC (o compromiso de correos corporativos) generaron pérdidas por más de 2.8 billones de dólares.

Pero el dato más crítico para nuestra justificación técnica está abajo a la derecha: *la vida útil de un sitio de phishing suele ser menor a 24 horas*. Esto significa que un atacante levanta el servidor web malicioso, estafa a cientos de usuarios y lo da de baja antes de que las autoridades puedan reaccionar."

---

## 🛝 Diapositiva 5: Limitaciones de los Métodos Actuales
* **Tiempo:** 4:30 - 5:45  
* **Expositor Principal:** Gabriel Fallas  
* **Elemento Visual Clave:** Dos bloques contrastantes: el bloque oscuro de Listas Negras frente al bloque claro de Heurísticas.

### 🗣️ Texto del Guión:
**Gabriel:** "Sabiendo que los sitios duran menos de un día activos, los mecanismos de defensa tradicionales basados en firmas fracasan. Las **Listas Negras (o Blacklists)** son reactivas: dependen de que un usuario sea estafado, reporte el sitio, un administrador lo verifique y se actualice la base de datos mundial. Para cuando la URL está en la lista negra, el atacante ya migró a otro dominio.

Por otro lado, las **Heurísticas Manuales**, es decir, reglas fijas programadas por ingenieros como 'si la URL tiene más de 75 caracteres es maliciosa', son fácilmente evadidas por los atacantes modificando ligeramente el código o la estructura del enlace. Es por esto que necesitamos algoritmos predictivos basados en Machine Learning."

---

## 🛝 Diapositiva 6: Pregunta de Investigación y Modelo Matemático
* **Tiempo:** 5:45 - 7:00  
* **Expositor Principal:** Valeria Chinchilla  
* **Elemento Visual Clave:** Formulación matemática del clasificador binario mediante la función por partes en MathML.

### 🗣️ Texto del Guión:
**Gabriel:** "Esto nos lleva a formular la pregunta central de nuestro proyecto: *¿Es viable diseñar una Red Neuronal Artificial capaz de clasificar estas URLs en tiempo real con una precisión competitiva frente al estado del arte?*

Matemáticamente, estamos modelando un **Clasificador Binario estricto**. Definimos una función $f(x)$ donde nuestra entrada $x$ es un vector dimensional en un espacio $\mathbb{R}^{30}$ —que representa las 30 características extraídas de la URL—. El modelo debe mapear esa entrada y retornar de forma determinista un valor de **1** si el sitio cuenta con los patrones estructurales de una página legítima, o un valor de **0** si es categorizado como Phishing."

---

## 🛝 Diapositiva 7: Cronograma y Evolución del Estado del Arte
* **Tiempo:** 7:00 - 8:15  
* **Expositor Principal:** Gabriel Fallas  
* **Elemento Visual Clave:** Línea de tiempo horizontal con nodos dorados que van desde el 2008 hasta el 2025.

### 🗣️ Texto del Guión:
**Valeria:** "Para no reinventar la rueda, analizamos cómo la comunidad científica ha abordado este problema en los últimos 15 años. Como se aprecia en esta línea de tiempo, en 2008 las investigaciones utilizaban Redes Neuronales muy simples con tasas de error elevadas debido a la falta de datos homogéneos. 

El punto de inflexión ocurre entre 2012 y 2014, cuando los investigadores Mohammad, Thabtah y McCluskey logran estandarizar los criterios de extracción de características de las URLs, culminando en la publicación del dataset de la UCI, el cual se convirtió en el estándar de la industria (o *benchmark*) sobre el cual construimos nuestra propuesta."

---

## 🛝 Diapositiva 8: Papers Fundacionales
* **Tiempo:** 8:15 - 9:30  
* **Expositor Principal:** Valeria Chinchilla  
* **Elemento Visual Clave:** Tabla comparativa formal con cabecera azul marino.

### 🗣️ Texto del Guión:
**Valeria:** "En esta tabla resumimos los cuatro pilares bibliográficos de nuestra investigación. Queremos destacar el trabajo de Mohammad del 2014, quienes utilizando una Red Neuronal Monocapa (SSNN) sobre un dataset de 11,055 URLs lograron un 97% de precisión. 

Posteriormente, en 2019 y 2020, autores como Sahingoz y Vrbančič exploraron algoritmos de árboles de decisión como Random Forest y XGBoost, alcanzando un techo técnico de entre 97.3% y 97.6%. Nuestro objetivo en este laboratorio de cómputo es analizar si modificando la profundidad y las técnicas de regularización de una red neuronal densa podemos superar o igualar este rendimiento con un menor costo computacional en la inferencia."

---

## 🛝 Diapositiva 9: Análisis del Dataset UCI Phishing Websites
* **Tiempo:** 9:30 - 10:45  
* **Expositor Principal:** Gabriel Fallas  
* **Elemento Visual Clave:** Bloque lateral que explica la codificación ternaria (+1, 0, -1).

### 🗣️ Texto del Guión:
**Valeria:** "Hablemos ahora del set de datos. El Dataset de la UCI no contiene el texto crudo de las URLs, sino que preprocesa cada sitio web en **30 características estructuradas**, divididas en cuatro grandes dominios que ven en pantalla: propiedades de la barra de direcciones, anomalías en los enlaces internos, análisis del código fuente HTML/JavaScript y estadísticas de reputación del dominio.

Lo verdaderamente interesante de este set de datos es su **Codificación Ternaria**. Cada característica se normaliza discretamente en tres valores: **+1** si el comportamiento es completamente limpio o legítimo, **0** si es dudoso o sospechoso, y **-1** si exhibe un comportamiento inequívoco de phishing. Esto simplifica el espacio de búsqueda para el optimizador de la red."

---

## 🛝 Diapositiva 10: Arquitectura de la Red (MLP) y Función de Pérdida
* **Tiempo:** 10:45 - 12:00  
* **Expositor Principal:** Valeria Chinchilla  
* **Elemento Visual Clave:** Diagrama de capas de la red neuronal y la ecuación matemática de Entropía Cruzada Binaria.

### 🗣️ Texto del Guión:
**Valeria:** "Para procesar estos vectores, diseñamos una red neuronal de tipo **Perceptrón Multicapa (MLP)**. La capa de entrada cuenta estrictamente con 30 neuronas, una por cada atributo del dataset. Proponemos una estructura de capas ocultas densas totalmente conectadas utilizando funciones de activación **ReLU** (Unidad Lineal Rectificada) para evitar el desvanecimiento del gradiente.

Dado que nuestro objetivo es la clasificación binaria, la capa de salida consta de una única neurona con activación **Sigmoide**, la cual nos entrega un valor continuo entre 0 y 1 que interpretamos como la probabilidad de riesgo. La optimización del modelo se realiza mediante la función de pérdida de **Entropía Cruzada Binaria** o *Binary Cross-Entropy*, detallada en la pantalla, la cual penaliza exponencialmente las clasificaciones erróneas durante el *backpropagation*."

---

## 🛝 Diapositiva 11: Resultados Preliminares y Siguientes Pasos
* **Tiempo:** 12:00 - 13:30  
* **Expositor Principal:** Gabriel Fallas  
* **Elemento Visual Clave:** Gráfico de barras horizontales que compara los algoritmos y la nota destacada con el icono del matraz de laboratorio.

### 🗣️ Texto del Guión:
**Valeria:** "En nuestra fase de pruebas base y replicación de entornos, implementamos modelos tradicionales de comparación. Como observamos en el gráfico, los clasificadores de ensamble como *Random Forest* mantienen la ventaja histórica con un 97% de precisión, seguidos de cerca por los modelos de vectores de soporte (SVM) con un 95%.

Nuestra hipótesis de investigación plantea que los modelos clásicos fallan en capturar interacciones no lineales complejas entre las características del HTML y las del dominio al mismo tiempo. Por lo tanto, nuestro siguiente paso inmediato en el proyecto —marcado en el bloque inferior— es realizar un **estudio ablativo completo**. Evaluaremos de forma sistemática el impacto de variar la profundidad de la red, y la inclusión de capas de *Dropout* y *Batch Normalization* para mitigar el sobreajuste y estabilizar el aprendizaje."

---

## 🛝 Diapositiva 12: Conclusión y Sesión de Preguntas
* **Tiempo:** 13:30 - 15:00  
* **Expositor Principal:** Ambos (Gabriel modera las preguntas, Valeria complementa).
* **Elemento Visual Clave:** Icono central de conversación y los datos de contacto de ambos expositores.

### 🗣️ Texto del Guión:
**Valeria:** "A modo de conclusión, la detección de phishing mediante inteligencia artificial no es solo una alternativa teórica, sino una necesidad de infraestructura indispensable en las redes modernas para combatir ataques dinámicos de corto ciclo de vida. Esperamos que este enfoque de red densa optimizada proporcione un balance óptimo entre latencia de procesamiento y precisión."

**Gabriel:** "Agradecemos enormemente su atención el día de hoy. Abrimos formalmente el espacio para cualquier duda, comentario o sugerencia que tengan sobre la arquitectura de la red o la naturaleza del set de datos. Muchas gracias."