def optimize_replay_throughput(batch_size):
    """Maximizes execution throughput by scaling adaptive batch sizes natively."""
    return batch_size * 1.5 if batch_size < 1000 else batch_size
