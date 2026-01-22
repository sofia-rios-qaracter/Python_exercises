def text_analizer(text):
    words = text.lower().split()
    long_words = 0
    text_len = len(text)

    if text_len > 10:
        text_type = "Long"
    else:
        text_type = "Short"

    for word in words:
        if len(word) > 5:
            long_words += 1
    
    return {"Length_of_the_text": text_len, "Type_of_text": text_type, "Long_words": long_words}


lorem = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."

texts = [lorem, "Short text", "Long_word"]

for text in texts:
    print("="*30)
    print("Analizing the following text:\n")
    print(text)
    print("\nResults:")
    print(text_analizer(text))

print("="*20)