from table2 import create_session
from table2 import AllData
import requests
import json
from datetime import datetime

url = "https://sme.moeasmea.gov.tw/startup/upload/opendata/gov_infopack_opendata.json"
res = requests.get(url)
datas = json.loads(res.text)

session = create_session()


for item in datas:
    data_obj = {
        "title": item["標題"],
        "content": item["內容"],
        "picture": item["主圖"],
        "category": item["分類"],
        "youtube": item["youtube嵌入代碼"],
        "slideshare": item["slideshare嵌入代碼"],
        "publish_time": datetime.strptime(item["建立時間"], "%Y%m%d%H%M%S"),
        "update_time": datetime.strptime(item["修改時間"], "%Y%m%d%H%M%S")
    }
    session = create_session()

    session.add(AllData(**data_obj))

    session.commit()
    session.close()