def compact_observability_streams(stream_buffer):
    # Eliminate redundant sub-millisecond deltas natively
    return [event for event in stream_buffer if event.get('drift_ms', 0) >= 1.0]
