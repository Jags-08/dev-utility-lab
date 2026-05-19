def check_replay_affinity(shard_id):
    return shard_id % 2 == 0 # Mock affinity parity
