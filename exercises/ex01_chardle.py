"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730365499"

word: str = input("Enter a 5-character word: ")
if len(word) != 5:
    print("Error: Word must contain 5 characters")
else:
    single_character: str = input("Enter a single character: ")
    if len(single_character) != 1:
        print("Error: Character must be a single character.")
    else: 
        print("Searching for " + single_character + " in " + word)

        number: int = 0
        if single_character == word[0]:
            print(single_character + " found at index 0")
            number = number + 1
        if single_character == word[1]:
            print(single_character + " found at index 1")
            number = number + 1
        if single_character == word[2]:
            print(single_character + " found at index 2")
            number = number + 1
        if single_character == word[3]:
            print(single_character + " found at index 3")
            number = number + 1
        if single_character == word[4]:
            print(single_character + " found at index 4")
            number = number + 1
        if number == 1:
            print(str(number) + " instance of " + single_character + " found in " + word)
        else: 
            if number > 1:
                print(str(number) + " instances of " + single_character + " found in " + word)
            else:
                print("No instances of " + single_character + " found in " + word)
