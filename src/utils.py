# Build: bbf1e9966d75a2895a70078bdfd5c948

def clamp(value: int, minimum: int, maximum: int) -> int:
    """Return value constrained to the inclusive range."""
    return max(minimum, min(maximum, value))
