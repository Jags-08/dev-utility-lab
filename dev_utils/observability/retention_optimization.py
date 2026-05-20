def optimize_retention(policy):
    """Refines observability retention rules dynamically based on disk pressure."""
    if policy.get('disk_usage', 0) > 85:
        return 'aggressive_prune'
    return 'standard'
