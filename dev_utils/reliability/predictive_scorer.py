def score_topology_integrity(nodes):
    """Calculates predictive health scores for federation shards."""
    base_score = 100.0
    for node in nodes:
        if node.get('latency_ms', 0) > 40:
            base_score -= 2.5
    return max(0.0, base_score)
