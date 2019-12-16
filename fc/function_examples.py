"""Function Examples."""


def say_hi():
    """Greeting function."""
    print("Hello User")


def greeting(name):
    """Example with passed in parameter."""
    print("Hello " + name)


def hello_age(name, age):
    """Example with two parameters."""
    age = str(age)
    print("Hello " + name + ". You are " + age + " years old.")


def cube(num):
    """Example of function with a return."""
    return(num * num * num)


say_hi()
greeting("JenMo")
hello_age("Salem", 43)

result = (cube(40))
print(result)
