import redis

r = redis.Redis(decode_responses=True)

name = input("Enter your name:")
age = input("Enter your age:")
city = input("Enter your city:")

r.hset('user:1', mapping={
    'name': name,
    'age': age,
    'city': city
})

print("\nSuccessfully saved to Redis")

user = r.hgetall('user:1')

print("\nData from Redis:")
print(f"Name:{user['name']}")
print(f"Age:{user['age']}")
print(f"City:{user['city']}")