# Guion de Presentación — Entrega 5 (~10 min)

> **Fecha:** 1 de julio de 2026
> **Presentadores:** Gabriel Fallas & Valeria Chinchilla
> **Material:** `presentacion.html` (9 slides) + demo en vivo (`localhost:8000`)

## Antes de empezar

- Abrir `presentacion.html` en el navegador (F11 para pantalla completa)
- Dejar la API corriendo en otra pestaña:
  ```bash
  uvicorn src.api_phishing:app --reload
  ```
- Navegar con `→ / ←` o barra espaciadora

## Reparto
- **Gabriel:** slides 1–4 (portada → trabajo relacionado)
- **Valeria:** slides 5–9 (implementación → conclusiones) + demo en vivo

---

## Guion

### Slide 1 — Portada · (0:00–0:15) — *Gabriel*
"Buenas, somos Gabriel y Valeria. Vamos a presentar nuestro proyecto de detección de sitios de phishing con redes neuronales."

---

### Slide 2 — Introducción / Contexto · (0:15–1:15) — *Gabriel*
"El phishing es básicamente cuando alguien crea un sitio falso que parece legítimo para robarte la contraseña o los datos bancarios.

Lo que nosotros construimos es un sistema completo para detectar esos sitios. Usamos el dataset UCI Phishing Websites, que tiene 11 055 sitios etiquetados con 30 características cada uno. Y lo importante es que no nos quedamos solo en el experimento — lo pusimos a funcionar como un servicio real."

---

### Slide 3 — Motivación · (1:15–2:15) — *Gabriel*
"El problema es bastante serio: la APWG reportó 4.8 millones de ataques de phishing en 2024, el récord histórico. Y lo que lo hace difícil de combatir es que un sitio de phishing típicamente vive menos de 24 horas antes de ser bloqueado — para ese momento ya hizo el daño.

Las defensas clásicas no alcanzan ese ritmo. Las listas negras son reactivas y las reglas manuales se evaden fácil. Por eso tiene sentido usar machine learning: el modelo aprende los patrones de los datos en vez de que alguien los codifique a mano."

---

### Slide 4 — Trabajo relacionado · (2:15–3:15) — *Gabriel*
"Hay unos 15 años de investigación en esto. Varios grupos llegaron a 97-98% de accuracy con distintas técnicas. Pero si ven la tabla, todos tienen algo en común: ninguno hizo un servicio real. Solo clasificaron datasets estáticos en un experimento académico.

Esa es exactamente la brecha que nosotros cerramos — hacer algo que funcione con una URL nueva, en tiempo real."

---

### Slide 5 — Implementación: clasificación asíncrona · (3:15–4:45) — *Valeria*
"La primera parte de la implementación es la clasificación asíncrona, que fue el trabajo del inicio del semestre.

Tomamos el dataset, lo preprocesamos con StandardScaler y lo dividimos en 70% entrenamiento, 15% validación y 15% test. Entrenamos tres modelos: Random Forest, SVM y el MLP que es nuestra red neuronal. El MLP tiene tres capas ocultas de 128, 64 y 32 neuronas, con Batch Normalization, Dropout y Early Stopping para no sobreajustar. Todo el modelo y el scaler quedan guardados en disco para usarlos en tiempo real."

---

### Slide 6 — Implementación: clasificación en tiempo real · (4:45–6:15) — *Valeria*
"La segunda parte es la clasificación en tiempo real, y en esta entrega hicimos dos cosas.

La primera es la API REST con FastAPI. Recibe una URL, extrae los 30 features en vivo — hace el handshake TLS real, baja el HTML, consulta DNS y WHOIS — y devuelve el veredicto en menos de un segundo. 24 de los 30 features se miden en vivo; 6 no se pueden medir porque los servicios de donde venían ya no existen, como Alexa que cerró en 2022. Originalmente esta API era el entregable principal de esta entrega, pero se decidió moverla al laboratorio.

La segunda cosa que hicimos fue agregar una comparación de tiempos de inferencia entre los tres modelos — 50 repeticiones, 1 659 muestras, tiempo promedio por muestra.

*[Demo en vivo → localhost:8000]*
Probemos con github.com... vemos que sale Legítimo, y la tabla muestra qué features se midieron en vivo y cuáles son default."

---

### Slide 7 — Resultados: métricas · (6:15–7:30) — *Valeria*
"Evaluamos los tres modelos con el test set de 1 659 muestras que nunca habían visto. Random Forest tiene la mejor accuracy con 97.2%, pero la métrica que más importa en seguridad es el recall — de todos los sitios phishing, ¿cuántos detectamos?

El MLP tiene el recall más alto: 98.8%. Un falso negativo en seguridad es un sitio phishing que llega al usuario y roba sus datos, así que eso es lo que queremos minimizar. Los 47 falsos positivos solo generan una alerta innecesaria, que es mucho menos grave."

---

### Slide 8 — Resultados: tiempos + visualizaciones · (7:30–8:45) — *Valeria*
"En cuanto a los tiempos: Random Forest es el más rápido con 8 microsegundos por muestra, el MLP tarda 20 y la SVM 53. Pero el punto importante es que en la API real el clasificador no es el cuello de botella — descargar la página puede tardar segundos. Los 20 µs del MLP son irrelevantes, así que elegirlo por su mejor recall no nos cuesta nada en velocidad.

Las figuras confirman lo que dicen los números: solo 11 sitios phishing de 924 se nos escaparon, y las curvas ROC de los tres modelos están todas por encima de 0.98 de AUC."

---

### Slide 9 — Conclusiones · (8:45–9:30) — *Valeria*
"En resumen: construimos un MLP con 96.5% de accuracy y 98.8% de recall, y lo pusimos a funcionar como un sistema completo con extractor de features, API REST y demo web. La diferencia respecto a los trabajos anteriores es que esto es desplegable — no es solo un experimento.

Siendo honestos, el dataset es de 2014 y el phishing ha evolucionado, así que nuestras métricas pueden estar un poco sobreestimadas para el mundo real de hoy. Gracias, ¿alguna pregunta?"

---

## Posibles preguntas

- **¿Por qué el MLP si Random Forest da más accuracy?** Porque el recall del MLP es más alto (98.8% vs 98.1%), y en seguridad eso es lo que importa. Además es la base del proyecto de redes neuronales del curso.
- **¿Qué pasa si la página no carga?** El extractor usa solo los features que pudo medir. La confianza baja y la procedencia lo refleja.
- **¿Cómo evitan data leakage?** El StandardScaler se ajusta solo con el split de entrenamiento; validación y test usan esa misma transformación.

---
*PF3325 Redes | Gabriel Fallas & Valeria Chinchilla | Julio 2026*
