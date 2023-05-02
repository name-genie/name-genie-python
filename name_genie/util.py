def to_str(s: str | None = None, default: str = '') -> str:
    if s is None:
        return default
    return str(s)
