def tune_routing_consistency(routes):
    return {k: v for k, v in routes.items() if v['health'] == 'verified'}
