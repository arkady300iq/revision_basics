import redis

r = redis.Redis(decode_responses=True)

def add_task(task):
    r.rpush('tasks', task)
    print(f"Added task: {task}")

def list_tasks():
    tasks = r.lrange('tasks', 0, -1)
    if not tasks:
        print("No tasks yet")
    else:
        print('Your tasks:')
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")


def delete_task(index):
    tasks = r.lrange('tasks',0,-1)
    if 0 <= index <len(tasks):
        task_to_remove = tasks[index]
        r.lrem('tasks', 1, task_to_remove)
        print(f"Removed task: {task_to_remove}")
    else:
        print("Invalid task number")

if __name__ == "__main__":
    while True:
        print("\n1. Add task\n2. List tasks\n3. Delete task\n4. Exit")
        choice = input("Choose an option:")

        if choice == '1':
            task = input("Enter your task:")
            add_task(task)

        elif choice == '2':
            list_tasks()

        elif choice == '3':
            list_tasks()
            num = int(input("Enter task number to delete:")) - 1
            delete_task(num)

        elif choice == '4':
            break
            
        else:
            print("invalid choice.\nPlease choose a number from 1 to 4:")