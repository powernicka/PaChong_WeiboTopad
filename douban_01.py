from uuid import uuid4

import requests
import bs4
import  os


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36',
    'Cookie': 'bid=JJNZ34D0sYo; ap_v=0,6.0; __utma=30149280.1203516276.1587124907.1587124907.1587124907.1; __utmc=30149280; __utmz=30149280.1587124907.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmt=1; __gads=ID=ac33be2a0bfd3781:T=1587124908:S=ALNI_MZa9sAvfDyptjo9-LOY2PCuy_8SXQ; __utmt_douban=1; __utma=81379588.1017193609.1587124911.1587124911.1587124911.1; __utmc=81379588; __utmz=81379588.1587124911.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; _pk_ref.100001.3ac3=%5B%22%22%2C%22%22%2C1587124911%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DoF9RtT7wvZOFdGzEAk9zWIeXKYgV60NzxIosYAkOUYcWB4GZ6tIcTYw3jmtn8cECnXNco_YFZFWKjrtNC3vpcq%26wd%3D%26eqid%3D94ba87c1001a5a9d000000035e999aa5%22%5D; _pk_ses.100001.3ac3=*; __utmb=30149280.3.10.1587124907; __utmb=81379588.2.10.1587124911; _pk_id.100001.3ac3=d005dd90794b450c.1587124911.1.1587124981.1587124911.'
}

def get_html(url):
     html = requests.get(url,headers=headers)
     if html.status_code == 200:
         print('成功')
         parse_html(html.text)
     else:
         print('ERROR',html.status_code)
     return

def parse_html(html):
    soup = bs4.BeautifulSoup(html, 'html.parser')
    books = soup.select('li.subject-item')
    for book in books:
        title  = book.select_one('div.info h2 a').text.strip().replace(' ','').replace('\n','')
        author = book.select_one('div.info div.pub').text.strip().replace(' ', '').replace('\n', '')
        content = book.select_one('div.info p').text.strip().replace(' ', '').replace('\n', '')
        image = book.select_one('.pic a img')['src']
        download(image)
        print(title,author)
        print(content)
        print(image)
        print('*'*20)

def download(img):
    filename = 'img'
    #如果这个文件不存在就自动创建
    if not os.path.exists(filename):
        os.mkdir(filename)
    html = requests.get(img,headers=headers)
    with open('{}/{}.jpg'.format(filename,uuid4()),'wb') as a:
        a.write(html.content)


if __name__ == '__main__':
    url = 'https://book.douban.com/tag/%E5%B0%8F%E8%AF%B4?start={}&type=T'
    num = 1
    for i in range(0,60,20):
        print('正在爬去第{}页'.format(num))
        get_html(url.format(i))
        num +=1