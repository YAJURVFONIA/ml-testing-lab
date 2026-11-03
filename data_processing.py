def remove_duplicates(items):
    """Keep each item only once, in the original order."""
    result = []
    for item in items:
        if item not in result:
            result.append(item)
    return result
 
 
def fill_missing(values):
    """Replace each None with the average of the other numbers."""
    known = [v for v in values if v is not None]
    average = sum(known) / len(known)
    return [average if v is None else v for v in values]
 
 
def scale_0_to_1(values):
    """Squeeze numbers into the range 0 to 1."""
    low, high = min(values), max(values)
    if high == low:
        return [0.0 for v in values]
    return [(v - low) / high for v in values]
