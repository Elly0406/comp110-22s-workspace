"""EX02 - One-Shot Wordle - Next step to implement Wordle."""

__author__ = "730365499"

secret_word: str = "python"
length: int = len(secret_word)
guess: str = input(f"What is your { length }-letter guess? ")
index: int = 0
emoji_result: str = ""
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

# This is the while loop to check if the guess has correct length
while len(guess) != length:
    guess: str = input(f"That was not { length } letters! Try again: ")

# This is the while loop to check each index one by one 
while index < length:
    # When index of guess is not equal to index of secret word
    # check if guess character exsits in other position or not
    # Otherwise, print Green. 
    if guess[index] != secret_word[index]:
        exist: bool = False
        alternate_index: int = 0
        while exist is False and alternate_index < length:
            if secret_word[alternate_index] == guess[index]:
                exist = True
            else:
                alternate_index += 1
        # Print Yellow if there is a same character in secret word
        # Print white if there is not.
        if exist is True: 
            emoji_result += YELLOW_BOX
        else:
            emoji_result += WHITE_BOX
    else:
        emoji_result += GREEN_BOX
    index += 1
print(emoji_result)

# This is to check if the guess word exactly matches secret word
if guess != secret_word:
    print("Not quite. Play again soon!")
else:
    print("Woo! You got it!")
