def count_vocals(word):
    vocals = ["a", "e", "i", "o", "u"]
    total_of_vocals = 0
    for vocal in vocals:
        total_of_vocals += word.lower().count(vocal)
    
    return total_of_vocals

word = "Esternocleidomastoideo"

print(f"Vocals in the word {word}: {count_vocals(word)}")