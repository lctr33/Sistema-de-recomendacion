# Etapa 1 – Análisis y preprocesamiento

## Resumen ejecutivo
- **Objetivo**: preparar el corpus de reseñas de Amazon Books para entrenar el baseline del sistema de recomendación.
- **Resultados clave**: limpieza de 3 millones de interacciones a 2.3 millones tras filtrar usuarios/libros con <3 reseñas; normalización de calificaciones; datasets procesados guardados en `data/processed/`.

## Decisiones de limpieza
1. **Carga de datos**: se usaron `load_books_ratings` y `load_books_metadata` para asegurar rutas reproducibles.
2. **Normalización de columnas**: renombrado a snake_case (`review/score` → `rating`) y creación de `book_title_key` para unir con metadatos.
3. **Imputaciones**:
   - `description`, `authors`, `publisher`, `categories` rellenadas con marcadores (`sin_descripcion`, `autor_desconocido`, etc.).
   - `review_summary` y `review_text` completados con cadenas vacías o "sin_resumen".
   - `ratings_count` reemplazado por 0 cuando faltaba.
4. **Conversión de tipos**: `review_time` a `datetime`; `rating` y `price` a numérico (con soporte para `NaN`).
5. **Deduplicación**: se conservó la reseña más reciente por combinación (`user_id`, `book_id`).
6. **Filtrado de sparsidad**: se eliminaron usuarios y libros con menos de 3 interacciones para estabilizar el baseline secuencial.
7. **Normalización de rating**: escala lineal a [0, 1] (`rating_normalized`).
8. **Columnas descartadas**: `image`, `previewLink`, `infoLink`, `price`, `profile_name`, `helpfulness` por alta ausencia o irrelevancia.

## Exploración descriptiva
- **Usuarios únicos**: 1,008,972 → 756,214 tras filtrado.
- **Libros únicos**: 221,998 → 158,430 tras filtrado.
- **Interacciones**: 3,000,000 → 2,312,587 tras limpieza.
- **Interacciones promedio**:
  - Por usuario: 2.41 → 3.06.
  - Por libro: 13.51 → 14.60.
- **Distribución temporal**: reseñas entre 1995 y 2013 (ver notebook para gráfico).

## Artefactos generados
- `data/processed/books_metadata_clean.csv`
- `data/processed/books_ratings_clean.csv`
- `data/processed/ratings_train.csv`
- `data/processed/ratings_dev.csv`
- `data/processed/ratings_test.csv`

## Próximos pasos
- Construir representaciones TF-IDF/N-gramas (`02_representacion_baseline.ipynb`).
- Entrenar baseline N-gramas secuencial y registrar métricas (notebook 03).
- Actualizar presentaciones con visualizaciones clave.
