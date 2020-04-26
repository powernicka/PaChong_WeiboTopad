import json
import time
import requests
import  threading
'''
    Json破解
'''
headers = {
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36',
'Connection': 'close'
}

new_set = set()

def getnew():
    url = 'https://opendata.baidu.com/data/inner?tn=reserved_all_res_tn&dspName=iphone&from_sf=1&dsp=iphone&resource_id=28565&alr=1&query=%E8%82%BA%E7%82%8E&cb=jsonp_1587136710225_23585'
    html = requests.get(url,headers=headers)

    #截取需要的Json字符串
    start = html.text.find('{"ResultCode')
    end = html.text.find(r'srcids\u0000\u0000"}')+len(r'srcids\u0000\u0000"}')
    json_data = json.loads(html.text[start:end])
    #层层递进在json中寻找所需内容
    data_new = json_data['Result'][0]['DisplayData']['result']['items']

    while 1:

        for content in data_new:
            #获取json中制定的内容
            news_title = content['eventDescription']
            news_time = content['eventTime']
            #格式化时间
            local_time = time.localtime(int(news_time))
            current_time = time.strftime("%Y-%m-%d-%M-%S",local_time)
            url = content['eventUrl']
            siteName = content['siteName']
            current_new = news_title + current_time +'\n'+url+'\n'+siteName
            #放到set中去重
            if current_new not  in new_set:
                new_set.add(current_new)

        for i in new_set:
            print(i)

        time.sleep(10 *1)


    # print(json_data['Result'][0]['DisplayData']['result']['items'])

def main():

    threading.Thread(target=getnew()).start()

if __name__ == '__main__':

    main()
