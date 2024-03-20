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