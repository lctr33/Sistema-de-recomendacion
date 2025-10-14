"""Construcción de representaciones basadas en N-gramas y TF-IDF."""
from typing import Iterable, Tuple

from sklearn.feature_extraction.text import TfidfVectorizer
from scipy.sparse import csr_matrix
import numpy as np


def build_tfidf_matrix(
    texts: Iterable[str],
    *,
    ngram_range: Tuple[int, int] = (1, 2),
    min_df: int | float = 5,
    max_df: int | float = 0.5,
    max_features: int | None = 200_000,
    dtype: type = np.float32,
) -> Tuple[TfidfVectorizer, csr_matrix]:
    """Entrena un vectorizador TF-IDF y devuelve la matriz de características.

    Parameters
    ----------
    texts:
        Iterable de textos (p. ej. reseñas o historiales de lectura concatenados).
    ngram_range:
        Rango de N-gramas a utilizar. `(1, 2)` se traduce en unigramas + bigramas.
    min_df:
        Frecuencia mínima absoluta o relativa para incluir un término en el vocabulario.
    max_df:
        Frecuencia máxima absoluta o relativa para mantener un término (filtra stopwords).
    max_features:
        Número máximo de términos a retener. Usa ``None`` para no limitar.
    dtype:
        Tipo de dato numérico a utilizar en la matriz esparsa (por defecto `float32` para ahorrar memoria).

    Returns
    -------
    vectorizer, matrix
        El vectorizador entrenado y la matriz esparsa resultante.
    """
    vectorizer = TfidfVectorizer(
        ngram_range=ngram_range,
        stop_words="english",
        min_df=min_df,
        max_df=max_df,
        max_features=max_features,
        dtype=dtype,
    )
    matrix = vectorizer.fit_transform(texts)
    return vectorizer, matrix
