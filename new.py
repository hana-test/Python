
def random_func(name: str, age: int, weight: float) -> str:
    print("Name: ", name)
    print("Age: ", age)
    print("Weight: ", weight)
    
    return ("{} is {} years old and weight {}". format(name, age, weight))

print(random_func("Derek", 41, 165.6))
print(random_func(88, "Derek", "dark"))
print(random_func.__annotations__)
