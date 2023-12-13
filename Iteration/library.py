"""
Library
-------------------------------------------------------------
"""


class Book:
    def __init__(self, id, title, borrowers=[], copies=1):
        self.id = id
        self.title = title
        self.borrowers = borrowers
        self.copies = copies

    def __str__(self):
        return self.title


class Library:
    def __init__(self, books):
        self.books = books

    def show_all_books(self):
        print("In Our Library We Have The Following Books:")
        print("================================================")
        for book in self.books.values():
            print(book)
            print(str(book.id) + " --- Copies available: " + str(book.copies))

    def show_avail_books(self):
        print("Our Library Can Offer You The Following Books:")
        print("================================================")
        for book in self.books.values():
            if len(book.borrowers) == 0 or book.copies > 0:
                print(book)
                print(str(book.id) + " --- Copies available: " + str(book.copies))

    def lend_book(self, requested_book, name):
        if requested_book in self.books.keys():
            book = self.books[requested_book]
            if  book.copies > 0:
                print(f"{book.title} has been marked" f" as 'Borrowed' by: {name}")
                book.borrowers.append(name)
                book.copies -= 1
                return True
            else:
                print(
                    f"Sorry, the {book.title} is currently"
                    f" out of stock."
                )
                return False
        else:
            print(f"Sorry, book ID: {requested_book} is not present in our library.")
            return False

    def return_book(self, returned_book, name):
        book = self.books[returned_book]
        book.borrowers.remove(name)
        book.copies += 1
        print(f"Thanks for returning {book}")


class Student:
    def __init__(self, name, library):
        self.name = name
        self.books = []
        self.library = library

    def view_borrowed(self):
        if not self.books:
            print("You haven't borrowed any books")
        else:
            for book in self.books:
                print(book)

    def request_book(self):
        book_id = int(input("Enter the id of the book you'd like to borrow >> "))
        if self.library.lend_book(book_id, self.name):
            self.books.append(self.library.books[book_id])

    def return_book(self):
        book_id = int(input("Enter the id of the book you'd like to return >> "))
        if book_id not in self.library.books:
            print(f"Sorry, book ID: {book_id} is not present in our library.")
        else:
            book = self.library.books[book_id]
            if book in self.books:
                self.library.return_book(book_id, self.name)
                self.books.remove(self.library.books[book_id])
            else:
                print("You haven't borrowed that book, try another...")


def create_lib():
    books = {
        1 : Book(1, "The Last Battle", [], copies=5),
        2 : Book(2, "The Hunger Games", [], copies=5),
        3 : Book(3, "Cracking the Coding Interview", [], copies=5),
    }

    library = Library(books)
    student_name = input("Enter your name >> ")
    student_example = Student(student_name, library)

    while True:
        print(
            """
           ==========LIBRARY MENU===========
           1. Display All Books
           2. Display Available Books
           3. Borrow a Book
           4. Return a Book
           5. View Your Books
           6. Exit"""
        )

        choice = int(input("Enter Choice: "))
        if choice == 1:
            print()
            library.show_all_books()
        elif choice == 2:
            print()
            library.show_avail_books()
        elif choice == 3:
            print()
            student_example.request_book()
        elif choice == 4:
            print()
            student_example.return_book()
        elif choice == 5:
            print()
            student_example.view_borrowed()
        elif choice == 6:
            print("Goodbye")
            exit()


if __name__ == "__main__":
    create_lib()
