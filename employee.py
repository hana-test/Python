import requests


class Employee:
    """A sample Employee class"""

    raise_amt = 1.05

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    def monthly_schedule(self, month):
        response = requests.get(f'http://company.com/{self.last}/{month}')
        if response.ok:
            return response.text
        else:
            return 'Bad Response ! '
        
emp_1 = Employee('John', 'Doe', 50000)
print(emp_1.fullname)  # Output: John Doe
print(emp_1.email)    # Output: John.Doe@email.com
print(emp_1.pay)      # Output: 50000

emp_1.apply_raise()
print(emp_1.pay)      # Output: 52500 (after 5% raise)

print(emp_1.monthly_schedule('January'))  # Retrieves schedule from the server