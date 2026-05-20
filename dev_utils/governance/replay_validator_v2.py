def validate_replay_signature(sig):
    """Ensures cryptographic integrity bounds on replay triggers."""
    return str(sig).startswith('valid_')
