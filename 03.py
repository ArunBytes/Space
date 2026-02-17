def count_words(text):
    """Count frequency of words in text"""
    words = text.lower().split()
    word_count = {}
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
    return word_count

text = "python is great python is fun"
print(count_words(text))
# Output: {'python': 2, 'is': 2, 'great': 1, 'fun': 1}