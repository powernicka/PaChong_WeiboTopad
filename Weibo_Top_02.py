import time

import requests
import asyncio
from bs4 import  BeautifulSoup
from urllib import parse#将rul拼接到一起
import  aiohttp

'''
    异步程爬取微博热榜
    同时爬取，伪并发
    很好的利用了单线程优势，socket（IO等待时间）
'''

headers = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36'
}
# async表示异步IO
async def get_html(url):
    print('正在爬去：',url)
    async with aiohttp.ClientSession(headers=headers) as session:
        async  with session.get(url) as  resp:
            if resp.status == 200:
                print("获取页面成功")
                parse_html(await resp.text())
            else:
                print("error",resp.status)
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
    start = time.time()
    url = [
        'https://s.weibo.com/top/summary?cate=socialevent',
        'https://s.weibo.com/top/summary'
    ]
    tasks = []
    for url in url:
        tasks.append(get_html(url))
    #创建异步de事件循环
    loop = asyncio.get_event_loop()
    #获取当前事件循环,开启异步事件，等待异步完成
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()

    print(time.time()-start)