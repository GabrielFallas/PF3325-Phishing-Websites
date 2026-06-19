# Entrega 5 — Guion de Presentación (10–12 min)

> **Curso:** PF3325 – Redes · **Fecha:** Miércoles 1 de julio de 2026
> **Presentadores:** Gabriel Fallas & Valeria Chinchilla
> **Material:** `presentacion.html` (13 slides) + demo en vivo de la API

## Cómo presentar

1. Abrir `presentacion.html` en el navegador (pantalla completa con `F11`).
2. Navegar con `→ / ←` (o barra espaciadora). La barra superior marca el progreso.
3. Antes de empezar, dejar la API corriendo en otra pestaña para la demo:
   ```bash
   uvicorn src.api_phishing:app --reload     # luego abrir http://localhost:8000
   ```

## Reparto sugerido
- **Gabriel:** slides 1–6 (motivación → modelo)
- **Valeria:** slides 7–13 (tiempo real → conclusión) + demo en vivo

---

## Guion por slide

### Slide 1 — Portada · (0:00–0:30)
> "Buenos días. Somos Gabriel y Valeria. Nuestro proyecto es la detección de
> sitios de phishing con redes neuronales, y en esta entrega final dimos el paso
> de la clasificación offline a la **detección en tiempo real**."

### Slide 2 — Motivación · (0:30–2:00)
> "El phishing no para de crecer: la APWG registró **4.8 millones** de ataques en
> 2024, un récord. Lo crítico es que un sitio vive **menos de 24 horas** antes de
> ser bloqueado — para entonces ya robó credenciales."
>
> "Las defensas clásicas se quedan cortas: las **listas negras** son reactivas y
> las **heurísticas manuales** se evaden. Por eso usamos **machine learning**:
> aprende los patrones en vez de codificar reglas a mano."

### Slide 3 — Trabajo relacionado · (2:00–3:00)
> "Hay 15 años de investigación, desde Mohammad en 2012 hasta ensembles modernos
> con más de 97% de accuracy. Pero **todos comparten una limitación**: tratan el
> problema como un experimento offline. Ninguno publica un **servicio que reciba
> una URL nueva y la clasifique al instante**. Esa brecha es nuestra contribución."

### Slide 4 — Dataset · (3:00–4:00)
> "Usamos el dataset UCI Phishing Websites: **11 055 sitios** y **30 features** en
> cuatro categorías. La codificación es ternaria: +1 legítimo, 0 sospechoso, −1
> phishing. Mantenemos el 0 porque aporta información que un flag binario
> perdería. Las clases están balanceadas, así que no hace falta tratamiento
> especial de desbalance."

### Slide 5 — Arquitectura del sistema · (4:00–4:45)
> "Este es el sistema completo. Arriba, la rama **offline**: dataset →
> preprocesamiento → entrenamiento → evaluación → persistencia del modelo y el
> scaler. Abajo, la rama de **tiempo real** reutiliza esos artefactos: URL →
> extractor → scaler → MLP → veredicto. Ambas comparten el mismo modelo."

### Slide 6 — Modelo MLP · (4:45–5:45)
> "La red es un MLP: capas densas de 128, 64 y 32 neuronas y una salida sigmoide.
> Para evitar sobreajuste combinamos **Batch Normalization, Dropout, regularización
> L2 y Early Stopping**. Son apenas 15 105 parámetros — ligero y rápido."
>
> *(Transición a Valeria.)*

### Slide 7 — Extractor de features · (5:45–7:00)
> "El corazón de la parte en tiempo real es el **extractor**: convierte una URL
> cruda en los 30 features. De la URL sacamos longitud, IP, acortadores; hacemos
> un **handshake TLS real**, contamos redirects, parseamos el HTML para anchors,
> formularios e iframes, y consultamos **DNS y WHOIS**."
>
> "Pero somos **honestos**: 6 de los 30 features dependían de servicios que **ya
> no existen** — Alexa cerró en 2022, el PageRank público en 2016. Para esos
> usamos un valor por defecto y **reportamos la procedencia** de cada feature:
> cuáles se midieron en vivo y cuáles no. En un sitio normal medimos **24 de 30**."

### Slide 8 — API + demo · (7:00–7:45)
> "Todo se expone con **FastAPI** en tres endpoints: clasificar un vector,
> clasificar una URL cruda, y una demo web. La inferencia es **sub-segundo**.
> Ahora lo vemos funcionando."
>
> **➡️ DEMO EN VIVO** (cambiar a `localhost:8000`):
> - Probar `github.com` → debe dar **Legítimo** con alta confianza.
> - Probar la URL sospechosa de ejemplo → mostrar la tabla de features y la
>   etiqueta `measured` / `default`.
> - Resaltar el contador "24/30 features medidas en vivo".

### Slide 9 — Resultados · (7:45–9:00)
> "Evaluamos los tres modelos en el mismo test set de 1 659 muestras. Random
> Forest lidera en accuracy con 97.2%, pero miren el **recall**: el **MLP logra
> 98.8%**, el más alto de todos. En seguridad el recall manda — un falso negativo
> es un sitio phishing que **sí llega al usuario**."

### Slide 10 — Matriz de confusión · (9:00–9:45)
> "Aquí se ve por qué: el MLP solo deja pasar **11 sitios phishing de 924**. Tiene
> 47 falsos positivos, pero esos apenas muestran una alerta al usuario. El modelo
> prioriza **atrapar el phishing** — el balance correcto para un filtro."

### Slide 11 — ROC · (9:45–10:15)
> "Las curvas ROC confirman que los tres modelos están muy por encima del azar,
> todos sobre 0.98 de AUC. MLP y Random Forest son casi indistinguibles, y el
> entrenamiento fue estable, sin sobreajuste gracias a la regularización."

### Slide 12 — Limitaciones · (10:15–11:00)
> "Somos transparentes con las limitaciones: el dataset es de 2014, hay un shift
> de distribución por los servicios desaparecidos, y descargar la página añade
> latencia. A futuro: reentrenar con un dataset moderno de features léxicas
> 100% reproducibles, y agregar caché y confianza calibrada a la API."

### Slide 13 — Conclusión · (11:00–12:00)
> "En resumen: construimos un sistema **end-to-end**. Un MLP con 96.5% de accuracy
> y 98.8% de recall, **más un servicio de detección en tiempo real** — extractor,
> API y demo — que es justo el componente desplegable que faltaba en los trabajos
> fundacionales. Gracias, ¿preguntas?"

---

## Posibles preguntas (Q&A)

- **¿Por qué el MLP si Random Forest da más accuracy?** Por el recall (98.8% vs
  98.1%) y porque la red es la base extensible del proyecto (curso de redes
  neuronales). RF queda como baseline fuerte y barato.
- **¿Qué pasa si la página no carga?** Caen los features medidos en vivo y el
  veredicto se apoya en señales solo-URL; la confianza baja y la procedencia lo
  refleja. Es una propiedad inherente de la extracción en tiempo real.
- **¿Cómo evitan el data leakage?** El `StandardScaler` se ajusta **solo** con el
  split de entrenamiento; validación y test usan esa misma transformación.
- **¿Es seguro el scraping?** Se hace con timeout corto y sin ejecutar JS; para
  producción se añadiría sandboxing y rate-limiting.

---
*Entrega 5 – PF3325 Redes | Gabriel Fallas & Valeria Chinchilla | Julio 2026*
