from uuid import uuid4

import  requests
import re
import os

def getpage():
    url = 'https://stock.tuchong.com/topic?topicId=49599#481859759799795754'
    html = requests.get(url, headers='')
    id_list = re.findall('"imageId":"(.*?)"', html.text)

    for i in id_list:
        url_id = 'https://weiliicimg6.pstatp.com/weili/l/{}.webp'.format(i)
        download(url_id,i)




# headers = {
# 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36'
# }
def  download(url,i):
    filename = '图片2'
    if not os.path.exists(filename):
        os.mkdir(filename)
    img = requests.get(url)
    with open('{}/{}.jpg'.format(filename,i),'wb') as f:
        f.write(img.content)



if __name__ == '__main__':

    getpage()
