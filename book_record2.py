import redis

r = redis.Redis(decode_responses=True)

def add_book():
    book_id = r.incr('next_book_id')
    title = input("Enter book title:")
    author = input("Enter book author:")
    year = input("Enter year of publication:")

    book_key = f"book:{book_id}"
    r.hset(book_key, mapping={
        'title': title,
        'author': author,
        'year': year
    })

    print(f"\nBook successfully saved as :{book_key}")

def list_books():
    keys = r.keys('book:*')
    if not keys:
        print("No books found")
        return
    print("\nBooks in Redis:")
    for key in keys:
        book = r.hgetall(key)
        print(f"{key}:{book['title']} by {book['author']} ({book['year']})")

def view_book():
    book_id = input("Enter book ID to view:")
    book_key = f"book:{book_id}"
    if not r.exists(book_key):
        print("Book not found")
        return
    book = r.hgetall(book_key)
    print(f"\nDetails for {book_key}:")
    print(f"Title:{book['title']}")
    print(f"Author:{book['author']}")
    print(f"Year:{book['year']}")

def delete_book():
    book_id = input("Enter book ID to delte:")
    book_key = f"book:{book_id}"
    if r.delete(book_key):
        print(f"Book {book_key} deleted")
    else:
        print("Book not found")
    
if __name__ =="__main__":
    while True:
        print("\n==Book Manager==")
        print("1. Add new book")
        print("2. List all books")
        print("3. View book details")
        print("4. Delete book")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            add_book()
        elif choice == '2':
            list_books()
        elif choice == '3':
            view_book()
        if choice == '4':
            delete_book()
        if choice == '5':
            print("Have a good day")
            break
    