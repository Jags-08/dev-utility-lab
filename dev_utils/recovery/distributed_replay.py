class DistributedReplaySync:
    def __init__(self):
        self.state_vectors = set()

    def merge_vector(self, vector_hash):
        self.state_vectors.add(vector_hash)
    
    def is_fully_replicated(self, expected_count):
        return len(self.state_vectors) >= expected_count
