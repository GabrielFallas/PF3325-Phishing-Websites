# 🎬 ENTREGA 2 - RESUMEN COMPLETADO

## ✅ QUÉ SE HIZO

Esta es la Entrega 2 del proyecto de Detección de Phishing. Se entrega un **video de demostración de 8-12 minutos** con:

1. ✅ **Dataset Overview** - Explicación de los 11,055 datos con 30 características
2. ✅ **Classifier Design** - Arquitectura de Random Forest y SVM
3. ✅ **Sample Predictions** - Predicciones en muestras reales
4. ✅ **Results** - Métricas: 97.17% accuracy, 98.05% recall

---

## 🚀 CÓMO EJECUTAR

### Paso 1: Entrenar modelos (una sola vez)

```bash
cd /Users/vchinchilla/Documents/UCR/Redes/PF3325-Phishing-Websites
source .venv/bin/activate
python src/train_sklearn.py
```

**Tiempo:** ~2-3 minutos
**Output:** 2 modelos entrenados + métricas de evaluación

### Paso 2: Generar demostración

```bash
python src/demo.py
```

**Tiempo:** ~1 minuto
**Output:** Todo lo necesario para la presentación de 12 minutos

### Paso 3: Grabar video (tu responsabilidad)

- Sigue el guión en `presentations/ENTREGA2_SCRIPT.md`
- Graba pantalla de la demo + narración de Gabriel y Valeria
- Duración: 8-12 minutos

---

## 📁 ESTRUCTURA DE ARCHIVOS CREADOS

### Código Python (src/)

```
✅ preprocess.py         → Cargar y preparar datos
✅ train_sklearn.py      → Entrenar Random Forest + SVM
✅ demo.py               → Demostración interactiva
✅ model.py              → Arquitectura de redes neuronales (futuro)
✅ train.py              → Entrenamiento de NN (futuro)
✅ evaluate.py           → Utilidades de evaluación
```

### Modelos Entrenados (models/)

```
✅ random_forest_model.pkl      → Random Forest (97.17% accuracy)
✅ svm_model.pkl                → SVM (94.64% accuracy)
✅ scaler.joblib                → Normalizador de features
✅ feature_names.joblib         → Nombres de 30 features
```

### Visualizaciones (reports/)

```
✅ confusion_matrix.png         → Matriz de confusión
✅ roc_curve.png               → Curva ROC (AUC=0.9959)
```

### Documentación de Presentación (presentations/)

```
✅ ENTREGA2_SCRIPT.md           → Guión detallado para 2 personas
✅ ENTREGA2_EJECUCION.md        → Instrucciones paso a paso
✅ Este archivo (README)
```

---

## 📊 RESULTADOS OBTENIDOS

### Dataset

| Métrica        | Valor         |
| -------------- | ------------- |
| Total muestras | 11,055        |
| Features       | 30            |
| Phishing       | 4,898 (44.3%) |
| Legítimo       | 6,157 (55.7%) |

### Random Forest (Mejor modelo)

| Métrica   | Valor  |
| --------- | ------ |
| Accuracy  | 97.17% |
| Precision | 96.90% |
| Recall    | 98.05% |
| F1-Score  | 97.47% |
| AUC-ROC   | 0.9959 |

### SVM

| Métrica   | Valor  |
| --------- | ------ |
| Accuracy  | 94.64% |
| Precision | 93.53% |
| Recall    | 97.08% |
| F1-Score  | 95.27% |
| AUC-ROC   | 0.9874 |

---

## 🎯 RESPONDE TODAS LAS PREGUNTAS DEL ENUNCIADO

### ❓ 1) ¿Cuáles son sus datos?

✅ **Respondido en:** `demo.py` → sección "DATASET OVERVIEW"

- UCI Phishing Websites (11,055 muestras)
- 30 características (Address Bar, Abnormal, HTML/JS, Domain)
- Codificación: -1 (phishing), 0 (sospechoso), 1 (legítimo)

### ❓ 2) ¿Qué aspectos de diseño y funcionalidad del clasificador?

✅ **Respondido en:** `demo.py` → sección "CLASSIFIER DESIGN"

- Random Forest: 100 árboles
- SVM: kernel RBF
- Preprocesamiento: normalización + split 70/15/15
- Métricas: Accuracy, Precision, Recall, F1, AUC-ROC

### ❓ 3) ¿Cuáles son las posibles salidas del clasificador?

✅ **Respondido en:** `demo.py` → secciones "SAMPLE PREDICTIONS" + "MODEL EVALUATION"

- Predicción binaria: Phishing (0) o Legítimo (1)
- Probabilidad: 0.0 - 1.0
- Matriz de confusión: TP, TN, FP, FN

---

## 🎬 GUIÓN DE PRESENTACIÓN (12 MINUTOS)

| Persona | Tiempo      | Tema               | Duración |
| ------- | ----------- | ------------------ | -------- |
| Gabriel | 0:00-0:30   | Introducción       | 30s      |
| Gabriel | 0:30-2:30   | Dataset Overview   | 2 min    |
| Valeria | 2:30-4:00   | Preprocesamiento   | 1.5 min  |
| Valeria | 4:00-5:30   | Classifier Design  | 1.5 min  |
| Gabriel | 5:30-7:00   | Sample Predictions | 1.5 min  |
| Valeria | 7:00-9:30   | Model Evaluation   | 2.5 min  |
| Valeria | 9:30-11:00  | Visualizaciones    | 1.5 min  |
| Gabriel | 11:00-12:00 | Conclusiones       | 1 min    |

**Total: 12 minutos**

---

## 💾 CÓMO GRABAR EL VIDEO

### Método 1: QuickTime + Zoom (Recomendado)

1. Abre Zoom
2. Comparte pantalla
3. Ejecuta `python src/demo.py`
4. Graba mientras Gabriel y Valeria narran el guión
5. Exporta como MP4

### Método 2: QuickTime Screen Recording

1. `Cmd + Shift + 5` → "Grabar pantalla"
2. Ejecuta `python src/demo.py`
3. Edita después con iMovie/DaVinci Resolve

### Método 3: OBS Studio

1. Descarga OBS (gratis)
2. Configura: Pantalla + Micrófono
3. Presiona "Start Recording"
4. Ejecuta `python src/demo.py`
5. Exporta como MP4

---

## ⚙️ VERIFICACIÓN FINAL

```bash
# ✅ Todos estos comandos deben ejecutarse sin errores

# Activar ambiente
source .venv/bin/activate

# Entrenar modelos
python src/train_sklearn.py
# Esperado: "✓ TRAINING COMPLETE" + métricas

# Ejecutar demo
python src/demo.py
# Esperado: "✓ DEMONSTRATION COMPLETE" + visualizaciones generadas

# Verificar gráficas
ls -lh reports/*.png
# Esperado: 2 archivos PNG
```

---

## 📝 ARCHIVOS DE REFERENCIA

Para más información:

- **Plan del proyecto:** [docs/PLAN_PROYECTO.md](../docs/PLAN_PROYECTO.md)
- **Info del dataset:** [data/README.md](../data/README.md)
- **Info del código:** [src/README.md](../src/README.md)
- **Guión completo:** [presentations/ENTREGA2_SCRIPT.md](ENTREGA2_SCRIPT.md)
- **Instrucciones de ejecución:** [presentations/ENTREGA2_EJECUCION.md](ENTREGA2_EJECUCION.md)

---

## 🎓 CONCLUSIÓN

La Entrega 2 está **100% lista para grabar**. Solo necesitas:

1. ✅ Ejecutar `python src/train_sklearn.py` (ya está hecho)
2. ✅ Ejecutar `python src/demo.py` (para ver el output)
3. ⬜ Grabar video siguiendo `ENTREGA2_SCRIPT.md`
4. ⬜ Entregar MP4 con narración de Gabriel y Valeria

**Tiempo de preparación:** <30 minutos
**Tiempo de grabación:** ~20 minutos
**Tiempo de edición:** Variable (10-30 minutos)

¡Éxito con la presentación! 🎬✨
