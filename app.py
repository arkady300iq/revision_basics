import redis

r = redis.Redis(host='localhost',port=6379, db=0, decode_responses=True)

if r.ping():
    print("Connected to Redis!")

r.hset('contact:1', mapping = {'name':'Arkady', 'phone_number':'0955505715'})
r.hset('profile:1', mapping= {'login':'arkady','password':'232323'})

contact = r.hgetall('contact:1')
profile = r.hgetall('profile:1')
print(contact)
print(profile)

r.hset('contact:1','phone_number', '987654321')
r.hset('profile:1','login','changed')

contact = r.hgetall('contact:1')
profile = r.hgetall('profile:1')
print(contact)
print(profile)

result = r.delete('contact:1')
print(result)
