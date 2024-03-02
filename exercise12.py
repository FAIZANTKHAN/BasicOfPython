from collections import Counter

with open('poem.txt','r') as file:
    poem=file.read()

words=poem.split()
word_counts=Counter(words)

max_count=max(word_counts.values())

max_occurence_words=[word for word, count in word_counts.items() if count==max_count]

print(f"Words with maximum occurrence ({max_count}  times):")
for word in max_occurence_words:
    print(f"{word}: {max_count} times")