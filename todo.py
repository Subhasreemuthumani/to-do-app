todo_list = []

def add_task():
    task = input("📝 Enter a new task: ")
    todo_list.append({"task": task, "done": False})
    print("✅ Task added!\n")

def view_tasks():
    if not todo_list:
        print("📭 No tasks in the list.\n")
    else:
        print("\n📋 --- To-Do List ---")
        for idx, item in enumerate(todo_list, 1):
            status = "✅" if item["done"] else "❌"
            print(f"{idx}. [{status}] {item['task']}")
        print()

def mark_done():
    view_tasks()
    try:
        num = int(input("✔️ Enter task number to mark as done: "))
        if 1 <= num <= len(todo_list):
            todo_list[num - 1]["done"] = True
            print("🎉 Task marked as done!\n")
        else:
            print("❌ Invalid task number.\n")
    except ValueError:
        print("❌ Please enter a valid number.\n")

def delete_task():
    view_tasks()
    try:
        num = int(input("🗑️ Enter task number to delete: "))
        if 1 <= num <= len(todo_list):
            removed = todo_list.pop(num - 1)
            print(f"🗑️ Deleted: {removed['task']}\n")
        else:
            print("❌ Invalid task number.\n")
    except ValueError:
        print("❌ Please enter a valid number.\n")

def show_menu():
    while True:
        print("🔹 To-Do List CLI App 🔹")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("👉 Choose an option (1-5): ")

        if choice == '1':
            add_task()
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            mark_done()
        elif choice == '4':
            delete_task()
        elif choice == '5':
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice, please try again.\n")

# Run the app
show_menu()
