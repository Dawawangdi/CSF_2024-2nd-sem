from queue import Queue

def register_patient(queue):
    name = input("Enter patient name: ")
    queue.put(name)
    print("Patient", name, "registered.")

def remove_patient(queue):
    if queue.empty():
        print("No patients in the queue.")
    else:
        name = queue.get()
        print("Patient", name, "removed after meeting the doctor.")

def display_queue(queue):
    if queue.empty():
        print("No patients in the queue.")
    else:
        print("Current queue of patients:")
        for index, name in enumerate(queue.queue):
            print(index + 1, ".", name)

def main():
    patient_queue = Queue()

    while True:
        print("\nMenu:")
        print("1. Register Patient")
        print("2. Remove Patient after Meeting Doctor")
        print("3. Display Patient Queue")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            register_patient(patient_queue)
        elif choice == '2':
            remove_patient(patient_queue)
        elif choice == '3':
            display_queue(patient_queue)
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()

