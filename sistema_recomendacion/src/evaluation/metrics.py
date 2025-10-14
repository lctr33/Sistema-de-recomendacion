"""Implementaciones de métricas MAE, RMSE, Precision@K, Recall@K y MAP."""
from typing import Iterable, Sequence
import numpy as np


def mae(y_true: Iterable[float], y_pred: Iterable[float]) -> float:
    true = np.asarray(list(y_true), dtype=float)
    pred = np.asarray(list(y_pred), dtype=float)
    if true.shape != pred.shape:
        raise ValueError("`y_true` y `y_pred` deben tener la misma forma.")
    return float(np.mean(np.abs(true - pred)))


def rmse(y_true: Iterable[float], y_pred: Iterable[float]) -> float:
    true = np.asarray(list(y_true), dtype=float)
    pred = np.asarray(list(y_pred), dtype=float)
    if true.shape != pred.shape:
        raise ValueError("`y_true` y `y_pred` deben tener la misma forma.")
    return float(np.sqrt(np.mean(np.square(true - pred))))


def precision_at_k(recommended: Sequence[Sequence[str]], relevant: Sequence[Sequence[str]], k: int) -> float:
    if len(recommended) != len(relevant):
        raise ValueError("El número de usuarios debe coincidir en recommended y relevant.")
    scores = []
    for recs, rels in zip(recommended, relevant):
        top_k = set(recs[:k])
        rel_set = set(rels)
        if not top_k:
            scores.append(0.0)
            continue
        scores.append(len(top_k & rel_set) / min(k, len(top_k)))
    return float(np.mean(scores))


def recall_at_k(recommended: Sequence[Sequence[str]], relevant: Sequence[Sequence[str]], k: int) -> float:
    if len(recommended) != len(relevant):
        raise ValueError("El número de usuarios debe coincidir en recommended y relevant.")
    scores = []
    for recs, rels in zip(recommended, relevant):
        rel_set = set(rels)
        if not rel_set:
            scores.append(0.0)
            continue
        top_k = set(recs[:k])
        scores.append(len(top_k & rel_set) / len(rel_set))
    return float(np.mean(scores))


def mean_average_precision(recommended: Sequence[Sequence[str]], relevant: Sequence[Sequence[str]], k: int) -> float:
    if len(recommended) != len(relevant):
        raise ValueError("El número de usuarios debe coincidir en recommended y relevant.")
    average_precisions = []
    for recs, rels in zip(recommended, relevant):
        rel_set = set(rels)
        if not rel_set:
            average_precisions.append(0.0)
            continue
        hits = 0
        precision_sum = 0.0
        for idx, item in enumerate(recs[:k], start=1):
            if item in rel_set:
                hits += 1
                precision_sum += hits / idx
        if hits == 0:
            average_precisions.append(0.0)
        else:
            average_precisions.append(precision_sum / min(len(rel_set), k))
    return float(np.mean(average_precisions))
