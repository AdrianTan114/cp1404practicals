"""
Word Occurrences
Estimate: 20 minutes
Actual:   17 minutes
"""

word_to_count = {}
text = input("Text: ")
words = text.split(" ")
for word in words:
    if word in word_to_count:
        word_to_count[word] += 1
    else:
        word_to_count[word] = 1
width = max((len(word) for word in word_to_count))
for word, count in sorted(word_to_count.items()):
    print(f"{word:{width}} : {count}")
