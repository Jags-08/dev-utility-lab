class QuorumValidator:
    def check_quorum(self, acks, required): return len(acks) >= required
