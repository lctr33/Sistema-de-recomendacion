# Plan de trabajo – Sistema de Recomendación

Este plan distribuye las actividades para cumplir la rúbrica del 2do parcial y obtener la máxima calificación en el Proyecto 4.

## Visión general
- **Corpus**: [Amazon Books Reviews](https://www.kaggle.com/datasets/mohamedbakhet/amazon-books-reviews).
- **Baseline**: enfoque de N-gramas con recomendación secuencial + modelo de clasificación/regresión (p. ej. Random Forest o SVM para predicción de calificaciones).
- **Modelos alternativos**: factorization machines / LightFM, LightGCN o Item2Vec + red neuronal.
- **Métricas**: MAE, RMSE, Precision@K, Recall@K, MAP.
- **Entregables recurrentes**: Notebook, documento formal y presentación para cada etapa.

## Cronograma alineado con la rúbrica

### Semana 1 (hasta jueves 16 de octubre) – Etapa 1: Análisis del problema (40%)
- **Notebook (`notebooks/etapa1`)**
  - 01_analisis_y_preprocesamiento.ipynb: limpieza, exploración, división Train/Dev/Test.
  - 02_representacion_baseline.ipynb: construcción de N-gramas y validación de representaciones.
  - 03_modelo_baseline.ipynb: entrenamiento y evaluación del baseline.
- **Documento (`docs/documentos/etapa1_baseline.md`)**
  - Resumen de decisiones de preprocesamiento.
  - Descripción técnica de representaciones.
  - Resultados y discusión del baseline.
- **Presentación (`docs/presentaciones/etapa1_baseline.pptx`)**
  - Slides con hallazgos clave y métricas.
- **Checklist**
  - Completar sección Etapa 1 en `docs/checklist_rubrica.md`.

### Semana 2 (hasta martes 28 de octubre) – Etapa 2: Resolución (1ª aproximación) (30%)
- **Notebook (`notebooks/etapa2`)**
  - 01_modelo_alternativo_v1.ipynb: implementación de un modelo distinto al baseline.
  - 02_evaluacion_v1.ipynb: comparación con baseline y análisis de errores.
- **Documento (`docs/documentos/etapa2_modelo_alternativo.md`)**
  - Detalle de mejoras, resultados y limitaciones.
- **Presentación (`docs/presentaciones/etapa2_modelo_alternativo.pptx`)**
  - Estrategia y métricas comparativas.

### Semana 3 (hasta martes 4 de noviembre) – Etapa 3: Resolución (2ª aproximación) (30%)
- **Notebook (`notebooks/etapa3`)**
  - 01_modelo_alternativo_mejorado.ipynb: incorporar mejoras basadas en el análisis previo.
  - 02_evaluacion_final.ipynb: resultados finales con comparación completa.
- **Documento (`docs/documentos/etapa3_mejoras.md`)**
  - Detalle de ajustes, resultados y discusión final.
- **Presentación (`docs/presentaciones/etapa3_final.pptx`)**
  - Historia completa del proyecto, incremento de métricas y próximos pasos.

## Roles sugeridos
- **Líder de datos**: prepara corpus y split.
- **Ingeniero de características**: implementa representaciones y validaciones.
- **Modelador**: entrena baseline y modelos alternativos.
- **Analista de métricas**: evalúa resultados, genera visualizaciones.
- **Coordinador de documentación**: mantiene notebooks, documentos y presentaciones.

## Infraestructura y herramientas
- Python 3.10+ con librerías: `pandas`, `numpy`, `scikit-learn`, `implicit`/`lightfm`, `lightgbm`, `networkx`, `matplotlib`, `seaborn`.
- Gestión de experimentos opcional con `MLflow` o `Weights & Biases` (documentar en `docs/documentos/infraestructura.md` si se usa).
- Control de versiones con Git y convenciones de ramas feature/etapa.

## Gestión de riesgos
- **Tamaño del corpus**: preparar scripts de muestreo en `src/data` si el hardware es limitado.
- **Desbalance de interacciones**: considerar técnicas de regularización y filtrado en `src/features`.
- **Tiempo de cómputo**: calendarizar sesiones de entrenamiento y paralelizar cuando sea posible.
- **Documentación**: actualizar `docs/checklist_rubrica.md` después de cada sesión de trabajo.

## Métricas de éxito
- Cumplimiento del 100% de la rúbrica.
- Recomendador con mejoras significativas frente al baseline (>10% en Precision@K o reducción de error).
- Documentación reproducible y presentaciones listas en cada fecha de entrega.
