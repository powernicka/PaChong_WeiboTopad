
import requests
# from bs4 import BeautifulSoup
from lxml import etree
'''
    xpath
'''
headers = {
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36',
'Connection': 'close'
}

def get_html(url):
    html = requests.get(url,headers=headers)
    if html.status_code == 200:
        print('成功')
        print(html.text)
        #parse_html(html.text)
    else:
        print("ERROR",html.status_code)
    return

def parse_html(html):

    num = 0
    #源代码转化为xpath格式
    soup = etree.HTML(html)
    data = soup.xpath('//div[@class = "cover_tabs"]')

    for cover_data in data:
        title = cover_data.xpath('')
        print(title,"ad")
        num +=1
        print(num)



if __name__ == '__main__':
    url = 'https://wp.m.163.com/163/page/news/virus_report/index.html?_nw_=1&_anw_=1'
    get_html(url)