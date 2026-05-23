# Entrega 3 — Presentación en Clase

**Fecha:** Miércoles 27 de mayo de 2026  
**Duración:** ~25-27 minutos  
**Formato:** Presentación oral interactiva con diapositivas HTML  
**Equipo:** Gabriel Fallas & Valeria Chinchilla  
**Curso:** PF3325 – Redes Computacionales  
**Universidad:** Universidad de Costa Rica

---

## 📁 Archivos de Entrega 3

### **Documentos de Presentación**

| Archivo | Descripción | Uso |
|---------|-------------|-----|
| **[`presentacion.html`](presentacion.html)** | 🎨 **Presentación interactiva HTML** — 18 diapositivas navegables con diseño profesional, animaciones, y barra de progreso. | **Proyectar en clase** — Abre en cualquier navegador (Firefox, Chrome, Edge). Navega con botones o teclas de flecha. |
| **[`SCRIPT_PRESENTACION.md`](SCRIPT_PRESENTACION.md)** | 📋 **Guión detallado para presentadores** — Script completo palabra-por-palabra, notas pedagógicas, tiempos, preguntas esperadas con respuestas preparadas, y tips de oratoria. | **Para preparación** — Gabriel y Valeria practiquen su sección (ver timeline abajo). |
| **[`ENTREGA3_PRESENTACION.md`](ENTREGA3_PRESENTACION.md)** | 📖 **Guía original completa** — Contiene el contexto académico, referencias detalladas, y estructura de cada diapositiva. | **Para referencia académica** — Consultar cuando necesites más contexto sobre el contenido. |

---

## ⏱️ Timeline de Presentación

**Duración Total: 25-27 minutos**

```
00:00 - 00:30  │  PORTADA                        │  GABRIEL (30 seg)
00:30 - 01:00  │  AGENDA                         │  GABRIEL (30 seg)
01:00 - 03:00  │  El Problema del Phishing       │  GABRIEL (2 min)
03:00 - 05:00  │  Impacto Real: Estadísticas     │  GABRIEL (2 min)
05:00 - 06:30  │  ¿Por qué fallan métodos?       │  GABRIEL (1.5 min)
06:30 - 07:30  │  Pregunta de Investigación      │  GABRIEL (1 min)
07:30 - 08:30  │  Overview Trabajos Relacionados │  VALERIA (1 min)
08:30 - 10:30  │  Papers Fundacionales (M12/14)  │  VALERIA (2 min)
10:30 - 12:00  │  ML Clásico (Sahingoz, Vrbančič)│  VALERIA (1.5 min)
12:00 - 13:30  │  Deep Learning y SOTA           │  VALERIA (1.5 min)
13:30 - 15:00  │  Posicionamiento de Propuesta   │  VALERIA (1.5 min)
15:00 - 16:30  │  Marco Conceptual del Phishing  │  GABRIEL (1.5 min)
16:30 - 18:30  │  Dataset UCI y Features         │  GABRIEL (2 min)
18:30 - 20:30  │  Redes Neuronales (MLP)         │  VALERIA (2 min)
20:30 - 22:00  │  Regularización y Técnicas      │  VALERIA (1.5 min)
22:00 - 23:30  │  Resultados Preliminares        │  GABRIEL (1.5 min)
23:30 - 24:00  │  Próximos Pasos                 │  GABRIEL (30 seg)
24:00 - 27:00  │  Preguntas y Respuestas         │  AMBOS (3 min)
```

---

## 📊 Estructura de la Presentación (18 diapositivas)

### **SECCIÓN (a): Motivación y Problema** — Gabriel (6.5 min)
| # | Título | Tiempo |
|---|--------|:------:|
| 1 | Portada | 30 seg |
| 2 | Agenda | 30 seg |
| 3 | ¿Qué es el Phishing? | 2 min |
| 4 | Impacto Real: Estadísticas 2024-2025 | 2 min |
| 5 | ¿Por qué fallan los métodos actuales? | 1.5 min |
| 6 | Nuestra Pregunta de Investigación | 1 min |

**Temas:** Definición de phishing (URL-based, content-based, DNS-based) · Estadísticas alarmantes (4.8M ataques 2024, $2.8B pérdidas) · Limitaciones de blacklists y heurísticas · Transición a Machine Learning

---

### **SECCIÓN (b): Trabajo Relacionado** — Valeria (6.5 min)
| # | Título | Tiempo |
|---|--------|:------:|
| 7 | Overview: Trabajos Relacionados | 1 min |
| 8 | Papers Fundacionales (Mohammad 2012, 2014) | 2 min |
| 9 | ML Clásico (Sahingoz, Vrbančič 2019-2020) | 1.5 min |
| 10 | Deep Learning y Estado del Arte (2022-2025) | 1.5 min |
| 11 | Posicionamiento de Nuestra Propuesta | 1.5 min |

**Temas:** Mohammad 2012 = Feature Engineering · Mohammad 2014 = Primer clasificador en UCI (~97%) · Random Forest 97.32% (Sahingoz) · Ensemble 97.6% (Vrbančič) · Deep RL (Chatterjee) · Transformers SOTA 98%+ · **GAP:** Ningún trabajo previo implementó sistema en tiempo real (API REST)

---

### **SECCIÓN (c): Marco Teórico** — Gabriel & Valeria (6.5 min)
| # | Título | Presentador | Tiempo |
|---|--------|:------------:|:------:|
| 12 | ¿Qué es Phishing? Marco Conceptual | Gabriel | 1.5 min |
| 13 | Dataset UCI y sus Features | Gabriel | 2 min |
| 14 | Redes Neuronales Artificiales (MLP) | Valeria | 2 min |
| 15 | Regularización y Técnicas de Entrenamiento | Valeria | 1.5 min |

**Temas:** Taxonomía del phishing (3 tipos) · Dataset UCI: 11,055 instancias, 30 features en 4 categorías, codificación ternaria · MLP: arquitectura (30→128→64→32→1), ReLU, Sigmoid, Backpropagation · Regularización: Dropout, Batch Normalization, Early Stopping · Métricas: Accuracy, Precision, Recall, F1, AUC-ROC

---

### **RESULTADOS Y CIERRE** — Gabriel (2 min)
| # | Título | Tiempo |
|---|--------|:------:|
| 16 | Resultados Preliminares (Entrega 2) | 1.5 min |
| 17 | Próximos Pasos (Entregas 4-6) | 30 seg |
| 18 | Preguntas | 3 min |

**Contenido:** Random Forest ~97% baseline · Plan: Entrega 4 (IEEE paper), Entrega 5 (MLP + API), Entrega 6 (paper final)

---

## 🎯 Cómo Usar los Archivos

### **Para Presentación en Clase:**

1. **Abre `presentacion.html` en el navegador**
   - No requiere instalación, funciona offline
   - Click derecho → "Presentar" (fullscreen mode en algunos navegadores)
   - O simplemente maximiza la ventana

2. **Navegación:**
   - Botones "Anterior/Siguiente" en la parte inferior
   - Teclas flecha izquierda/derecha
   - Barra espaciadora para avanzar

3. **Proyección:**
   - Conecta el proyector antes de abrir
   - La presentación es responsive y se verá bien en cualquier tamaño

### **Para Preparación de Presentadores:**

1. **Lee `SCRIPT_PRESENTACION.md`**
   - Gabriel: Revisa líneas con "🎤 GABRIEL"
   - Valeria: Revisa líneas con "🎤 VALERIA"

2. **Practica con cronómetro**
   - Asegúrate que tu sección dura exactamente el tiempo asignado
   - Memoriza los puntos clave, no leas palabra por palabra

3. **Prepárate para preguntas**
   - Las respuestas esperadas están en el script (sección "PREPARACIÓN PARA PREGUNTAS")

4. **Checklist pre-presentación**
   - Revisar: ["SCRIPT_PRESENTACION.md"](SCRIPT_PRESENTACION.md#-checklist-pre-presentación)

---

## 📚 Contenido Académico Cubierto

### **(a) Motivación**
✅ Definición clara de phishing (3 tipos de ataque)  
✅ Estadísticas 2024-2025 (APWG: 4.8M ataques, 1.13M en Q2 2025, $2.8B pérdidas)  
✅ Limitaciones de métodos actuales (blacklists, heurísticas manuales)  
✅ Formulación formal del problema: clasificación binaria supervisada  

### **(b) Trabajo Relacionado**
✅ Mohammad et al. (2012): Feature engineering, 17 features → 84% accuracy  
✅ Mohammad et al. (2014): Clasificación con SSNN, 11K URLs, 30 features → **97% accuracy** (nuestro baseline)  
✅ Sahingoz et al. (2019): Random Forest + NLP → 97.32%  
✅ Vrbančič et al. (2020): Ensemble methods → 97.6%  
✅ Chatterjee & Namin (2019): Deep Reinforcement Learning  
✅ Estado del arte (2022-2025): Transformers, CNNs, BiLSTM → 98%+  
✅ **Posicionamiento crítico:** Gap = ausencia de sistemas en tiempo real (API REST)

### **(c) Marco Teórico**
✅ Taxonomía del phishing (URL-based, Content-based, DNS-based)  
✅ Dataset UCI: 4 categorías (Address Bar 12, Abnormal 6, HTML/JS 5, Domain 7), codificación ternaria {-1, 0, 1}  
✅ MLP: Arquitectura, ReLU, Sigmoid, Binary Cross-Entropy  
✅ Regularización: Dropout, Batch Normalization, Early Stopping  
✅ Métricas: Accuracy, Precision, Recall, F1-Score, AUC-ROC, Confusion Matrix  

### **Resultados Preliminares**
✅ Random Forest: 97% accuracy, 99% AUC (baseline)  
✅ SVM (RBF): 95% accuracy, 98% AUC  
✅ Plan: Comparar MLP (2L, 3L, 4L) vs baselines

---

## 🔗 Referencias Académicas

| # | Referencia | Año |
|----|-----------|------|
| [1] | Mohammad et al. - Feature engineering for phishing | 2012 |
| [2] | Mohammad et al. - Predicting phishing with SSNN | 2014 |
| [3] | Sahingoz et al. - Machine learning based phishing detection | 2019 |
| [4] | Vrbančič et al. - Datasets for phishing detection | 2020 |
| [5] | Chatterjee & Namin - Deep Reinforcement Learning | 2019 |
| [6] | LeCun, Bengio & Hinton - Deep Learning | 2015 |
| [7] | Srivastava et al. - Dropout | 2014 |
| [8] | Ioffe & Szegedy - Batch Normalization | 2015 |
| [9] | APWG - Phishing Activity Trends Report Q4 2024 | 2025 |
| [10] | UCI ML Repository - Phishing Websites Dataset #327 | 2014 |

---

## ✅ Checklist de Entrega 3

- ✅ Presentación HTML interactiva (18 diapositivas)
- ✅ Script detallado con tiempos y notas del orador
- ✅ Timeline completo (00:00 - 27:00)
- ✅ Preguntas esperadas con respuestas preparadas
- ✅ Tips de oratoria y manejo de presentación
- ✅ Referencias académicas completas
- ⏳ **Próximas:** Entrega 4 (IEEE paper ~3 páginas, June 3)

---

## 🚀 Próximos Pasos

**Entrega 4 (June 3, 2026):** IEEE paper formateado (~3 páginas)  
**Entrega 5 (July 1, 2026):** Presentación final + demostración de API REST en tiempo real  
**Entrega 6 (July 5, 2026):** Paper final IEEE (6 páginas completo)

---

*Entrega 3 — PF3325 Redes | Gabriel Fallas & Valeria Chinchilla | Mayo 2026*
