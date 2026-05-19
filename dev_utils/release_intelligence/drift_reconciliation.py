def reconcile_config_drift(expected, actual):
    diff = set(expected) - set(actual)
    return list(diff)
