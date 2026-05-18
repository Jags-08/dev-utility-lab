class ShardManager:
    def allocate(self, node): return hash(node) % 1024
