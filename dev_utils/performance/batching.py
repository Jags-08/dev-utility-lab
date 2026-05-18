class AdaptiveBatcher:
    def __init__(self, max_batch_size=1000):
        self.max_batch_size = max_batch_size
        self.buffer = []

    def append(self, item):
        self.buffer.append(item)
        if len(self.buffer) >= self.max_batch_size:
            return self.flush()
        return None

    def flush(self):
        batch = self.buffer[:]
        self.buffer.clear()
        return batch
