# Function to display the menu options
def display_menu():
    print('Personal To-Do list Menu:')
    print('[1] Add Task')
    print('[2] Mark Task as Completed')
    print('[3] View To-Do List')
    print('[4] Prioritize Task')
    print('[5] Remove Completed Tasks')
    print('[6] Exit')

    while True:
        try:
            user_input = int(input('Enter your choice (1-6): '))
            if user_input not in range(1,7):
                raise ValueError 
            break
        except ValueError:
            print('Invalid choice. Please try again. ')
    
    return user_input


# Function to add a new task to the to-do list
def add_task(todo_list):
    new_task = input('Enter the task: ')
    todo_list.append({'Description':new_task, 'Complete':False, 'Priority':None})
    print('Task added successfully!')


# Function to display the current to-do list
def display_todo_list(todo_list):
    if len(todo_list) == 0:
        print('Nothing to do, lucky you!')
        return -1
    

    for index, task in enumerate(todo_list):
        if todo_list[index]['Complete'] == False:
            complete = 'Pending' 
        else:
            complete = 'Complete'
        
        if todo_list[index]['Priority'] != None:
            priority = f'Priority: {todo_list[index]['Priority']}'
        else:
            priority = ''
    
        print(f"{index}. {task['Description']} - {complete} - {priority}")


# Function to mark a task as completed
def mark_completed(todo_list):
    print('To-Do List')
    print('-' * 10)

    if display_todo_list(todo_list) == -1:
        return
    
    try:
        index = int(input('Enter the index of the task to mark as completed: '))
        if index not in range(len(todo_list)):
            raise ValueError
    
    except ValueError:
        print('Invalid index. Please try again.')
        return
    
    todo_list[index]['Complete'] = True
    print('Task marked as complete!')
    


# Function to prioritize a task
def prioritize_task(todo_list):
    print('To-Do List')
    print('-' * 10)
    if display_todo_list(todo_list) == -1:
        return

    try:
        index = int(input('Enter the index of the task to prioritize: '))
        if index not in range(len(todo_list)):
            raise ValueError
    except ValueError:
        print('Invalid index. Please try again.')
        return


    try:
        priority = input('Enter the priority level (High, Medium, or Low): ').capitalize()
        if priority not in ['High', 'Medium', 'Low']:
            raise ValueError
        else:
            todo_list[index]['Priority'] = priority
            print('Task priority updated!')
            return
    except ValueError:
        print('Invalid priority level. Please enter High, Medium, or Low')
        return
    

# Function to remove completed tasks
def remove_completed_tasks(todo_list):
    removed_tasks = [task for task in todo_list if task['Complete'] == True]
    for task in todo_list[:]:
        if task['Complete'] == True:
            todo_list.remove(task)

    if len(removed_tasks) == 0:
        print('There are no completed tasks...')
    else:
        print("Completed Tasks to Remove:")
        display_todo_list(removed_tasks)
        print('Completed tasks removed successfully!')


# Main function to manage the to-do list
def main():
    todo_list = []

    while True:
        user_input = display_menu()

        if user_input ==  6:
            print('Exiting program... Goodbye!')
            break
        elif user_input == 1:
            add_task(todo_list)
        elif user_input == 2:
            mark_completed(todo_list)
        elif user_input == 3:
            print('To-Do List')
            print('-' * 10)
            display_todo_list(todo_list)
        elif user_input == 4:
            prioritize_task(todo_list)
        elif user_input == 5:
            remove_completed_tasks(todo_list)
        
        print()
        print()





# Call the main function
if __name__ == "__main__":
    main()
