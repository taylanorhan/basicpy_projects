# Initialize an empty list to store tasks
tasks = []

# Function to add tasks
def add_task(task):
    tasks.append(task)

# Function to display tasks
def display_tasks():
    if tasks:
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. {task}")
    else:
        print("No tasks in the list.")

# Function to delete tasks by index
def delete_task(index):
    if index >= 1 and index <= len(tasks):
        del tasks[index - 1]
        print("Task deleted.")
    else:
        print("Invalid task number.")

# Example usage
add_task("Buy groceries")
add_task("Read a book")
display_tasks()
delete_task(1)
display_tasks()

