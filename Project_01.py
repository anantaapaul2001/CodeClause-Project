import random
def guess_number():
    secret_number = random.randint(1, 100)  #generating a random number between 1 to 100
    attempts = 0

    print("Welcome to guessing game!")
    print("Here, I have a number that you need to guess it correctly")

    while True:
        try:
    # get the user's guess
            guess = int(input("Enter the number that you have guessed"))
            attempts +=1

    #Check if the number is correct or not 
            if guess == secret_number:
                print(f"Congratulations! You have guessed the right number {secret_number} correctly in {attempts} attempts!")
                break 
            elif guess< secret_number:
                print("Oops! The number is too low. Try again!")
            else:
                print("A lit bit bigger. Better Luck next time")
        except ValueError: 
            print("Invalid input! Please check your number.")

if __name__ == "__main__":
    guess_number()  



