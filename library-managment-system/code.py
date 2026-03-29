class Book:
    def __init__(self, book_id, title, author, isbn, copies=1):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.isbn = isbn
        self.copies = copies
        self.available = copies

    def __str__(self):
        return f"{self.book_id}: {self.title} by {self.author} (Available: {self.available})"

class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []  # list of (book_id, due_date)

class LibrarySystem:
    def __init__(self):
        self.books = {}
        self.members = {}
        self.next_book_id = 1
        self.next_member_id = 1

    def add_book(self, title, author, isbn, copies=1):
        book = Book(self.next_book_id, title, author, isbn, copies)
        self.books[self.next_book_id] = book
        self.next_book_id += 1
        print(f"Book added: {book}")

    def search_book(self, keyword):
        results = [book for book in self.books.values() if keyword.lower() in book.title.lower() or keyword.lower() in book.author.lower()]
        return results

    def register_member(self, name):
        member = Member(self.next_member_id, name)
        self.members[self.next_member_id] = member
        self.next_member_id += 1
        print(f"Member registered: {name} (ID: {member.member_id})")
        return member.member_id

    def issue_book(self, member_id, book_id):
        if member_id not in self.members or book_id not in self.books:
            print("Invalid member or book ID")
            return False
        book = self.books[book_id]
        if book.available > 0:
            book.available -= 1
            self.members[member_id].borrowed_books.append((book_id, "2026-04-30"))  # example due date
            print(f"Book {book_id} issued to member {member_id}")
            return True
        print("Book not available")
        return False

    def return_book(self, member_id, book_id):
        if member_id not in self.members or book_id not in self.books:
            print("Invalid ID")
            return False
        member = self.members[member_id]
        for i, (b_id, _) in enumerate(member.borrowed_books):
            if b_id == book_id:
                del member.borrowed_books[i]
                self.books[book_id].available += 1
                print(f"Book {book_id} returned successfully")
                return True
        print("Book not borrowed by this member")
        return False

    def generate_overdue_report(self):
        print("Overdue Report (Sample - implement date check in real system)")
        for mem_id, mem in self.members.items():
            if mem.borrowed_books:
                print(f"Member {mem_id}: {len(mem.borrowed_books)} books borrowed")

# Demo
if __name__ == "__main__":
    lib = LibrarySystem()
    lib.add_book("Python Programming", "Guido van Rossum", "123456", 5)
    lib.add_book("Data Structures", "Mark Weiss", "789012", 3)
    lib.register_member("Alice")
    lib.issue_book(1, 1)
    lib.return_book(1, 1)
    print("\nSearch Results:", [str(b) for b in lib.search_book("Python")])
    lib.generate_overdue_report()