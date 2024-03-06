from table2 import create_session
from table2 import AllData
from table3 import Data
from table_csv import DataCsv
from table_json import Test

import requests
import json
from datetime import datetime
from pprint import pprint
import  csv 
from order import Order,Product


# # Open the CSV file and read its contents
# with open("dataSource\ogPeopleData.json", "rb") as f:
#     data = json.load(f)
#     pprint(data[0]["result"]["records"])

#     session = create_session()

#     for row in data[0]["result"]["records"]: 
#         data_obj={"records":row} 
#         session.add(Test(**data_obj))
#         session.commit()
#     session.close()
# print("done")

session = create_session()

# Assuming you have already defined your Product class, session, and engine

# Create a dictionary containing product information
product_info = {
    'name': "TOYOTA",
    'price': 1239000
}
# Create a Product instance using the product_info dictionary
product_1 = Product(**product_info)
# Add the product instance to the session
session.add(product_1)
# Commit the transaction to save the changes to the database
session.commit()
# Close the session
session.close()


# user_data_obj={
#     'author':"max", 
#     'author_email':'king123@gmail.com',
#     'author_password':'123asqwe'
# }


# user1=User(**user_data_obj)
# print(user1.id)
# session.add(user1) 
# session.commit()
# session.close()

# post_data_obj={
#     'post_title':'okok',
#     'post_context':'qwec23123qwea',
#     'Owner_id':1
# }

# post1=Post(**post_data_obj)
# session.add(post1)
# session.commit()
# session.close()

# # 查询所有用户
# users = session.query(User).all()
# for user in users:
#     print(user.id, user.author, user.author_email)

# # 查询所有帖子
# posts = session.query(Post).all()
# for post in posts:
#     print(post.post_id, post.post_title, post.post_context, post.Owner_id)

# # 关闭会话
# session.close()


# res=session.query(Post).all()

# for item in res : 
#     print(item.user.author)


# res = session.query(Post, User).join(Post, Post.Owner_id == User.id).all()

# for post,user in res:
#     print(post.post_id,end=" ")
#     print(post.post_title,end=" ")
#     print(post.post_context,end=" ")
#     print(post.Owner_id,end=" ")
#     print(user.id,end=" ")
#     print(user.author,end=" ")
#     print(user.author_email,end=" ")
#     print(user.author_password,end=" ")



# session=create_session()

# session.add(Parent())
# session.commit()

# data_obj={
#     'child_name':'kariew', 
#     'illness':0,
#     'parent_id':1 
# }

# session.add(Child(**data_obj))
# session.commit()

# pareant=Parent()
# session.add(pareant)
# session.commit()
