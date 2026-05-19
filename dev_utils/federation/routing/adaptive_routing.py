def calculate_adaptive_route(packet, network_map):
    # Determine least-saturated path based on heatmaps
    return sorted(network_map, key=lambda x: network_map[x]['saturation'])[0]
