# 🎬 ENTREGA 2 - GUÍA DE USO Y EJECUCIÓN

## Quick Start

### 1. Instalar dependencias (una sola vez)

```bash
cd /Users/vchinchilla/Documents/UCR/Redes/PF3325-Phishing-Websites

# Activar virtual environment
source .venv/bin/activate

# Instalar paquetes
pip install -q ucimlrepo pandas numpy scikit-learn scipy matplotlib seaborn joblib
```

### 2. Entrenar los modelos

```bash
# Entrenar Random Forest y SVM (una sola vez)
python src/train_sklearn.py
```

Este comando:

- ✅ Carga el dataset UCI Phishing Websites (11,055 muestras)
- ✅ Preprocesa: normalización, splitting 70/15/15
- ✅ Entrena Random Forest y SVM
- ✅ Guarda modelos en `models/`
- ✅ Muestra métricas de validación y test

**Tiempo esperado:** ~2-3 minutos

### 3. Ejecutar demostración (para grabar video)

```bash
python src/demo.py
```

Este comando genera:

- ✅ Output detallado para cada pregunta del enunciado
- ✅ 10 predicciones de muestra
- ✅ Métricas de evaluación completas
- ✅ Visualizaciones PNG en `reports/`

**Tiempo esperado:** ~1 minuto

---

## 📊 ARCHIVOS GENERADOS

### Modelos Entrenados

```
models/
├── random_forest_model.pkl      # Modelo Random Forest
├── svm_model.pkl                # Modelo SVM
├── scaler.joblib                # StandardScaler para normalizar
└── feature_names.joblib         # Nombres de las 30 features
```

### Visualizaciones

```
reports/
├── confusion_matrix.png         # Matriz de confusión (Phishing vs Legítimo)
└── roc_curve.png               # Curva ROC con AUC
```

---

## 🎯 RESPONDER LAS PREGUNTAS DEL ENUNCIADO

La presentación debe explicar:

### ❓ 1) ¿Cuáles son sus datos?

**Datos:**

- Dataset UCI Phishing Websites (ID: 327)
- 11,055 muestras
- 30 características (Address Bar, Abnormal, HTML/JS, Domain)
- Codificación ternaria: -1, 0, 1
- Balance: 44.3% phishing, 55.7% legítimo

**Ver en demo.py:**

```
sección "DATASET OVERVIEW" (primeros 2-3 minutos)
```

---

### ❓ 2) ¿Qué aspectos de diseño y funcionalidad del clasificador?

**Diseño:**

- Dos clasificadores: Random Forest (100 árboles) + SVM (kernel RBF)
- Pipeline de preprocesamiento: normalización StandardScaler
- Split: 70% train / 15% val / 15% test
- Métricas: Accuracy, Precision, Recall, F1, AUC-ROC

**Ver en demo.py:**

```
sección "CLASSIFIER DESIGN" (3-4 minutos)
```

---

### ❓ 3) ¿Cuáles son las posibles salidas del clasificador?

**Salidas:**

- **Predicción binaria:** Phishing (0) o Legítimo (1)
- **Probabilidad:** Valor entre 0 y 1 (confianza)
- **Métricas:** Accuracy, Precision, Recall, AUC-ROC
- **Matriz de confusión:** TP, TN, FP, FN

**Ver en demo.py:**

```
sección "SAMPLE PREDICTIONS" (2-3 minutos)
sección "MODEL EVALUATION" (2-3 minutos)
```

---

## 🎬 GRABAR EL VIDEO

### Paso 1: Preparar la pantalla

```bash
# En terminal 1
cd /Users/vchinchilla/Documents/UCR/Redes/PF3325-Phishing-Websites
source .venv/bin/activate

# Tener listo: python src/demo.py
# NO EJECUTES AÚN
```

### Paso 2: Abrir grabar de pantalla

**En macOS:**

- Presiona: `Cmd + Shift + 5`
- Selecciona "Grabar la pantalla seleccionada"
- Haz clic en la terminal

### Paso 3: Grabar demostración (12 minutos)

```bash
# Terminal lista - ¡AHORA PRESIONA GRABAR!
python src/demo.py

# [El script genera todo el output para los 12 minutos]
# Sigue el GUIÓN ENTREGA2_SCRIPT.md
```

### Paso 4: Insertar narración

Necesitarás:

1. **Grabar demostración de pantalla** (output + gráficas)
2. **Grabar audio** (guión de Gabriel y Valeria)
3. **Mezclar audio + video** (en editora como DaVinci Resolve, Adobe Premiere, iMovie)

**O más simple:**

- Abre Zoom
- Comparte pantalla + ejecuta demo.py
- Graba con narración en vivo

---

## 📋 CHECKLIST FINAL

```
Código:
  ☐ src/preprocess.py          ✅ Cargar datos
  ☐ src/train_sklearn.py        ✅ Entrenar modelos
  ☐ src/demo.py                 ✅ Demo interactiva

Datos:
  ☐ data/Training_Dataset.arff  ✅ Dataset UCI
  ☐ models/*.pkl                ✅ Modelos guardados
  ☐ reports/*.png               ✅ Gráficas generadas

Documentación:
  ☐ presentations/ENTREGA2_SCRIPT.md     ✅ Guión 2 personas
  ☐ presentations/ENTREGA2_EJECUCION.md  ✅ Este archivo

Video:
  ☐ Grabado                     ⬜ ~12 minutos
  ☐ Narración por Gabriel       ⬜ Datos + predicciones
  ☐ Narración por Valeria       ⬜ Diseño + resultados
  ☐ Editado (si aplica)         ⬜ Calidad de audio/video
```

---

## ⚙️ RESOLUCIÓN DE PROBLEMAS

### Error: "ModuleNotFoundError: No module named 'X'"

```bash
# Reinstala dependencias
pip install -q ucimlrepo pandas numpy scikit-learn scipy matplotlib seaborn joblib
```

### Error: "Models not found"

```bash
# Ejecuta entrenamiento primero
python src/train_sklearn.py
```

### Output muy largo

```bash
# Guarda a archivo para revisar después
python src/demo.py > demo_output.txt

# Luego abre y revisa
cat demo_output.txt
```

### Gráficas no se guardan

```bash
# Verifica que reports/ existe
mkdir -p reports
python src/demo.py
```

---

## 📹 RECOMENDACIONES PARA VIDEO

✅ **Do's:**

- Mantén la terminal limpia y bien visible
- Habla claro y no muy rápido
- Muestra las gráficas PNG generadas
- Sigue el guión pero sé natural
- Practica el timing antes

❌ **Don'ts:**

- No scrollees demasiado rápido el output
- No hables en background ruido
- No obvies la conclusión
- No excedas 12 minutos
- No graves en mala resolución

---

## 📞 CONTACTO & NOTAS

**Equipo:** Gabriel Fallas & Valeria Chinchilla  
**Curso:** PF3325 - Redes  
**Dataset:** UCI Phishing Websites (ID: 327)  
**Fecha:** Mayo 2026

Para más información, ver:

- [docs/PLAN_PROYECTO.md](../docs/PLAN_PROYECTO.md)
- [data/README.md](../data/README.md)
- [src/README.md](../src/README.md)
