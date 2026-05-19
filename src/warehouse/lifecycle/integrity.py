def enforce_schema(data):
    if "session_id" not in data:
        return False
    return True
