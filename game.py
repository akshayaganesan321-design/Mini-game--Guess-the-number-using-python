print("Welcome to the Number Guessing Game!")

print("Choose difficulty level:")
print("1. Easy (1-10)")
print("2. Medium (1-50)")
print("3. Hard (1-100)")

level = input("Enter level (1/2/3): ")

if level == "1":
    max_num = 10
elif level == "2":
    max_num = 50
else:
    max_num = 100

secret_number = (hash("secret") % max_num) + 1

attempts = 0
print(f"\nI have chosen a number between 1 and {max_num}. Try to guess it!")

while True:
    guess = input("Enter your guess: ")
    if not guess.isdigit():
        print("Please enter a valid number.")
        continue

    guess = int(guess)
    attempts += 1

    if guess < secret_number:
        print("Too low!")
    elif guess > secret_number:
        print("Too high!")
    else:
        print(f" Correct! The number was {secret_number}.")
        print(f"You guessed it in {attempts} attempts.")
        break
