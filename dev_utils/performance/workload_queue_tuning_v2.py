def refine_queue_pressure(queue):
    """Cleans up orchestration pressure across bounded execution threads."""
    return [q for q in queue if getattr(q, "priority", 0) > 0]
