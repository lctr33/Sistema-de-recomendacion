"""Modelo baseline basado en N-gramas y recomendación secuencial."""
from collections import Counter, defaultdict
from typing import Dict, Iterable, List, Sequence


class NgramSequenceRecommender:
    """Recomendador simple que aprende transiciones entre libros mediante N-gramas."""

    def __init__(self, n: int = 2, max_suggestions: int = 10):
        if n < 2:
            raise ValueError("El valor de n debe ser al menos 2 para capturar secuencias.")
        self.n = n
        self.max_suggestions = max_suggestions
        self.transitions: Dict[tuple, Counter] = defaultdict(Counter)

    def fit(self, user_histories: Sequence[Sequence[str]]) -> None:
        """Aprende transiciones a partir de historiales ordenados de lectura."""
        for history in user_histories:
            if len(history) < self.n:
                continue
            for i in range(len(history) - self.n + 1):
                context = tuple(history[i : i + self.n - 1])
                next_item = history[i + self.n - 1]
                self.transitions[context][next_item] += 1

    def recommend(self, context: Iterable[str]) -> List[str]:
        """Devuelve una lista de recomendaciones ordenadas por frecuencia."""
        context_tuple = tuple(context)[-self.n + 1 :]
        candidates = self.transitions.get(context_tuple)
        if not candidates:
            return []
        most_common = candidates.most_common(self.max_suggestions)
        return [item for item, _ in most_common]
