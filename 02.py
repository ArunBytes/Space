def process_names(names):
    """Filter and sort names by length"""
    # Filter names longer than 3 characters
    long_names = [name for name in names if len(name) > 3]
    # Sort alphabetically
    return sorted(long_names)

names = ["Ali", "Sarah", "Bob", "Alexander"]
print(process_names(names))
# Output: ['Alexander', 'Sarah']