"""Funciones de carga del corpus de Amazon Books Reviews."""
from pathlib import Path
from typing import Optional

import pandas as pd


def load_raw_reviews(path: Path, *, nrows: Optional[int] = None) -> pd.DataFrame:
    """Carga el dataset crudo desde `path`.

    Parameters
    ----------
    path:
        Ruta al archivo CSV original descargado de Kaggle.
    nrows:
        Número máximo de filas a cargar (útil para muestreos rápidos).

    Returns
    -------
    pd.DataFrame
        DataFrame con las reseñas crudas.
    """
    if not path.exists():
        raise FileNotFoundError(f"No se encuentra el archivo de reseñas en {path}")
    return pd.read_csv(path, nrows=nrows)


def load_books_metadata(path: Path, *, nrows: Optional[int] = None) -> pd.DataFrame:
    """Carga el archivo `books_data.csv` con información de los libros.

    Este dataset suele incluir columnas como identificador del libro, título,
    autoría, categorías y metadatos de publicación. Mantenerlo separado ayuda a
    combinarlo con las interacciones de usuarios cuando se requiera.
    """

    if not path.exists():
        raise FileNotFoundError(f"No se encuentra el archivo de metadatos en {path}")
    return pd.read_csv(path, nrows=nrows)


def load_books_ratings(path: Path, *, nrows: Optional[int] = None) -> pd.DataFrame:
    """Carga el archivo `Books_rating.csv` con interacciones usuario-libro.

    Las columnas típicas incluyen identificador de usuario, identificador de
    libro, calificación y fecha. Ajusta los parámetros de `pd.read_csv` aquí si
    necesitas forzar tipos (por ejemplo, `dtype={"reviewerID": str}`).
    """

    if not path.exists():
        raise FileNotFoundError(f"No se encuentra el archivo de ratings en {path}")
    return pd.read_csv(path, nrows=nrows)
