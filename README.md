Task-1
Description

Main Functionality:
The program allows users to manage a list of tasks through a menu-driven interface. Users can add tasks, view tasks, mark tasks as completed, and exit the application.

Data Structure:
Tasks are stored in a list of dictionaries, where each dictionary contains:

task: The description of the task.
done: A boolean indicating whether the task is completed.

Menu Options:
Add Task: Users can add multiple tasks at once by specifying the number of tasks they wish to add. Each task is prompted for input and appended to the tasks list.
Show Tasks: Displays all tasks along with their status (either "Done" or "Not Done"). Each task is listed with a corresponding index number.
Mark Task as Done: Users can mark a specific task as completed by entering its index number. The program checks if the index is valid before updating the task's status.

Exit: Ends the program.

User Input Handling:
The program includes input validation, particularly for marking tasks as done, ensuring the entered task number is valid.

Loop Structure:
A while True loop is used to continuously display the menu until the user chooses to exit.

Task-2
Description

Functionality:
The program provides a menu for users to select from four arithmetic operations: addition, subtraction, multiplication, and division.

Arithmetic Functions:
Addition: The add(num1, num2) function returns the sum of num1 and num2.
Subtraction: The subtract(num1, num2) function returns the difference between num1 and num2.
Multiplication: The multiply(num1, num2) function returns the product of num1 and num2.
Division: The divide(num1, num2) function returns the quotient of num1 divided by num2. (Note: This function does not handle division by zero.)

User Interface:
The program prompts the user to select an operation by entering a number from 1 to 4.
After selecting the operation, the user is asked to input two numbers on which the selected operation will be performed.

Input Handling:
The program reads the user’s choice and the two numbers. It uses conditional statements (if, elif, else) to execute the corresponding arithmetic function based on the user’s selection.

Output:
The result of the selected operation is displayed in a formatted manner, showing the calculation performed (e.g., number_1 + number_2 = result).

Error Handling:
The program includes a basic error handling mechanism for invalid operation selections, informing the user if the input is not recognized

Task-3
Description

Character Sets:
The password generator uses uppercase and lowercase letters, digits, and punctuation characters to create a strong password.

User Input:
The program prompts the user to enter the desired length of the password, ensuring that the length is at least 8 characters for better security.

Password Generation:
The generate_password function creates a password by randomly selecting characters from the defined character set based on the specified length.

Display:
The generated password is printed to the console for the user to see.
