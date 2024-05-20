from queue import LifoQueue

# Initialize the stacks for backward and forward history
backward_history = LifoQueue()
forward_history = LifoQueue()
current_page = None

# Prompt the user to enter the number of URLs they want to visit
NoOfvisits = int(input("Enter the number of URL history: "))

print("Enter URLs to visit:")

# Loop through the number of visits to get URLs from the user
for i in range(NoOfvisits):
    url = input("URL: ")
    print(f"Visiting {url}")
    # Push the current page onto the backward history stack
    backward_history.put(current_page)
    # Update the current page to the new URL
    current_page = url

# Print the current page after all URLs are entered
print(f"Current page: {current_page}")

# Go back in history
while input("Do you want to go back (yes/no): ").lower() == "yes":
    if not backward_history.empty():
        # Push the current page onto the forward history stack
        forward_history.put(current_page)
        # Pop the last page from the backward history stack and set it as the current page
        current_page = backward_history.get()
        print(f"Going back to {current_page}")
    else:
        print("No previous page available")

# Go forward in history
while input("Do you want to go forward (yes/no): ").lower() == "yes":
    if not forward_history.empty():
        # Push the current page onto the backward history stack
        backward_history.put(current_page)
        # Pop the last page from the forward history stack and set it as the current page
        current_page = forward_history.get()
        print(f"Going forward to {current_page}")
    else:
        print("No forward page available")
