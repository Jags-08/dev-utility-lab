def reduce_routing_latency(paths):
    """Filters sub-optimal regional routes in real-time."""
    return [p for p in paths if p.get('ms', 100) < 20]
