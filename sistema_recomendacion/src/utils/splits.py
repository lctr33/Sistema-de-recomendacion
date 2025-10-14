"""Funciones para dividir datos en conjuntos Train/Dev/Test."""
from typing import Tuple

import numpy as np
import pandas as pd


def temporal_train_dev_test_split(
    df: pd.DataFrame,
    timestamp_col: str,
    dev_size: float = 0.1,
    test_size: float = 0.1,
    random_state: int | None = 42,
    shuffle_dev: bool = False,
) -> Tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    """Divide respetando el orden temporal.

    Parameters
    ----------
    df:
        DataFrame con reseñas.
    timestamp_col:
        Columna con la marca de tiempo (será usada para ordenar antes de dividir).
    dev_size:
        Proporción destinada al conjunto de validación.
    test_size:
        Proporción destinada al conjunto de prueba.
    random_state:
        Semilla para reproducibilidad.
    """
    if timestamp_col not in df.columns:
        raise KeyError(f"La columna temporal `{timestamp_col}` no está en el DataFrame.")

    df_sorted = df.sort_values(timestamp_col).reset_index(drop=True)
    n_total = len(df_sorted)
    if n_total == 0:
        return df_sorted.copy(), df_sorted.copy(), df_sorted.copy()

    test_count = int(round(n_total * test_size))
    test_count = min(max(test_count, 0), n_total)

    train_dev = df_sorted.iloc[: n_total - test_count]
    test = df_sorted.iloc[n_total - test_count :] if test_count else df_sorted.iloc[0:0]

    if len(train_dev) == 0:
        return train_dev.copy(), train_dev.copy(), test.copy()

    dev_fraction = dev_size / max(1 - test_size, 1e-8)
    dev_count = int(round(len(train_dev) * dev_fraction))
    dev_count = min(max(dev_count, 0), len(train_dev))

    if shuffle_dev:
        indices = np.arange(len(train_dev))
        rng = np.random.default_rng(seed=random_state)
        rng.shuffle(indices)
        dev_indices = np.sort(indices[:dev_count])
        dev = train_dev.iloc[dev_indices]
        train = train_dev.drop(train_dev.index[dev_indices])
    else:
        dev = train_dev.iloc[len(train_dev) - dev_count :] if dev_count else train_dev.iloc[0:0]
        train = train_dev.iloc[: len(train_dev) - dev_count]

    return train, dev, test
