def is_suffix(suffix, word):
    if len(suffix) > len(word):
        return False
    return word[-len(suffix):] == suffix
