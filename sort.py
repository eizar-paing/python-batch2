nums1 = [3, -7, 1, -4, 8, -5]
sorted_nums = sorted(nums1, key=abs)
print(sorted_nums)

words = ["apple", "banana", "kiwi", "grape"]
sorted_words = sorted(words, key=lambda word: word[-1])
print(sorted_words)

# sort by frequency of item
nums2 = [4, 6, 2, 6, 4, 4, 3]
result = [2, 3, 6, 6, 4, 4, 4]
print(nums2.count(4))

# sort by count of word in each sentence
sentences = ["This is short.", "Here is a much longer sentence.", "Tiny."]
result = ["Tiny.", "This is short.", "Here is a much longer sentence."]
sentence = "This is short."
print(len(sentence.split()))  # ['This', 'is', 'short.']
