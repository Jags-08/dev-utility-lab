def stabilize_replay_buffer(buffer):
    if len(buffer) > 1000:
        return buffer[:1000] # trim saturation
    return buffer
