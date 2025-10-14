# Proyecto: Sistema de Recomendación de Libros

Este repositorio organiza el trabajo del **Proyecto 4 - Sistemas de Recomendación** del segundo parcial de Minería de Texto. El objetivo es construir un recomendador de libros basado en las reseñas de Amazon Books, cumpliendo al 100% con la rúbrica de evaluación.

## Objetivos generales
- Desarrollar un pipeline reproducible para preprocesar, representar y modelar el corpus de reseñas.
- Comparar un baseline de N-gramas contra al menos una técnica avanzada (factorización matricial, GNN, etc.).
- Evaluar exhaustivamente con métricas de ranking y error (MAE, RMSE, Precision@K, Recall@K, MAP).
- Documentar cada etapa (notebook, documento y presentación) para asegurar la máxima calificación.

## Estructura
- `data/`: datos crudos y procesados.
- `docs/`: documentación formal y presentaciones para cada entrega.
- `notebooks/`: notebooks organizados por etapas de la rúbrica.
- `reports/`: visualizaciones y reportes generados.
- `src/`: código fuente modular (preprocesamiento, modelos, evaluación, utilidades).

## Próximos pasos
1. Completar el plan granular en `docs/plan_de_trabajo.md`.
2. Recolectar y limpiar el corpus en `notebooks/etapa1/01_analisis_y_preprocesamiento.ipynb`.
3. Entrenar el baseline y documentarlo (`notebooks/etapa1`, `docs/documentos/etapa1_baseline.md`).
4. Implementar y evaluar alternativas (`notebooks/etapa2`, `notebooks/etapa3`).
5. Mantener el checklist de la rúbrica actualizado (`docs/checklist_rubrica.md`).

## Control de versiones recomendado
- Mantener notebooks limpios (sin salidas pesadas) y versionar experimentos claves.
- Registrar dependencias en `requirements.txt` (se añadirá cuando se definan los entornos).

## Contacto
Para dudas o coordinación del equipo, documentar acuerdos en `docs/documentos/acuerdos.md`.
