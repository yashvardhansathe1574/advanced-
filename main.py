from book import Book
from user import User
# ===============================
# Transaction Class
# ===============================
class Transaction:

    def __init__(self):
        self.users = []
        self.books = []

    # --------------------------
    # Add User
    # --------------------------
    def add_user(self):

        user_id = input("Enter User ID : ")
        name = input("Enter Name : ")
        email = input("Enter Email : ")

        user = User(user_id, name, email)

        self.users.append(user)

        print("\nUser Added Successfully\n")

    # --------------------------
    # Add Book
    # --------------------------
    def add_book(self):

        book_id = input("Enter Book ID : ")
        title = input("Enter Book Title : ")
        author = input("Enter Author Name : ")

        book = Book(book_id, title, author)

        self.books.append(book)

        print("\nBook Added Successfully\n")

    # --------------------------
    # Display Users
    # --------------------------
    def show_users(self):

        if len(self.users) == 0:
            print("No Users Found\n")
            return

        for user in self.users:
            user.display()

    # --------------------------
    # Display Books
    # --------------------------
    def show_books(self):

        if len(self.books) == 0:
            print("No Books Available\n")
            return

        for book in self.books:
            book.display()

    # --------------------------
    # Search Book
    # --------------------------
    def search_book(self):

        title = input("Enter Book Title : ")

        found = False

        for book in self.books:

            if book.title.lower() == title.lower():
                book.display()
                found = True

        if not found:
            print("Book Not Found\n")

    # --------------------------
    # Issue Book
    # --------------------------
    def issue_book(self):

        book_id = input("Enter Book ID : ")

        for book in self.books:

            if book.book_id == book_id:

                if book.available:
                    book.available = False
                    print("Book Issued Successfully\n")
                else:
                    print("Book Already Issued\n")

                return

        print("Book Not Found\n")

    # --------------------------
    # Return Book
    # --------------------------
    def return_book(self):

        book_id = input("Enter Book ID : ")

        for book in self.books:

            if book.book_id == book_id:

                if not book.available:
                    book.available = True
                    print("Book Returned Successfully\n")
                else:
                    print("Book is Already Available\n")

                return

        print("Book Not Found\n")


# ===============================
# Main Program
# ===============================
if __name__ == "__main__":

    library = Transaction()

    while True:

        print("\n========== Library Management ==========")
        print("1. Add User")
        print("2. Add Book")
        print("3. Show Users")
        print("4. Show Books")
        print("5. Search Book")
        print("6. Issue Book")
        print("7. Return Book")
        print("8. Exit")

        choice = input("Enter Choice : ")

        if choice == "1":
            library.add_user()

        elif choice == "2":
            library.add_book()

        elif choice == "3":
            library.show_users()

        elif choice == "4":
            library.show_books()

        elif choice == "5":
            library.search_book()

        elif choice == "6":
            library.issue_book()

        elif choice == "7":
            library.return_book()

        elif choice == "8":
            print("Thank You...")
            break

        else:
            print("Invalid Choice")