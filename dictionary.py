#Dictionaries are fundamental data structures in Python, offering versatile organization and retrieval of data.
# Mastering them is essential for effective Python programming.

person = {'name': 'John', 'age': 30, 'city': 'New York', 'skills': ['Python', 'JavaScript']}

print(person['name'])  # Output: John
print(person.get('email', 'Not found'))  # Output: Not found
person['email'] = 'john@example.com'
print(person.keys())  # Output: dict_keys(['name', 'age', 'city', 'skills', 'email'])
for key, value in person.items():
    print(f"{key}: {value}")