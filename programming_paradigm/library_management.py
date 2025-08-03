class Book:
    def __init__(self, title, author, _is_checked_out):
        """Initialize a book with title, author, and checked out status."""
        self.title = title
        self.author = author
        self._is_checked_out = _is_checked_out

    def is_checked_out(self):
        """Return whether the book is checked out."""
        return self._is_checked_out 
    


class Library:
    def __init__(self, _books):
        """Initialize an empty library."""
        self._books = _books
        

    def add_book(self, book):
        """Add a book to the library."""
        self.books.append(book)

    def list_available_books(self):
        """List all available books in the library."""
        for book in self.books:
            if not book.is_checked_out():
                print(f"{book.title} by {book.author}")

    def check_out_book(self, title):
        """Check out a book by title."""
        for book in self.books:
            if book.title == title and not book.is_checked_out():
                book._is_checked_out = True
                print(f"Checked out: {book.title}")
                return
        print(f"Book '{title}' is not available.")

    def return_book(self, title):
        """Return a checked out book by title."""
        for book in self.books:
            if book.title == title and book.is_checked_out():
                book._is_checked_out = False
                print(f"Returned: {book.title}")
                return
        print(f"Book '{title}' was not checked out.")