from collections import Counter

word_one = input()
word_two = input()
print("YES" if Counter(word_one) == Counter(word_two) else 'NO')

