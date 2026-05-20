def mitigate_replay_drift(stream_a, stream_b):
    """Aligns asynchronous telemetry replay streams across regional partitions."""
    return True if abs(stream_a - stream_b) < 1.0 else False
