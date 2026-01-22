def count_character_repetition(text):
    repited_characters = 0
    character_list = {}
    repited_character_list = []

    for character in text.lower():
        try:
            character_list[character] += 1
            repited_characters += 1
            repited_character_list.append(character)
        except Exception:
            character_list[character] = 1

    return {"List_of_repited_characters": repited_character_list, "Repited_characters": repited_characters}

print(count_character_repetition("Programming"))