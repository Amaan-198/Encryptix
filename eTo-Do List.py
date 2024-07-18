tasks=[]

def view_task():
    if len(tasks)==0:
        print()
        print("===================")
        print("No tasks available.")
    else:
        for index, task in enumerate(tasks, start=1):
            status="✓" if task["completed"] else "✗"
            print(f"{index}. {task['task']} [{status}]")

def add_task(task):
    tasks.append({"task":task, "completed":False})

def change(index):
    tasks[index-1]["completed"]=not tasks[index-1]["completed"]

def delete(index):
    tasks.remove(tasks[index-1])

while True:
    print()
    print("=======To-do List=======")
    print("1.View Tasks.\n2.Add Task\n3.Mark as done.\n4.Mark as not done.\n5.Delete Task.\n6.Exit.")
    choice=int(input("\nEnter choice(1-6): "))
    if choice==1:
        view_task()
    if choice==2:
        a=input("Enter the task: ")
        add_task(a)
        print("\nTask added, here is the updated list:")
        print("\n=========")
        view_task()
        print("=========")
    if choice==3 or choice==4:
        a=int(input("Enter task number to update: "))
        change(a)
        print("\nUpdated list:")
        print("\n=========")
        view_task()
        print("=========")
    if choice==5:
        a=int(input("Enter task number to delete: "))
        delete(a)
        print("\nDeleted successfully, updated list:")
        print("\n=========")
        view_task()
        print("=========")
    if choice==6:
        break
        
