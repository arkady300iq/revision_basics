import redis

r = redis.Redis(decode_responses=True)

book_id = r.incr('next_book_id')

title = input("Enter book title:")
author = input("Input book author:")
year = input("Input year of publication:")

book_key = f"book:{book_id}"
r.hset(book_key, mapping={
    'title': title,
    'author': author,
    'year': year
})

print(f"\nBook saved under a key:{book_key}")

book = r.hgetall(book_key)

print("\nBook info from Redis:")
print(f"\nBook title: {book['title']}")
print(f"Book author: {book['author']}")
print(f"Book year: {book['year']}")