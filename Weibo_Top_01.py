import requests
from bs4 import  BeautifulSoup
from urllib import parse#将rul拼接到一起
'''
    单线程爬取微博热榜，html
    爬去完一个页面在爬去另一个，顺序执行
'''

headers = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36'
}

def get_html(url):
    #hearders伪装成浏览器去访问页面，得到页面源码
    html = requests.get(url,headers=headers)
    if html.status_code == 200:
        print("获取页面成功")
        parse_html(html.text)
    else:
        print("error",html.text)
    return

#将获取到的页面进行解析
def parse_html(html):
    #已说明方式解析
    soup = BeautifulSoup(html,'html.parser')
    #获取css标签内容
    trs = soup.select('table tbody tr')
    for tr in trs:
        #获取更底层标签的内容
        title = tr.select_one('td a').text
        #获取该标签下中一个属性
        url = tr.select_one('td a')['href']
        # 补全链接
        url = parse.urljoin('https://s.weibo.com/',url)
        print(title,url)

if __name__ == '__main__':
    #单线程执行
    url1 = "https://s.weibo.com/top/summary"
    get_html(url1)
    url2 = "https://s.weibo.com/top/summary?cate=socialevent"
    get_html(url2)