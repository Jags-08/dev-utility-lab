def score_recovery_confidence(shard_history):
    """Calculates statistical confidence in replay recovery sequences."""
    successes = sum(1 for status in shard_history if status == 'recovered')
    return (successes / len(shard_history)) if shard_history else 0.0
