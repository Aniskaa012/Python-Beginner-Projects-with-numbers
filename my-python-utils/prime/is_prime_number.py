#program to count the number of vowels
def vowel(word):
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0
    for char in (word):
        if char in vowels:
            count += 1
    return count

word = input("Enter a word: ").lower()
result = vowel(word)

print(f"The number of vowels is: {result}")
