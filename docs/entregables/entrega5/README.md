# Entrega 5 — Presentación Final

> **Curso:** PF3325 – Redes
> **Autores:** Gabriel Fallas & Valeria Chinchilla
> **Fecha:** Miércoles 1 de julio de 2026
> **Duración:** 10–12 minutos

## Contenido

| Archivo | Descripción |
|---------|-------------|
| `presentacion.html` | Presentación interactiva (13 slides, navegable con teclado) |
| `SCRIPT_PRESENTACION.md` | Guion del presentador con tiempos y notas de la demo |
| `figures/` | Figuras usadas en las slides |

## Cómo usar

1. Abrir `presentacion.html` en cualquier navegador → `F11` para pantalla completa.
2. Navegar con `→ / ←`, barra espaciadora, `Home` / `End`.
3. Dejar la API corriendo en otra pestaña para la **demo en vivo**:
   ```bash
   uvicorn src.api_phishing:app --reload
   # abrir http://localhost:8000
   ```

## Estructura de la charla (según el enunciado)

| Bloque | Slides | Tiempo |
|--------|--------|--------|
| a. Motivación / Problema / Trabajo relacionado | 2–3 | ~2.5 min |
| b. Implementación (datos, modelo, tiempo real, API + demo) | 4–8 | ~5 min |
| c. Resultados y análisis | 9–11 | ~2.5 min |
| Discusión + conclusión | 12–13 | ~2 min |

## Resultados destacados (test set)

- MLP: **96.5% accuracy · 98.8% recall · 0.994 AUC** (recall más alto de los 3 modelos)
- Servicio de detección en tiempo real funcional (extractor + FastAPI + demo web)

---
*Entrega 5 – PF3325 Redes | Gabriel Fallas & Valeria Chinchilla | Julio 2026*
