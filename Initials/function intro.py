def greet():
    print("hello world \nWelcome!")

greet()


def greets(f_name,l_name):
    print(f"hello {f_name} {l_name}")
    print("Welcome")

greets("Michel","Danny")
greets("Prakash","Thapa")
greets("Taka","Noboru")

input=("enter greeting: ")
def greets(f_name,l_name, greeting):
    print(f"{greeting} {f_name} {l_name}")
    print("Welcome")

greets("Michel","Danny","namaste,")
greets("Prakash","Thapa","Jhorle,")
greets("Taka","Noboru", "konichiwa,")


def get_greeting(name):
    return f"hi {"name"}"

message = get_greeting("john")
print(message)
