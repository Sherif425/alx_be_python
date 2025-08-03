class Book:
    """
    A class to represent a book with its title, author, and availability status.
    """
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out(self):
        """Marks the book as checked out."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        """Marks the book as available."""
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    def is_available(self):
        """Returns True if the book is not checked out, otherwise False."""
        return not self._is_checked_out


class Library:
    """
    A class to manage a collection of Book objects.
    """
    def __init__(self):
        self._books = []

    def add_book(self, book):
        """Adds a new Book object to the library's collection."""
        self._books.append(book)

    def find_book(self, title):
        """Helper method to find a book by title."""
        for book in self._books:
            if book.title == title:
                return book
        return None

    def check_out_book(self, title):
        """
        Checks out a book from the library by its title.
        Prints a success or failure message.
        """
        book = self.find_book(title)
        if book and book.check_out():
            print(f"'{title}' has been successfully checked out.")
        else:
            print(f"'{title}' is not available for checkout.")

    def return_book(self, title):
        """
        Returns a book to the library by its title.
        Prints a success or failure message.
        """
        book = self.find_book(title)
        if book and book.return_book():
            print(f"'{title}' has been successfully returned.")
        else:
            print(f"'{title}' could not be returned.")

    def list_available_books(self):
        """Prints the title and author of all currently available books."""
        for book in self._books:
            if book.is_available():
                print(f"{book.title} by {book.author}")
                