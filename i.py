# LibraryManagement.py
class BookManagement:
    def add_book(self, book):
        print("Adding a book to the catalog.")

    def remove_book(self, book):
        print("Removing a book from the catalog.")

class BookSearch:
    def search_by_title(self, title):
        print(f"Searching for book by title: {title}")

    def search_by_author(self, author):
        print(f"Searching for book by author: {author}")

class BookBorrowing:
    def borrow_book(self, book, user):
        print(f"Borrowing book for user: {user}")

    def return_book(self, book, user):
        print(f"Returning book for user: {user}")

# main function
def main():
    search = BookSearch()
    search.search_by_title("The Great Gatsby")

if __name__ == "__main__":
    main()
