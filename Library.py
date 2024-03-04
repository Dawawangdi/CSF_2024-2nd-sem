#initialize empty list, set, and dict


book_list = []
author_set= set()
book_dict = {}

#add books
book_list.append ("Python Programing")
author_set.add("karma")
book_dict["Python Programing"] = "karma"

book_list.append ("Data structure and Algorithms")
author_set.add("dawa")
book_dict["Data structure and Algorithms"] = "dawa"

book_list.append ("Machine Learning Basics")
author_set.add("dorji")
book_dict["Machine Learning Basics"]= "dorji"

#search for a book
search_book = input("Enter the title of the book to search: ")
if search_book in book_list:
    print(f"Book found! \nAuthor: {book_dict[search_book]}")
else:
    print("Book not found!")

#displaying all books
print("List of books: ")
for book in book_list:
    print(book)


remove_title = input("Enter the title of the book to remove or else enter to skip: ")
if remove_title in book_list:
    remove_author = book_dict[remove_title]
    book_list.remove(remove_title)
    author_set.remove(remove_author)
    del book_dict[remove_title]
    print("Book removed successfully")
else:
    print("Book not fouund!")