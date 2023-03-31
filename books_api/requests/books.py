import requests

def get_books(limit:'', book_type:''):
    return requests.get(f'https://simple-books-api.glitch.me/books?type={book_type}&limit={limit}')

def get_book(id):
    return requests.get(f'https://simple-books-api.glitch.me/books/{id}')