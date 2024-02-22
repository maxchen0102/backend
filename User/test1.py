people_list = [
    {"name": "Alice", "age": 30,"status":1},
    {"name": "Bob", "age": 25,"status":0},
    {"name": "Charlie", "age": 35 ,"status":1}
]

# 使用字典推导式将列表转换为字典
people_dict = {person["name"]: person["age"] for person in people_list if person["status"]}

print(people_dict)
