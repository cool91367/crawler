# -*- coding: utf-8 -*-
import pandas as pd
import time
import requests
from parse_function import parse_url
import random

file = "parse_data.xlsx"
xlsx = pd.ExcelFile(file)

# 抓取所有news_id 和 url
result_dict = {}
sheet = xlsx.sheet_names[0]
datas = result_dict.get(sheet)
if not datas:
    datas = []
    result_dict.setdefault(sheet, datas)
# read rows
df = xlsx.parse(sheet)
df = df.fillna('')
print("{}: x:{}, y:{}".format(sheet, df.index, df.columns))
session = requests.Session()
for x in df.index:
    d = []
    d.append(df.iloc[x][0])
    d.append(df.iloc[x][1])
    d.append(df.iloc[x][2])
    if df.iloc[x][3] is not '':
        d.append(df.iloc[x][3])
    else:
        # if x<20:
        content_data = parse_url(df.iloc[x][1], session=session)
        if content_data !='':
            d.append(content_data)
            time.sleep(random.randint(3, 5))
        else:
            d.append('')
    datas.append(d)
result_dict.update({"data":datas})

df = pd.DataFrame(result_dict['data'],columns=['news_id', 'url','content','real_content'])
df.to_excel("parse_data.xlsx", sheet_name='data', index=False)

