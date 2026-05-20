def optimize_routing_queue(queue):
    # Sort natively by highest QoS tag overhead
    return sorted(queue, key=lambda q: q.get('qos', 0), reverse=True)
