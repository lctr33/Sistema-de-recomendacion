"""Rutinas de exploración y limpieza para el corpus de reseñas."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable, Literal

import pandas as pd


@dataclass
class RatingsSummary:
    n_users: int
    n_items: int
    n_interactions: int
    interactions_per_user: float
    interactions_per_item: float


def basic_ratings_summary(df: pd.DataFrame, user_col: str, item_col: str) -> RatingsSummary:
    """Devuelve métricas rápidas del dataset de ratings."""
    n_interactions = len(df)
    user_counts = df[user_col].value_counts()
    item_counts = df[item_col].value_counts()
    return RatingsSummary(
        n_users=user_counts.shape[0],
        n_items=item_counts.shape[0],
        n_interactions=n_interactions,
        interactions_per_user=float(user_counts.mean()),
        interactions_per_item=float(item_counts.mean()),
    )


def drop_sparse_entities(
    df: pd.DataFrame,
    *,
    user_col: str,
    item_col: str,
    min_user_interactions: int = 2,
    min_item_interactions: int = 2,
) -> pd.DataFrame:
    """Filtra usuarios/libros con pocas interacciones."""
    filtered = df.copy()
    if min_user_interactions > 1:
        user_mask = filtered[user_col].map(filtered[user_col].value_counts()) >= min_user_interactions
        filtered = filtered[user_mask]
    if min_item_interactions > 1:
        item_mask = filtered[item_col].map(filtered[item_col].value_counts()) >= min_item_interactions
        filtered = filtered[item_mask]
    return filtered


def normalize_ratings(df: pd.DataFrame, rating_col: str, *, min_rating: float = 1.0, max_rating: float = 5.0) -> pd.Series:
    """Normaliza calificaciones al rango [0, 1]."""
    scaled = (df[rating_col] - min_rating) / (max_rating - min_rating)
    return scaled.clip(0.0, 1.0)


def deduplicate_reviews(
    df: pd.DataFrame,
    subset: Iterable[str],
    *,
    timestamp_col: str | None = None,
    keep: Literal["first", "last", False] = "last",
) -> pd.DataFrame:
    """Elimina duplicados conservando la última reseña por combinación de columnas."""

    if timestamp_col is not None and timestamp_col not in df.columns:
        raise KeyError(f"La columna temporal `{timestamp_col}` no está en el DataFrame.")

    ordered = df.sort_values(timestamp_col) if timestamp_col else df
    return ordered.drop_duplicates(subset=subset, keep=keep)
