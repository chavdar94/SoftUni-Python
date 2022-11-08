words = input().split()
key_word = input()

palindromes = [x for x in words if x == x[::-1]]
print(palindromes)
key_word_occurrence = palindromes.count(key_word)
print(f"Found palindrome {key_word_occurrence} times")