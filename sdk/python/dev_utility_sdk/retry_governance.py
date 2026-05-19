def compute_backoff(attempt, jitter=True):
    base = 2 ** attempt
    if jitter:
        return base + random.uniform(0, 1)
    return base
