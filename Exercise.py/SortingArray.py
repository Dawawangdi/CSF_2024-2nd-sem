
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less_than_pivot = [x for x in arr[1:] if x <= pivot]
        greater_than_pivot = [x for x in arr[1:] if x > pivot]
        return quick_sort(less_than_pivot) + [pivot] + quick_sort(greater_than_pivot)

# Function to search and replace elements in the array
def search_and_replace(arr, target, replacement):
    found = False
    for i in range(len(arr)):
        if arr[i] == target:
            arr[i] = replacement
            found = True
    return found

while True:
    # Prompting the user to input an array of integers
    arr = [int(x) for x in input("Array Sorting and Element Replacement\nEnter the array elements separated by spaces: ").split()]

    # Sorting the input array using quick sort algorithm
    arr = quick_sort(arr)

    # Displaying the sorted array
    print("Array:", arr, "Sorted Array using Quick Sort:", arr)

    # Prompting the user to input a target element to search for
    target = int(input("Enter the element to search for: "))

    # If the target element is found, prompting the user to input a replacement element
    replacement = None  # Defining replacement here
    if search_and_replace(arr, target, replacement):
        print("Enter the replacement element: ")
        replacement = int(input())
        # Replaceing all occurrences of the target element with the replacement element
        search_and_replace(arr, target, replacement)
        # Displaying the modified array after replacing elements
        print("Modified Array after replacing", target, "with", replacement, ":", arr)
    else:
        print("Element not found in the given array.")
