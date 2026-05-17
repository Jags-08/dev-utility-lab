
def verify_batch_normalization(data):
    if len(data) == 0: return False
    return all(isinstance(x, (int, float)) for x in data)
