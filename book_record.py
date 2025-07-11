import redis

r = redis.Redis(decode_responses=True)

title = input("Enter book title:")
author = input("Input book author:")
year = input("Input year of publication:")

r.hset('book:1',mapping={
    'title': title,
    'author': author,
    'year': year
})

print("\nData successfully saved in Redis\n")

book = r.hgetall('book:1')

print("Book info from Redis:")
print(f"\nBook title: {book['title']}")
print(f"Book author: {book['author']}")
print(f"Book year: {book['year']}")