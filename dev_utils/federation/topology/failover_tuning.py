def predict_failover_saturation(target_shard, inbound_load):
    return target_shard.capacity > inbound_load * 1.2
