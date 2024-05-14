def bubble_sort_2d(arr):
    n = len(arr)  # no. of rows in 2d array
    m = len(arr[0])  # no. of columns in the 2D; assume all rows have equal length
    total_element = n * m  # total no. of elements in array

    for i in range(total_element - 1):
        # outer loop goes through all elements in 2D array

        for j in range(total_element - 1 - i):

            # calculating current position
            row1 = j // m
            col1 = j % m

            # calculating new position (right next to current position)
            row2 = (j + 1) // m
            col2 = (j + 1) % m

            # compare the positions, swap elements if needed
            if arr[row1][col1] > arr[row2][col2]:
                # then swap
                arr[row1][col1], arr[row2][col2] = arr[row2][col2], arr[row1][col1]

def search_element(arr, element):
    found = False  # Initialize a flag if the element is found
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] == element:
                print(f"Element found at position: row = {i}, column = {j}")
                found = True
                return  # exit the function after finding the element
    if not found:
        print("Element not found in the given array")

# Example
arr = [
    [9, 2, 3],
    [4, 5, 6],
    [7, 8, 1]
]

print(arr)
bubble_sort_2d(arr)
print("Sorted Array:")
print(arr)

# searching for an element
search = int(input("Enter the element to search: "))
search_element(arr, search)
