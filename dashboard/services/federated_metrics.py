class FederatedMetrics:
    def __init__(self):
        self.nodes = {}

    def register_node(self, node_id, throughput):
        self.nodes[node_id] = throughput

    def aggregate_global_throughput(self):
        return sum(self.nodes.values())
