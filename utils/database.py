
# books = []

from os import read
# import json

books_file = 'books.txt'

def add_book(name, author):
    # books.append({'name':name, 'author':author, 'read': False})
    with open(books_file,'a') as file:
        file.write(f'{name},{author},0\n')

def get_all_books():
    # return books
    with open(books_file,'r') as file:
        books = [book.strip().split(',') for book in file.readlines()]
    
    return [
        {'name':book[0], 'author':book[1], 'read':book[2]}
        for book in books
    ]

def mark_read_book(name):
    # for book in books:
        # if book['name'] == name:
            # book['read'] = True
    books = get_all_books()
    for book in books:
        if book['name'] == name:
            book['read'] = '1'

    _save_all_books(books) #should only be used in this file

def _save_all_books(books):
    with open(books_file,'w') as file:
        for book in books:
            file.write(f"{book['name']},{book['author']},{book['read']}\n")
        
    


def delete_book(name):
    # global books
    # books = [book for book in books if['name'] != name]
    books = get_all_books()
    books = [book for book in books if book['name']!= name]

    _save_all_books(books)