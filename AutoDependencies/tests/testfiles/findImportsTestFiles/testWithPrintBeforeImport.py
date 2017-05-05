
def func():
    print("There's an import after this print"); import random 
    print(random.randint(1,10))

func()