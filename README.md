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
