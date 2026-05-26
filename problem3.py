from abc import ABC, abstractmethod


# =========================
# Custom Exceptions
# =========================

class BookNotAvailableError(Exception):
    pass


class BookLimitExceededError(Exception):
    pass


# =========================
# Abstract User Class
# =========================

class LibraryUser(ABC):

    def __init__(self, name, user_id):

        self.name = name
        self.user_id = user_id

        self.borrowed_books = []

    @abstractmethod
    def borrow_limit(self):
        pass

    def __str__(self):

        return (
            f"User: {self.name} | "
            f"ID: {self.user_id}"
        )


# =========================
# Student Member
# =========================

class StudentMember(LibraryUser):

    def borrow_limit(self):

        return 3


# =========================
# Teacher Member
# =========================

class TeacherMember(LibraryUser):

    def borrow_limit(self):

        return 5


# =========================
# Book Class
# =========================

class Book:

    def __init__(self, title, author):

        self.title = title
        self.author = author

        self.is_available = True

    def __str__(self):

        status = (
            "Available"
            if self.is_available
            else "Borrowed"
        )

        return (
            f"Title: {self.title} | "
            f"Author: {self.author} | "
            f"Status: {status}"
        )


# =========================
# Library Class
# =========================

class Library:

    def __init__(self):

        self.books = []

        self.users = []

    # ---------------------
    # Add Book
    # ---------------------

    def add_book(self, book):

        self.books.append(book)

        print(
            f"Book '{book.title}' "
            f"added successfully"
        )

    # ---------------------
    # Add User
    # ---------------------

    def add_user(self, user):

        self.users.append(user)

        print(
            f"User '{user.name}' "
            f"added successfully"
        )

    # ---------------------
    # Borrow Book
    # ---------------------

    def borrow_book(
        self,
        user,
        book_title
    ):

        # Check borrow limit

        if (
            len(user.borrowed_books)
            >= user.borrow_limit()
        ):

            raise BookLimitExceededError(
                "Borrow limit exceeded"
            )

        # Search book

        for book in self.books:

            if book.title == book_title:

                # Check availability

                if not book.is_available:

                    raise BookNotAvailableError(
                        "Book is not available"
                    )

                # Prevent duplicate borrowing

                if (
                    book
                    in user.borrowed_books
                ):

                    raise ValueError(
                        "Book already borrowed"
                    )

                # Borrow process

                book.is_available = False

                user.borrowed_books.append(
                    book
                )

                print(
                    f"{user.name} borrowed "
                    f"'{book.title}'"
                )

                return

        raise ValueError(
            "Book not found"
        )

    # ---------------------
    # Return Book
    # ---------------------

    def return_book(
        self,
        user,
        book_title
    ):

        for book in user.borrowed_books:

            if book.title == book_title:

                book.is_available = True

                user.borrowed_books.remove(
                    book
                )

                print(
                    f"{user.name} returned "
                    f"'{book.title}'"
                )

                return

        raise ValueError(
            "User did not borrow this book"
        )

    # ---------------------
    # Show Books
    # ---------------------

    def show_books(self):

        print("\nLibrary Books:\n")

        for book in self.books:

            print(book)

    # ---------------------
    # Show Users
    # ---------------------

    def show_users(self):

        print("\nLibrary Users:\n")

        for user in self.users:

            print(user)


# =========================
# Main Program
# =========================

library = Library()


# -------------------------
# Create Books
# -------------------------

b1 = Book(
    "Python Basics",
    "John Smith"
)

b2 = Book(
    "OOP in Python",
    "David Warner"
)

b3 = Book(
    "Data Structures",
    "Alex Johnson"
)

b4 = Book(
    "Machine Learning",
    "Andrew Ng"
)


# -------------------------
# Add Books
# -------------------------

library.add_book(b1)
library.add_book(b2)
library.add_book(b3)
library.add_book(b4)


# -------------------------
# Create Users
# -------------------------

s1 = StudentMember(
    "Steni",
    101
)

t1 = TeacherMember(
    "Meow",
    201
)


# -------------------------
# Add Users
# -------------------------

library.add_user(s1)
library.add_user(t1)


# =========================
# Borrow Operations
# =========================

try:

    library.borrow_book(
        s1,
        "Python Basics"
    )

    library.borrow_book(
        s1,
        "OOP in Python"
    )

    library.borrow_book(
        s1,
        "Data Structures"
    )

    # Exceeds limit

    library.borrow_book(
        s1,
        "Machine Learning"
    )

except (
    BookLimitExceededError,
    BookNotAvailableError,
    ValueError
) as e:

    print(f"Error: {e}")


# =========================
# Return Operation
# =========================

try:

    library.return_book(
        s1,
        "Python Basics"
    )

except ValueError as e:

    print(f"Error: {e}")


# =========================
# Display Data
# =========================

library.show_books()

library.show_users()