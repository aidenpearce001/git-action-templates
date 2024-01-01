# file: string_operations.py
def uppercase_string(s):
    if not isinstance(s, str):
        raise ValueError("Only strings are allowed")
    return s.upper()

def lowercase_string(s):
    if not isinstance(s, str):
        raise ValueError("Only strings are allowed")
    return s.lower()