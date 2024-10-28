todo_lists = []

def show_menu():
    menus = [
        "Add task",
        "Remove task",
        "Search task",
        "Update task ",
        "View done tasks",
        "Sort tasks",
        "Exit"
    ]

    print("menu options:")
    for index in range(len(menus)):
        print(f"{index+1}. {menus[index]}")

def sort_tasks():
    print("Sorted tasks")
    for task in todo_lists:
        print(task)

def add_task():
    name_of_task = input("Enter the name of the task:")
    status_of_the_task = input("Enter the status of the task:")

    task = f"{name_of_task},{status_of_the_task}"
    todo_lists.append(task)
    print(f"{task} has been added to the list")



def main():
    while True:
        show_menu()
        choice = input("What would you like to do:")
        if choice == "1":
            add_task()
        elif choice =="6":
            sort_tasks()
        elif choice == "7":
            confirm = input("Are you sure you want to quit?(y/n):")
            if confirm == "y":
                print("Thank you for using this app")
                exit(0)


main()