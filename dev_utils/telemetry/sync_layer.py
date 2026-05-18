class TelemetrySyncLayer:
    @staticmethod
    def synchronize(vectors):
        merged = {}
        for vec in vectors:
            node_id = vec.get('node_id')
            if node_id not in merged or vec.get('timestamp') > merged[node_id].get('timestamp'):
                merged[node_id] = vec
        return list(merged.values())
