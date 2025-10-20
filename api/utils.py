import hashlib
from collections import Counter

def analyze_string(value: str) -> dict:
    """
    Analyze a given string and return all computed properties.
    """
    if not isinstance(value, str):
        raise ValueError("Value must be a string")

    # Clean up spacing
    stripped_value = value.strip()

    # Compute SHA256 hash
    sha256_hash = hashlib.sha256(stripped_value.encode()).hexdigest()

    # Compute basic properties
    length = len(stripped_value)
    is_palindrome = stripped_value.lower() == stripped_value[::-1].lower()
    unique_characters = len(set(stripped_value))
    word_count = len(stripped_value.split())

    # Character frequency map (counting how many times each character appears)
    frequency_map = dict(Counter(stripped_value))

    return {
        "length": length,
        "is_palindrome": is_palindrome,
        "unique_characters": unique_characters,
        "word_count": word_count,
        "sha256_hash": sha256_hash,
        "character_frequency_map": frequency_map
    }
