# Activity 3: Vowel Counter
# Count all vowels in a sentence, including uppercase and lowercase vowels.

sentence = input("Sentence: ")
vowels = "aeiouAEIOU"
count = 0

for character in sentence:
    if character in vowels:
        count += 1

print("Vowels:", count)
