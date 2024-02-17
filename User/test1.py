
class Table: 
    def __init__(self, name, age):
        self.name = name
        self.age = age

my_data={'name':'chris','age':100}


table=Table(**my_data)

print(table.name)
print(table.age)

