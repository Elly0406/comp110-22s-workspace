"""EX03 - Structured Wordle - Implement wordle program with function definitions."""

__author__ = "730365499"


def main() -> None:
    """The entry point of the program and main game loop."""
    turn_number: int = 1
    secret_word: str = "codes"
    game_result: bool = False
    guess_result: str = ""
    # To check how many times the user get correct secret word in 6 chances.
    while turn_number <= 6 and game_result is False: 
        print(f"=== Turn {turn_number}/6 ===")
        guess_result = input_guess(len(secret_word))
        print(emojified(guess_result, secret_word))
        if guess_result == secret_word:
            game_result = True
        else:
            turn_number += 1
    if game_result is True:
        print(f"You won in {turn_number}/6 turns!")
    else:
        print("X/6 - Sorry, try again tomorrow!")
    

def contains_char(word: str, character: str) -> bool:
    """Return corresponding boolean if character is found in word or not"""
    assert len(character) == 1
    index: int = 0
    exist: bool = False
    while exist is False and index < len(word):
        if character == word[index]:
            exist = True
        else: 
            index += 1
    return exist 


def emojified(guess: str, secret: str) -> str:
    """Return the corresponding color to each character"""
    assert len(guess) == len(secret)
    WHITE_BOX: str = "\U00002B1C"
    YELLOW_BOX: str = "\U0001F7E8"
    color_result: str = ""
    i: int = 0
    # while loop to check each character's color in guess word
    while i < len(secret):
        if contains_char(secret, guess[i]) is True:
            color_result += YELLOW_BOX
        else:
            color_result += WHITE_BOX
        i += 1
    return color_result


def input_guess(length: int) -> str:
    """Check if user input correct length. return guess with correct length"""
    answer: str = input(f"Enter a {length} character word: ")
    while len(answer) != length:
        answer = input(f"That wasn't {length} chars! Try again: ")
    return answer


if __name__ == "__main__":
    main()