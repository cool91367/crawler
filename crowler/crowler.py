# -*- coding: utf-8 -*-
import urllib.request as request
import requests
import bs4
import time
import random
from collections import defaultdict
from scrapy_splash import SplashRequest
from eyesmediapydb.mongo_base import MongoClientProvider
from eyesmediapydb.mongo_base import MongoConfig
from eyesmediapydb.__init__ import DefaultDBConfig

def changeFormData(page):
    formData = {
        "pageId": str(page),
        "pagesize": "20",
        "country": "11"
    }
    return formData

def replaceFormat(string):
    string = string.replace("→", "/")
    string = string.replace("-->", "/")
    string = string.replace("～", "/")
    string = string.replace("~", "/")
    string = string.replace("<br />", "/")
    return string



# setting my db collection
mongoConfig = MongoConfig(host="13.114.67.48", dbname="nlubot_dictionary", username="nlubot", password="28010606", port= 27017, replicaset=None)
mongoConfig.auth_mode = "SCRAM-SHA-1"
provider = MongoClientProvider(mongoConfig)
db = provider.create_client()
collection = db.dev_parse_source

url = "https://www.besttour.com.tw/api/query_List_all.asp"
detailUrl = "https://www.besttour.com.tw/api/travel_detail_schedule.asp?travel_no="
# pretend to be a real user
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36"
}

result = collection.find({}, {"item_id":1})
itemIdArray = []
for item in result:
    itemIdArray.append(item["item_id"])

# do
page = 1
response = requests.post(url, data=changeFormData(page), headers=header)
while page <= int(response.json()["pagecount"]):
    print(str(page) + "/" + response.json()["pagecount"])
    response = response.json()["data"]
    
    # start getting data
    for outline in response:
        # if collection.find_one({"item_id":outline["id"]}) == None:
        if outline["id"] not in itemIdArray:
            detailResponse = requests.get(detailUrl + outline["id"], headers=header).json()["data"]

            schedule = defaultdict()
            hashtag = []
            day = 1
            hashtag.append(outline["city"].split(" ")[0])# append 台灣 to hashTag

            # 拿出每日行程
            for data in detailResponse:
                schedule["第" + str(day) + "天"] = replaceFormat(data["abstract_1"])
                # print(schedule)
                for view in data["view"]:
                    hashtag.append(view["name"])
                day += 1

            # set item of collection and insert to db
            info = {
                "item_title":outline["name"],
                "hierarchy": ["台灣旅遊", outline["city"]],
                "item_specification":schedule,
                "item_id": outline["id"],
                "item_url": "https://www.besttour.com.tw/e_web/travel?v=" + outline["id"],
                "item_price": int(outline["price"]),
                "hashtag": hashtag,
                "article_source": "besttour",
                "node": "item"
            }
            collection.insert_one(info)

    time.sleep(random.randint(1, 3))
    page += 1
    response = requests.post(url, data=changeFormData(page), headers=header)
