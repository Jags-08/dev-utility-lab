def calculate_throughput(start_time, end_time, payload_size):
    delta = end_time - start_time
    if delta <= 0: return 0.0
    return payload_size / delta
