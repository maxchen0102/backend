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
from table4 import Post, User


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


post_data_obj={
    'post_title':'okok',
    'post_context':'qwec23123qwea',
    'Owner_id':1
}

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

query=session.query(User,Post).join(Post,User.id==Post.Owner_id).all()

for user, post in query:
    print("User:", user.id, user.author, user.author_email)
    print("Post:", post.post_id, post.post_title, post.post_context, post.Owner_id)


