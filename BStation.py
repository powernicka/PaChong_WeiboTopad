from   __future__ import  absolute_import#防止命名错误
import requests
import json
import  os
import  threading


headers = {

'referer': 'https://space.bilibili.com/11000',
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36'
}

def b_get(url):

    jsondata = requests.get(url).json()
    if jsondata['code'] == 0:
        mid = jsondata['data']['mid']
        sex = jsondata['data']['sex']
        face = jsondata['data']['face']
        level = jsondata['data']['level']
        birthday= jsondata['data']['birthday']
        coins = jsondata['data']['coins']
        name = jsondata['data']['name']
        # print(jsondata)
        downloads(face,name)
        print(mid,name,sex,face,level,birthday,coins)

def get_num(url):
    jsonnum_data = requests.get(url,headers=headers)

    start = jsonnum_data.text.find('{"code"')
    end = jsonnum_data.text.find(')')
    json1 = json.loads(jsonnum_data.text[start:end])['data']

    mid = json1['mid']
    following = json1['following']
    follower = json1['follower']

    # print(json1)
    print(mid,following,follower)
    print("*"*20)

def downloads(url,username=1):
    filename = '图片'
    if not os.path.exists(filename):
        os.mkdir(filename)
    print("正在下载图片")
    img = requests.get(url,headers=headers).content
    with open('{}/{}.jpg'.format(filename,username),'wb') as f:
        f.write(img)


def main():

    for i in range(22,23):
        url = 'https://api.bilibili.com/x/space/acc/info?mid={}&jsonp=jsonp'.format(i)
        url1 = 'https://api.bilibili.com/x/relation/stat?vmid={}&jsonp=jsonp&callback=__jp3'.format(i)
        threading.Thread(target=b_get(url)).start()
        threading.Thread(target=get_num(url1)).start()

if __name__ == '__main__':
    main()