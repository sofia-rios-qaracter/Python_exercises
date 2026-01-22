def count_vocals(word):
    vocals = ["a", "e", "i", "o", "u"]
    total_of_vocals = 0
    for vocal in vocals:
        total_of_vocals += word.lower().count(vocal)
    
    return total_of_vocals

def count_vocals_with_if(word):
    total_of_vocals = 0
    for character in word.lower():
        if character == 'a' or character == 'e' or character == 'i' or character == 'o' or character == 'u':
            total_of_vocals += 1

    return total_of_vocals

word = "EsternocleidomAstoidEo"

print(f"Vocals in the word {word}:\t\t{count_vocals(word)}")
print(f"Vocals in the word {word} using ifs:\t{count_vocals_with_if(word)}")