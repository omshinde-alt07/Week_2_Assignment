def analyze_value(value):
    """
    Analyze any Python value and return a formatted summary.
    """
    value_type = type(value).__name__
    truthy = bool(value)

    # Check if length is applicable
    try:
        length = len(value)
    except TypeError:
        length = "N/A"

    return (
        f"Value: {value} | "
        f"Type: {value_type} | "
        f"Truthy: {truthy} | "
        f"Length: {length}"
    )


print(analyze_value(42))
print(analyze_value(""))
print(analyze_value([1, 2, 3]))
print(analyze_value(None))

