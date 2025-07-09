import redis

r = redis.Redis(host='localhost', port=6379, db=0)

# r.set('foo', 'bar')
# value = r.get('foo')
# print(value)

# r.set('username', 'arkady')
# print(r.get('username').decode('utf-8'))

# r.set('page_views',0)
# r.incr('page_views')
# r.incrby('page_views', 5)
# print(r.get('page_views').decode('utf-8'))

# r.set('username', 'arkady')
# r.set('login','arkady_redozubov')
# r.set('password', '8903')
# username = r.get('username').decode('utf-8')
# login = r.get('login').decode('utf-8')
# password = int(r.get("password"))
# print(f"User's {username} login is {login} and password is {password} ")

# r.rpush('tasks','task1')
# r.rpush('tasks','task2')

# tasks = r.lrange('tasks', 0, -1)
# print([task.decode('utf-8') for task in tasks])

# task = r.lpop('tasks')
# print(task.decode('utf-8'))
