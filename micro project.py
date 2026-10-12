queue = []

def add_student():
    name = input("Enter student name: ")
    queue.append(name)
    print(name, "added to university.")

def remove_student():
    if queue:
        print("Removed student:", queue.pop(0))
    else:
        print("Queue is empty.")

def display():
    print("University Student Queue:", queue)

while True:
    print("\n--- University Organization System ---")
    print("1. Add Student")
    print("2. Remove Student")
    print("3. Display Students")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        add_student()
    elif choice == 2:
        remove_student()
    elif choice == 3:
        display()
    elif choice == 4:
        print("Program ended.")
        break
    else:
        print("Invalid choice")
