def feedback(text):
    text = text.lower().strip()
    words = text.split()
    positive_words = 0
    negative_words = False

    for word in words:
        if word == "good" or word == "excelent":
            positive_words += 1
        elif word == "bad" or word == "poor":
            negative_words = True
            break
    
    if negative_words: 
        return "Negative feedback"
    elif positive_words == 1:
        return "Positive feedback"
    elif positive_words >= 2:
        return "Very positive feedback"
    else:
        return "Neutral feedback"