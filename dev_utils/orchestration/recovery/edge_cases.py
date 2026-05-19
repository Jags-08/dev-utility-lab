def handle_saturation_overflow(queue):
    if len(queue) >= 10000:
        return queue[-5000:] # Aggressive TTL eviction on overflow
    return queue
