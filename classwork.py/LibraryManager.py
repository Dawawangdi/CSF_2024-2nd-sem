# Initialize empty list, set, and dictionary to store books, authors, and book-author mappings
book_list = []
author_set = set()
book_dict = {}

# Add books to the library
book_list.append("Python Programming")  # Add book title to list
author_set.add("karma")  # Add author to set
book_dict["Python Programming"] = "karma"  # Map book title to author in dictionary

book_list.append("Data Structures and Algorithms")
author_set.add("dawa")
book_dict["Data Structures and Algorithms"] = "dawa"

book_list.append("Machine Learning Basics")
author_set.add("dorji")
book_dict["Machine Learning Basics"] = "dorji"

# Search for a book by title
search_book = input("Enter the title of the book to search: ").strip()
if search_book in book_list:
    print(f"Book found! \nTitle: {search_book}\nAuthor: {book_dict[search_book]}")
else:
    print("Book not found!")

# Display all books in the library
print("\nList of books in the library: ")
for book in book_list:
    print(book)

# Prompt the user to remove a book by title
remove_title = input("\nEnter the title of the book to remove or press Enter to skip: ").strip()
if remove_title:
    if remove_title in book_list:
        remove_author = book_dict[remove_title]  # Retrieve the author's name
        book_list.remove(remove_title)  # Remove the book title from list
        author_set.remove(remove_author)  # Remove the author's name from set
        del book_dict[remove_title]  # Delete the book entry from dictionary
        print("Book removed successfully.")
    else:
        print("Book not found!")
else:
    print("No book removed.")
