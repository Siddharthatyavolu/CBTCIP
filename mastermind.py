import random

def generate_secret_number():
    return str(random.randint(1000, 9999))

def get_correct_digits_and_positions(secret_number, guess):
    correct_digits_and_positions = []
    for i in range(4):
        if secret_number[i] == guess[i]:
            correct_digits_and_positions.append((guess[i], i))
    return correct_digits_and_positions

def play_mastermind():
    print("Welcome to the Mastermind game!")
    print("Player 1 will set a secret number, and Player 2 will try to guess it.")
    print("The secret number is a 4-digit number between 1000 and 9999.")
    print("Digits can repeat.")

    # Player 1 sets the secret number
    player1_secret = generate_secret_number()

    attempts_player1 = 0
    attempts_player2 = 0

    while True:
        print("\nPlayer 2's turn to guess Player 1's number.")
        guess_player2 = input("Enter your guess: ")

        if guess_player2 == player1_secret:
            print("Player 2 wins! Player 1's secret number was", player1_secret)
            break

        correct_digits_and_positions = get_correct_digits_and_positions(player1_secret, guess_player2)
        if correct_digits_and_positions:
            print("Player 2 got the following digits and their positions correct:")
            for digit, position in correct_digits_and_positions:
                print(f"Digit '{digit}' at position {position + 1}")

        attempts_player2 += 1

    # Player 2 sets the secret number
    player2_secret = generate_secret_number()

    while True:
        print("\nPlayer 1's turn to guess Player 2's number.")
        guess_player1 = input("Enter your guess: ")

        if guess_player1 == player2_secret:
            print("Player 1 wins! Player 2's secret number was", player2_secret)
            break

        correct_digits_and_positions = get_correct_digits_and_positions(player2_secret, guess_player1)
        if correct_digits_and_positions:
            print("Player 1 got the following digits and their positions correct:")
            for digit, position in correct_digits_and_positions:
                print(f"Digit '{digit}' at position {position + 1}")

        attempts_player1 += 1

    if attempts_player1 < attempts_player2:
        print("Player 1 is crowned Mastermind!")
    elif attempts_player1 > attempts_player2:
        print("Player 2 is crowned Mastermind!")
    else:
        print("It's a draw!")

if __name__ == "__main__":
    play_mastermind()
