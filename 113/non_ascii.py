def extract_non_ascii_words(text):
    """Filter a text returning a list of non-ascii words"""
    return [i for i in text.split(" ") if not i.isascii()]