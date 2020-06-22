# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests
import pandas as pd
import sys, os

def parse_url(url, session, file=None):
    headers ={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1 Safari/605.1.15",
                "Accept-Language": "zh-tw",
                "Accept-Encoding": "gzip, deflate, br",
                "Connection": "keep-alive"}
    try:
        # session = None
        content = ''
        if not file:
            if "cnyes.com" in url:
                content = cnyes(url, file=file, session=session, headers=headers)
            if "udn.com" in url:
                content = udn(url, file=file, session=session, headers=headers)
            if "ctee.com" in url:
                content = ctee(url, file=file, session=session, headers=headers)
            if "mirrormedia.mg" in url:
                content = mirrormedia(url, file=file, session=session, headers=headers)
            if "judicial.gov" in url:
                content = judicial(url, file=file, session=session, headers=headers)
            if "coolloud.org" in url:
                content = coolloud(url, file=file, session=session, headers=headers)
            if "chinatimes.com" in url:
                content = chinatimes(url, file=file, session=session, headers=headers)
            if "mops.twse.com" in url:
                content = twse(url, file=file, session=session, headers=headers)
            if "hk01" in url:
                content = hk01(url, file=file, session=session, headers=headers)
            if "mingpao.com" in url:
                content = mingpao(url, file=file)
            if "ltn" in url:
                content = ltn(url, file=file, session=session, headers=headers)
            if "businesstoday.com" in url:
                content = businesstoday(url, file=file, session=session, headers=headers)
            if "tvbs.com" in url:
                content = tvbs(url, file=file, session=session, headers=headers)
            if "wealth.com" in url:
                content = wealth(url, file=file, session=session, headers=headers)
            if "bnext.com" in url:
                content = bnext(url, file=file, session=session, headers=headers)
            if "ettoday.net" in url:
                content = ettoday(url, file=file, session=session, headers=headers)
            if "hk.on" in url:
                content = hk_on(url, file=file, session=session, headers=headers)
            if "sina.com" in url:
                content = sina(url, file=file, session=session, headers=headers)
            if "technews.tw" in url:
                content = technews(url, file=file, session=session, headers=headers)
            if "news.yahoo" in url:
                content = yahoonews(url, file=file, session=session, headers=headers)
            if "cw.com" in url:
                content = cw(url, file=file, session=session, headers=headers)
            if "ebc.net" in url:
                content = ebc(url, file=file, session=session, headers=headers)
            if "fsc.gov" in url:
                content = fsc(url, file=file, session=session, headers=headers)
            if "setn.com" in url:
                content = setn(url, file=file, session=session, headers=headers)
            if "managertoday.com" in url:
                content = managertoday(url, file=file, session=session, headers=headers)
            if "hbrtaiwan.com" in url:
                content = hbrtaiwan(url, file=file, session=session, headers=headers)
            if "cna.com" in url:
                content = cna(url, file=file, session=session, headers=headers)
            if "nextmag.com" in url:
                content = nextmgz(url, file=file, session=session, headers=headers)
        else:
            content = nextmgz(url, file=file, session=session, headers=headers)
        return content
    except Exception as e:
        print(e)
        return ''


def cnyes(url, file, session, headers):
    print("cnyes %s"%url)
    content = ""
    try:
        if file:
            with open(file) as e:
                soup = BeautifulSoup(e.read(), 'html.parser')
                # print(soup.prettify())
        else:
            response = session.get(url, headers=headers)
            soup = BeautifulSoup(response.text, 'html.parser')
        # 分類
        classification = soup.find_all("span", itemprop="name")[:2]
        # 標題
        headline = soup.find_all("h1", itemprop="headline")
        # pic_desc = soup.find_all("figcaption", itemprop="caption")
        # 內文
        article = soup.find_all(itemprop="articleBody")
        if len(classification)>0:
            for i in classification:
                content+=i.text
        if len(headline)>0:
            title = headline[0].text
            content+=title
        for i in article[0].find_all("figure"):
            i.decompose()
        for i in article[0].find_all(["h6","p"]):
            content+=i.text
        return content
    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print("%s, %s, in line %s"%(exc_type, fname, exc_tb.tb_lineno))
        print("cnyes 404, %s"%e)
        return '404'

def udn(url, file, session, headers):
    print("udn %s"%url)
    content = ""
    try:
        if file:
            with open(file) as e:
                soup = BeautifulSoup(e.read(), 'html.parser')
                # print(soup.prettify())
        else:
            response = session.get(url, headers=headers)
            soup = BeautifulSoup(response.text, 'html.parser')
        article = soup.find_all("article", class_="article-content")
        # print(article)
        for i in article[0].find_all("figcaption"):
            i.decompose()
        for i in article[0].find_all(["p"]):
            content+=i.text.replace("\n","")
        return content
    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print("%s, %s, %s, in line %s"%(exc_type, e, fname, exc_tb.tb_lineno))
        print("udn %s"%e)
        return '404'

def ctee(url, file, session, headers):
    print("ctee %s"%url)
    content = ""
    try:
        if file:
            with open(file) as e:
                soup = BeautifulSoup(e.read(), 'html.parser')
                # print(soup.prettify())
        else:
            response = session.get(url, headers=headers)
            soup = BeautifulSoup(response.text, 'html.parser')
        article = soup.find_all("div", class_="entry-content")
        # print(article)
        for i in article[0].find_all("img"):
            i.decompose()
        for i in article[0].find_all(["p"]):
            content+=i.text.replace("\n","")
        return content
    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print("%s, %s, in line %s"%(exc_type, fname, exc_tb.tb_lineno))
        print("ctee %s"%e)
        return '404'

def mirrormedia(url, file, session, headers):
    print("mirrormedia %s"%url)
    content = ""
    try:
        if file:
            with open(file) as e:
                soup = BeautifulSoup(e.read(), 'html.parser')
                # print(soup.prettify())
        else:
            response = session.get(url, headers=headers)
            soup = BeautifulSoup(response.text, 'html.parser')
        # 找到文本 main
        article = soup.find_all("main", class_="article_main")
        
        # 刪除不重要的大面板
        for i in article[0].find_all("div", class_="article__audioplayer-share"):
            i.decompose()
        for i in article[0].find_all("div", class_="article_main_tags"):
            i.decompose()
        
        # 需要最後放入的做細微調整
        update_time = article[0].find_all("p", class_="updated-time")
        if update_time:
            time_ = None
            for i in update_time[0].find_all("span"):
                time_ = i.text
                i.decompose()
            update_time = update_time[0].text
            for i in article[0].find_all("p", class_="updated-time"):
                i.decompose()
        
        # 依序放入content
        for i in article[0].find_all(["h1","p"]):
            content+=i.text.replace("\t","").replace("\n","")
        
        # 將細微調整放入content
        if update_time:
            content+=update_time.replace("\n","").replace("\t","").replace(" ","")+time_

        return content
    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print("%s, %s, in line %s"%(exc_type, fname, exc_tb.tb_lineno))
        print("mirrormedia %s"%e)
        return '404'

def judicial(url, file, session, headers):
    print("judicial %s"%url)
    content = ""
    try:
        if file:
            with open(file) as e:
                soup = BeautifulSoup(e.read(), 'html.parser')
                # print(soup.prettify())
        else:
            response = session.get(url, headers=headers)
            soup = BeautifulSoup(response.text, 'html.parser')
        # 找到文本 main
        article = soup.find_all("form")
        
        # 刪除不重要的大面板
        for i in article[0].find_all("font"):
            i.decompose()
        
        # 依序放入content
        for i in article[0].find_all(["table"]):
            content+=i.text.replace("\t","").replace("\n","").replace(" ","").replace("　","").strip()
        
        return content
    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print("%s, %s, in line %s"%(exc_type, fname, exc_tb.tb_lineno))
        print("judicial %s"%e)
        return '404'

def coolloud(url, file, session, headers):
    print("coolloud %s"%url)
    content = ""
    try:
        if file:
            with open(file) as e:
                soup = BeautifulSoup(e.read(), 'html.parser')
                # print(soup.prettify())
        else:
            response = session.get(url, headers=headers)
            soup = BeautifulSoup(response.text, 'html.parser')
        # 找到文本 main
        article = soup.find_all("article")

        # 刪除不重要的大面板
        table = article[0].find_all("table")
        if table:
            for i in table[0].find_all("p"):
                i.decompose()
        # 依序放入content
        for i in article[0].find_all(["p"]):
            content+=i.text.replace("\t","").replace("\n","").replace(" ","").replace("　","").strip()
        
        return content
    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print("%s, %s, in line %s"%(exc_type, fname, exc_tb.tb_lineno))
        print("coolloud %s"%e)
        return '404'

def chinatimes(url, file, session, headers):
    print("chinatimes %s"%url)
    content = ""
    try:
        if file:
            with open(file) as e:
                soup = BeautifulSoup(e.read(), 'html.parser')
                # print(soup.prettify())
        else:
            response = session.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
        # 找到文本 main

        article = soup.find_all("div", class_="article-body")

        # 刪除不重要的大面板
        comments = article[0].find_all("section", id="comments")
        if comments:
            for i in comments[0].find_all(["div","p"]):
                i.decompose()

        # 依序放入content
        for i in article[0].find_all(["p"]):
            content+=i.text.replace("\t","").replace("\n","").replace(" ","").replace("　","").strip()
        
        return content
    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print("%s, %s, in line %s"%(exc_type, fname, exc_tb.tb_lineno))
        print("chinatimes %s"%e)
        return '404'

def twse(url, file, session, headers):
    print("twse %s"%url)
    content = ""
    try:
        if file:
            with open(file) as e:
                soup = BeautifulSoup(e.read(), 'html.parser')
                # print(soup.prettify())
        else:
            response = session.get(url, headers=headers)
            soup = BeautifulSoup(response.text, 'html.parser')
        # 找到文本 main
        article = soup.find_all("div", id="table01")

        # 依序放入content
        for i in article[0].find_all(["b","td","pre"]):
            content+=i.text.replace("\t","").replace("\n","").replace(" ","").replace("　","").strip()
        if len(content) ==0:
            content = "404"
        return content
    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print("%s, %s, in line %s"%(exc_type, fname, exc_tb.tb_lineno))
        print("twse %s"%e)
        return '404'

def hk01(url, file, session, headers):
    print("hk01 %s"%url)
    content = ""
    try:
        if file:
            with open(file) as e:
                soup = BeautifulSoup(e.read(), 'html.parser')
                # print(soup.prettify())
        else:
            response = session.get(url, headers=headers)
            soup = BeautifulSoup(response.text, 'html.parser')
        article = soup.find_all("article")
        # print(article)
        # for i in article[0].find_all("p", fontsizelevel="medium"):
        #     print(i.text)
        #     i.decompose()
        for i in article[0].find_all(["p"]):
            content+=i.text.replace("\t","").replace("\n","").replace(" ","").replace("　","").strip()
        return content
    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print("%s, %s, in line %s"%(exc_type, fname, exc_tb.tb_lineno))
        print("hk01 %s"%e)
        return '404'

def mingpao(url, file):
    print("mingpao %s"%url)
    session = requests.Session()
    headers ={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1 Safari/605.1.15",
                # "Accept-Language": "zh-tw",
                "Accept-Encoding": "gzip, deflate, br",
                "Connection": "keep-alive"}
    content = ""
    try:
        if file:
            with open(file) as e:
                soup = BeautifulSoup(e.read(), 'html.parser')
                # print(soup.prettify())
        else:
            response = session.get(url, headers=headers)
            soup = BeautifulSoup(response.text, 'html.parser')
        article = soup.find_all("article")
        for i in article[0].find_all("a"):
            i.decompose()
        for i in article[0].find_all(["p","h2"]):
            if "相關字詞﹕" in i.text:
                continue
            content+=i.text.replace("\n","").replace(" ","")
        session.close()
        if "" in content:
            content = ""
            response = session.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            article = soup.find_all("article")
            for i in article[0].find_all("a"):
                i.decompose()
            for i in article[0].find_all(["p","h2"]):
                if "相關字詞﹕" in i.text:
                    continue
                content+=i.text.replace("\n","").replace(" ","")
        print(content)
        if "" in content:
            return ""
        return content
    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print("%s, %s, %s, in line %s"%(exc_type, e, fname, exc_tb.tb_lineno))
        print("mingpao %s"%e)
        session.close()
        return '404'

def ltn(url, file, session, headers):
    print("ltn %s"%url)
    content = ""
    try:
        if file:
            with open(file) as e:
                soup = BeautifulSoup(e.read(), 'html.parser')
                # print(soup.prettify())
        else:
            response = session.get(url, headers=headers)
            soup = BeautifulSoup(response.text, 'html.parser')
        article = soup.find_all("div", itemprop="articleBody")
        for i in article[0].find_all("div", class_="photo boxTitle"):
            i.decompose()
        for i in article[0].find_all("p", class_="appE1121"):
            i.decompose()

        for i in article[0].find_all(["p","h1"]):
            content+=i.text.replace("\n","").replace(" ","")
        return content
    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print("%s, %s, %s, in line %s"%(exc_type, e, fname, exc_tb.tb_lineno))
        print("ltn %s"%e)
        return '404'

def businesstoday(url, file, session, headers):
    print("businesstoday %s"%url)
    content = ""
    try:
        if file:
            with open(file) as e:
                soup = BeautifulSoup(e.read(), 'html.parser')
                # print(soup.prettify())
        else:
            response = session.get(url, headers=headers)
            soup = BeautifulSoup(response.text, 'html.parser')
        article = soup.find_all("div", itemprop="articleBody")
        # for i in article[0].find_all("div", class_="photo boxTitle"):
            # i.decompose()
        # for i in article[0].find_all("p", class_="appE1121"):
            # i.decompose()

        for i in article[0].find_all(["p","h1"]):
            content+=i.text.replace("\n","").replace(" ","").replace(" ","")
        return content
    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print("%s, %s, %s, in line %s"%(exc_type, e, fname, exc_tb.tb_lineno))
        print("businesstoday %s"%e)
        return '404'

def tvbs(url, file, session, headers):
    print("tvbs %s"%url)
    content = ""
    try:
        if file:
            with open(file) as e:
                soup = BeautifulSoup(e.read(), 'html.parser')
                # print(soup.prettify())
        else:
            response = session.get(url, headers=headers)
            soup = BeautifulSoup(response.text, 'html.parser')
        article = soup.find_all("div", class_="newsdetail_content")
        for i in article[0].find_all("span"):
            i.decompose()
        # for i in article[0].find_all("p", class_="appE1121"):
            # i.decompose()

        for i in article[0].find_all(["p","h1"]):
            content+=i.text.replace("\n","").replace(" ","").replace(" ","")
        return content
    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print("%s, %s, %s, in line %s"%(exc_type, e, fname, exc_tb.tb_lineno))
        print("tvbs %s"%e)
        return '404'

def wealth(url, file, session, headers):
    print("wealth %s"%url)
    content = ""
    try:
        if file:
            with open(file) as e:
                soup = BeautifulSoup(e.read(), 'html.parser')
                # print(soup.prettify())
        else:
            response = session.get(url, headers=headers)
            soup = BeautifulSoup(response.text, 'html.parser')
        article = soup.find_all("div", itemprop="articleBody")
        # for i in article[0].find_all("span"):
        #     i.decompose()
        img = article[0].find_all("p", class_="main-img-intro")
        if img:
            for i in img:
                i.decompose()

        for i in article[0].find_all(["p","h1"]):
            content+=i.text.replace("\n","").replace(" ","").replace(" ","")
        return content
    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print("%s, %s, %s, in line %s"%(exc_type, e, fname, exc_tb.tb_lineno))
        print("wealth %s"%e)
        return '404'

def bnext(url, file, session, headers):
    print("bnext %s"%url)
    content = ""
    try:
        if file:
            with open(file) as e:
                soup = BeautifulSoup(e.read(), 'html.parser')
                # print(soup.prettify())
        else:
            response = session.get(url, headers=headers)
            soup = BeautifulSoup(response.text, 'html.parser')

        article = soup.find("script", type="application/ld+json")

        import json
        try:
            data = list(article)[0].replace("//","")
            data = json.loads(data)
            content+=data.get("description").replace("\n","").replace(" ","").replace(" ","")
            content+=data.get("articleBody").replace("\n","").replace(" ","").replace(" ","")
        except:
            return "404"
        return content
    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print("%s, %s, %s, in line %s"%(exc_type, e, fname, exc_tb.tb_lineno))
        print("bnext %s"%e)
        return '404'

def ettoday(url, file, session, headers):
    print("ettoday %s"%url)
    content = ""
    try:
        if file:
            with open(file) as e:
                soup = BeautifulSoup(e.read(), 'html.parser')
                # print(soup.prettify())
        else:
            response = session.get(url, headers=headers)
            soup = BeautifulSoup(response.text, 'html.parser')
        article = soup.find_all("article")
        # for i in article[0].find_all("span"):
        #     i.decompose()
        img = article[0].find_all("p", class_="center")
        if img:
            for i in img:
                i.decompose()

        for i in article[0].find_all(["p"]):
            if "【更多新聞】" in i.text:
                break
            content+=i.text.replace("\n","").replace(" ","").replace(" ","")
        return content
    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print("%s, %s, %s, in line %s"%(exc_type, e, fname, exc_tb.tb_lineno))
        print("ettoday %s"%e)
        return '404'

def hk_on(url, file, session, headers):
    headers ={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1 Safari/605.1.15",
                "Accept-Language": "zh-tw",
                "Accept-Encoding": "gzip, deflate, br",
                "Connection": "keep-alive",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"}
    print("hk_on %s"%url)
    content = ""
    try:
        if file:
            with open(file) as e:
                soup = BeautifulSoup(e.read(), 'html.parser')
                # print(soup.prettify())
        else:
            response = session.get(url)
            response.encoding="utf-8"
            soup = BeautifulSoup(response.text, 'html.parser')
        article = soup.find_all("div", class_="news_content")
        # for i in article[0].find_all("span"):
        #     i.decompose()
        img = article[0].find_all("div", class_="photoCaption")
        if img:
            for i in img:
                i.decompose()
        toolbar = article[0].find_all("div", class_="toolBar")
        if toolbar:
            for i in toolbar:
                i.decompose()
        bot = article[0].find_all("div", id="page_right_fixed_CTN")
        if bot:
            for i in bot:
                i.decompose()
        contentfeature = article[0].find_all("div", class_="contentFeature")
        if contentfeature:
            for i in contentfeature:
                i.decompose()

        for i in article[0].find_all(["div"]):
            if "【更多新聞】" in i.text:
                break
            content+=i.text.replace("\n","").replace(" ","").replace("　","").replace("\t","")
        return content
    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print("%s, %s, %s, in line %s"%(exc_type, e, fname, exc_tb.tb_lineno))
        print("hk_on %s"%e)
        return '404'

def sina(url, file, session, headers):
    print("sina %s"%url)
    content = ""
    try:
        if file:
            with open(file) as e:
                soup = BeautifulSoup(e.read(), 'html.parser')
                # print(soup.prettify())
        else:
            response = session.get(url, headers=headers)
            soup = BeautifulSoup(response.text, 'html.parser')
        article = soup.find_all("div", id="news-main-body")
        # for i in article[0].find_all("span"):
        #     i.decompose()
        img = article[0].find_all("div", class_="news-keyword")
        if img:
            for i in img:
                i.decompose()
        for i in article[0].find_all("p"):
            # print(i.text.replace("\n","").replace(" ","").replace(" ",""))
            if i.text.replace("\n","").replace(" ","").replace(" ","") in content:
                continue
            content+=i.text.replace("\n","").replace(" ","").replace(" ","")
        return content
    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print("%s, %s, %s, in line %s"%(exc_type, e, fname, exc_tb.tb_lineno))
        print("sina %s"%e)
        return '404'

def technews(url, file, session, headers):
    print("technews %s"%url)
    content = ""
    try:
        if file:
            with open(file) as e:
                soup = BeautifulSoup(e.read(), 'html.parser')
                # print(soup.prettify())
        else:
            response = session.get(url, headers=headers)
            soup = BeautifulSoup(response.text, 'html.parser')
        # 找到文本 main
        figure = soup.find_all("figure")
        if figure:
            for i in soup.find_all(["figure"]):
                i.decompose()
        article = soup.find_all("div", class_="indent")
        footer = soup.find_all("footer")
        if footer:
            for i in soup.find_all(["footer"]):
                i.decompose()
        # 刪除不重要的大面板

        # 依序放入content
        for i in soup.find_all(["p"]):
            content+=i.text.replace("\t","").replace("\n","").replace(" ","").replace("　","").strip()
        
        return content
    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print("%s, %s, in line %s"%(exc_type, fname, exc_tb.tb_lineno))
        print("technews %s"%e)
        return '404'

def yahoonews(url, file, session, headers):
    print("yahoonews %s"%url)
    content = ""
    try:
        if file:
            with open(file) as e:
                soup = BeautifulSoup(e.read(), 'html.parser')
                # print(soup.prettify())
        else:
            response = session.get(url, headers=headers)
            soup = BeautifulSoup(response.text, 'html.parser')
        article = soup.find_all("article", itemprop="articleBody")
        # for i in article[0].find_all("span"):
        #     i.decompose()
        img = article[0].find_all(["a","strong","span"])
        if img:
            for i in img:
                i.decompose()

        for i in article[0].find_all(["p"]):
            content+=i.text.replace("\n","").replace(" ","").replace(" ","")
        return content
    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print("%s, %s, %s, in line %s"%(exc_type, e, fname, exc_tb.tb_lineno))
        print("yahoonws %s"%e)
        return '404'

def cw(url, file, session, headers):
    print("cw %s"%url)
    content = ""
    try:
        if file:
            with open(file) as e:
                soup = BeautifulSoup(e.read(), 'html.parser')
                # print(soup.prettify())
        else:
            response = session.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
        article = soup.find_all("article")
        for i in article[0].find_all(["span","address"]):
            i.decompose()
        for i in article[0].find_all(["p","h1"]):
            content+=i.text.replace("\n","").replace(" ","")
        return content
    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print("%s, %s, %s, in line %s"%(exc_type, e, fname, exc_tb.tb_lineno))
        print("cw %s"%e)
        return '404'

def ebc(url, file, session, headers):
    print("ebc %s"%url)
    content = ""
    try:
        if file:
            with open(file) as e:
                soup = BeautifulSoup(e.read(), 'html.parser')
                # print(soup.prettify())
        else:
            response = session.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
        article = soup.find_all("div", id="main-inner")
        # for i in article[0].find_all(["span","address"]):
            # i.decompose()
        for i in article[0].find_all(["p","h1"]):
            content+=i.text.replace("\n","").replace(" ","")
        return content
    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print("%s, %s, %s, in line %s"%(exc_type, e, fname, exc_tb.tb_lineno))
        print("ebc %s"%e)
        return '404'   

def fsc(url, file, session, headers):
    print("fsc %s"%url)
    content = ""
    try:
        if file:
            with open(file) as e:
                soup = BeautifulSoup(e.read(), 'html.parser')
                # print(soup.prettify())
        else:
            response = session.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
        article = soup.find_all("div", class_="page_content")
        # for i in article[0].find_all(["span","address"]):
            # i.decompose()
        # for i in article[0].find_all("div", id="maincontent"):
        #     print(i.text)
        for i in article[0].find_all("div", class_="contentdate"):
            i.decompose()
        for i in article[0].find_all(["p","h1","div"]):
            content+=i.text.replace("\n","").replace(" ","").replace(" ","")
        return content
    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print("%s, %s, %s, in line %s"%(exc_type, e, fname, exc_tb.tb_lineno))
        print("fsc %s"%e)
        return '404'

def setn(url, file, session, headers):
    print("setn %s"%url)
    content = ""
    try:
        if file:
            with open(file) as e:
                soup = BeautifulSoup(e.read(), 'html.parser')
                # print(soup.prettify())
        else:
            response = session.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
        article = soup.find_all("article")
        # for i in article[0].find_all(["span","address"]):
            # i.decompose()
        for i in article[0].find_all(["p","h1"]):
            content+=i.text.replace("\n","").replace(" ","")
        return content
    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print("%s, %s, %s, in line %s"%(exc_type, e, fname, exc_tb.tb_lineno))
        print("setn %s"%e)
        return '404'   

def managertoday(url, file, session, headers):
    print("setn %s"%url)
    content = ""
    try:
        if file:
            with open(file) as e:
                soup = BeautifulSoup(e.read(), 'html.parser')
                # print(soup.prettify())
        else:
            response = session.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
        article = soup.find_all("div", itemprop="articleBody")
        # for i in article[0].find_all(["span","address"]):
            # i.decompose()
        for i in article[0].find_all(["p","h2"]):
            content+=i.text.replace("\n","").replace(" ","")
        return content
    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print("%s, %s, %s, in line %s"%(exc_type, e, fname, exc_tb.tb_lineno))
        print("setn %s"%e)
        return '404' 

def hbrtaiwan(url, file, session, headers):
    print("hbrtaiwan %s"%url)
    content = ""
    try:
        if file:
            with open(file) as e:
                soup = BeautifulSoup(e.read(), 'html.parser')
                # print(soup.prettify())
        else:
            response = session.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
        article = soup.find_all("article-content")
        for i in article[0].find_all(["hr","section"]):
            i.decompose()
        for i in article[0].find_all(["p","h1"]):
            content+=i.text.replace("\n","").replace(" ","")
        return content
    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print("%s, %s, %s, in line %s"%(exc_type, e, fname, exc_tb.tb_lineno))
        print("hbrtaiwan %s"%e)
        return '404'   

def cna(url, file, session, headers):
    print("cna %s"%url)
    content = ""
    try:
        if file:
            with open(file) as e:
                soup = BeautifulSoup(e.read(), 'html.parser')
                # print(soup.prettify())
        else:
            response = session.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
        article = soup.find_all("div", class_="container")
        # for i in article[0].find_all(["hr","section"]):
        #     i.decompose()
        for i in article[0].find_all(["p","h1"]):
            content+=i.text.replace("\n","").replace(" ","")
        return content
    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print("%s, %s, %s, in line %s"%(exc_type, e, fname, exc_tb.tb_lineno))
        print("cna %s"%e)
        return '404'

def nextmgz(url, file, session, headers):
    print("nextmgz %s"%url)
    content = ""
    try:
        if file:
            with open(file) as e:
                soup = BeautifulSoup(e.read(), 'html.parser')
                # print(soup.prettify())
        else:
            response = session.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
        article = soup.find_all("div", class_="article-content")
        for i in article[0].find_all(["span"]):
            i.decompose()
        for i in article[0].find_all(["p","h1"]):
            content+=i.text.replace("\n","").replace(" ","")
        return content
    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print("%s, %s, %s, in line %s"%(exc_type, e, fname, exc_tb.tb_lineno))
        print("nextmgz %s"%e)
        return '404'

# session = requests.Session()
# data = parse_url(url="", file="example_htm/mingpao/4.htm",session=session)
# url = "https://news.mingpao.com/ins/%e6%b8%af%e8%81%9e/article/20191104/s00001/1572833030181/22%e6%ad%b2%e7%94%b7%e5%a4%a9%e6%b0%b4%e5%9c%8d%e5%a2%ae%e6%96%83"
# data = parse_url(url,session=session)
# print(data)

