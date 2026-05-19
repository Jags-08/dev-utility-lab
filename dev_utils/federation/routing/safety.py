def safeguard_retry_exhaustion(attempts):
    if attempts >= 5:
        raise Exception("Federation Replay Exhaustion. Node isolated.")
