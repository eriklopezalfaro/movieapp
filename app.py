from utils import database
import json

USER_CHOICE = """
Enter:
- 'a' to add a new book
- 'l' to list all books
- 'r' to mark book as read
- 'd' to delete a book
- 'q' to quit

Your choice:"""

def menu():

    user_input = input(USER_CHOICE)
    while user_input != 'q':
        if user_input == 'a':
            prompt_add_book()
        elif user_input == 'l':
            list_books()
        elif user_input == 'r':
            prompt_read_book()
        elif user_input == 'd':
            prompt_delete_book()
        else:
            print('unknown command, try again')   
        user_input = input(USER_CHOICE)

# def prompt_add_book() ask for book name and author
def prompt_add_book():
    name = input('Enter book name: ')
    author = input('Enter author name: ')
    database.add_book(name, author)

# def list_books() show all the books in our list
def list_books():
    books = database.get_all_books()
    for book in books:
        print(f"Title: {book['name']}, Author: {book['author']}, Read: {book['read']}")

# def prompt_read_book() ask for book name and change it to "read" in our list
def prompt_read_book():
    user_input = input('Enter book name: ')
    database.mark_read_book(user_input)
# def prompt_delete_book() remove book from list
def prompt_delete_book():
    user_input = input('Enter name of book to delete: ')
    database.delete_book(user_input)

menu()