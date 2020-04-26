import json
import re

import  requests


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36'
}

def get_html(url):
    try:
        html = requests.get(url,headers=headers)
        html.encoding = html.apparent_encoding
    # print(html.text)
        return html.text
    except:
        print("出现了错误")


def parse_doc(html):
    result = ''
    url_list = re.findall('(https:.*?0.json.*?)\\\\x22}',html)
    url_list = [addr.replace('\\\\\\/','/') for addr in url_list]
    # print(url_list)
    for url in url_list:
        html_contect1 = get_html(url)
        y = 0
        
        # print(url)
        textlists = re.findall('"c":"(.*?)".*?"y":(.*?),', html_contect1)
        # print(textlists)
        for item in textlists[:-5]:
            # print(item[1])
            if not y == item[1]:
                y = item[1]
                n = '\n'
            else:
                n=''
            result += n
            result += item[0].encode('utf-8').decode('unicode_escape','ignore')
    return result




def main():
    url = input("请输入网址：")
    html = get_html(url)
    title = re.findall("\'title\'.*?\'(.*?\')",html)[0]
    type = re.findall("\'docType\'.*?\'(.*?\')", html)[0]
    ida = re.findall("\'docId\'.*?\'(.*?\')", html)[0]
    print("dsdfsd",title)
    print("dsafda",type)

    result = parse_doc(html)

    filename = title +".doc"
    with open(filename,'w',encoding='utf-8') as f:
        f.write(result)
    print("文件保存为{}".format(filename))


if __name__ == '__main__':
    main()