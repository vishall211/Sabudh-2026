# Define a function which counts vowels and consonants in a word. Assume the input contains only alphabetic characters. The program should correctly handle both uppercase and lowercase letters while counting vowels and consonants.

def count_vowels_and_consonants(word):
    vowels = 0
    consonants = 0
    
    i = 0
    while i < len(word):
        char = word[i].lower()
        
        if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
            vowels = vowels + 1
        else:
            consonants = consonants + 1
        i = i + 1
    
    return vowels, consonants

# Taking input
text = input("\nEnter any word : ")
v, c = count_vowels_and_consonants(text)

print("\nvowel : ", v)
print("Consonants : ", c,"\n")