print("Hello, welcome to a new sentence length checker")
userInput = input("Write a sentence: ")

if len(userInput) > 20:
    print("Oh, great! Your sentence is enough long.")
else: 
    print("Good try! Your sentence is not enough long")