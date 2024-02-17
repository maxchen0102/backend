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

csv_file_path = 'dataSource\ogPeopleData.csv'

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
res = session.query(Test).filter(Test.records["性別"] == "女").all()

for row in res:
    print(row.id, end=" ")
    print(row.records["Seq"], end=" ")
    print(row.records["性別"], end=" ")
    print(row.records["級別"])
