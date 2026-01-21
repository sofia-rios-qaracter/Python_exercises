def counting_good(text):
    total_goods = 0
    text = text.lower().strip()

    words = text.split(" ")
    
    # Count version
    total_goods_count = text.count("good")

    # For version
    for word in words: 
        if word == "good": 
            total_goods += 1
    print(f"Counting good's with count() : {total_goods_count}")
    print(f"Counting good's with for loop: {total_goods}")

    print(words)

counting_good("Hello, how are you, i'm good good good realy good")