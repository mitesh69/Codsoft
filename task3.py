import random
import string

def generate_password(length):
    # Define the character sets to use for the password
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate a random password from the defined character set
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

def main():
    print("Welcome to the Password Generator!")
 
    while True:
        try:
            length = int(input("Enter the desired length of the password (8 or more): "))
            if length >= 8:
                break
            else:
                print("Please enter a length of at least 8.")
        except ValueError:
            print("Invalid input. Please enter a number.")
    password = generate_password(length)
    print(f"Your generated password is: {password}")

if __name__ == "__main__":
    main()
