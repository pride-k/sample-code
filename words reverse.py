sentence = input()
words = sentence.split()
words = words[::-1]
sentence = " ".join(words)
print(sentence.swapcase())
