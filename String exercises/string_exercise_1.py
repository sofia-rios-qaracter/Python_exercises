text_user_1 = input("Given text for user 1: ")
text_user_2 = input("Given text for user 2: ")

text_user_1 = text_user_1.lower().strip()
text_user_2 = text_user_2.lower().strip()

if text_user_1 == text_user_2: print("Same category")
else: print("Different category")