import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime
import re

RESULT_PATH= '/c/Users/owner0220/Desktop/competition/visual/'
now = datetime.now()


def main():
    # maxpage=input("최대 출력 페이지 수")
    # query = input("검색어 입력:")
    # s_date = input("시작날짜 입력(2019.01.01) :")
    # e_date = input("끝날짜 입력(2019.04.28) :")
    query ="삼성"
    s_date = '2019.01.01'
    e_date = '2020.03.30'
    crawler(query,s_date,e_date)

    excel_make()



def crawler(query,s_date,e_date):
    s_from = s_date.replace(".","")
    e_to = e_date.replace(".","")
    page = 1
    maxpage_t = 4000
    url = "https://search.naver.com/search.naver?where=news&query=" + query + "&sort=1&ds=" + s_date + "&de=" + e_date + "&nso=so%3Ar%2Cp%3Afrom" + s_from + "to" + e_to + "%2Ca%3A&start=" + str(page)
    req = requests.get(url)
    cont = req.content
    soup = BeautifulSoup(cont, 'html.parser')
    tcount=soup.select("#main_pack > div.news.mynews.section._prs_nws > div.section_head > div.title_desc.all_my")[0].text.split('/')[1]
    count_num = ''.join(re.findall('\d+',tcount))
    temp=int(count_num)//10+1
    if temp < 4000:
        maxpage_t=temp

    with open("./contents_text.txt", 'w', encoding='utf-8') as f:
        while page < maxpage_t:
            # print(page)
            url = "https://search.naver.com/search.naver?where=news&query=" + query + "&sort=0&ds=" + s_date + "&de=" + e_date + "&nso=so%3Ar%2Cp%3Afrom" + s_from + "to" + e_to + "%2Ca%3A&start=" + str(page)
            req = requests.get(url)
            # print(url)
            cont = req.content
            soup = BeautifulSoup(cont, 'html.parser')
            print(count_num)
            print(maxpage_t)
            print(page)
            

            # print(soup)
            for urls in soup.select("._sp_each_url"):
                try :
                #print(urls["href"])
                    if urls["href"].startswith("https://news.naver.com"):
                #print(urls["href"])
                        news_detail = get_news(urls["href"])
                        # pdate, pcompany, title, btext
                        f.write("{}\t{}\t{}\t{}\t{}\n".format(news_detail[1], news_detail[4], news_detail[0], news_detail[2],news_detail[3])) # new style
                except Exception as e:
                    print(e)
                    continue
            page += 10
    



        


def get_news(n_url):
    news_detail = []
    breq = requests.get(n_url)
    bsoup = BeautifulSoup(breq.content, 'html.parser')
    title = bsoup.select('h3#articleTitle')[0].text #대괄호는 h3#articleTitle 인 것중 첫번째 그룹만 가져오겠다.
    news_detail.append(title)
    pdate = bsoup.select('.t11')[0].get_text()[:11]
    news_detail.append(pdate)
    _text = bsoup.select('#articleBodyContents')[0].get_text().replace('\n', " ")
    btext = _text.replace("// flash 오류를 우회하기 위한 함수 추가 function _flash_removeCallback() {}", "")
    news_detail.append(btext.strip().replace("\t", " "))
    news_detail.append(n_url)
    pcompany = bsoup.select('#footer address')[0].a.get_text()
    news_detail.append(pcompany)
    return news_detail


def excel_make():
    data = pd.read_csv(RESULT_PATH+'contents_text.txt', sep='\t',header=None, error_bad_lines=False)
    data.columns = ['years','company','title','contents','link']
    print(data)
    xlsx_outputFileName = '%s-%s-%s %s시 %s분 %s초 result.xlsx' % (now.year, now.month, now.day, now.hour, now.minute, now.second)
    #xlsx_name = 'result' + '.xlsx'
    data.to_excel(RESULT_PATH+xlsx_outputFileName, encoding='utf-8')




# main()


# https://search.naver.com/search.naver?&where=news&query=%EC%82%BC%EC%84%B1&start=11