# js破解 反爬虫
import random
import time
import hashlib
import  requests
'''
    var r = function(e) {
        var t = n.md5(navigator.appVersion)
          , r = "" + (new Date).getTime()
          , i = r + parseInt(10 * Math.random(), 10);
        return {
            ts: r,
            bv: t,
            salt: i,
            sign: n.md5("fanyideskweb" + e + i + "Nw(nmmbP%A-r6U3EUn]Aj")
        }
'''
appVersion = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36'
keywords = input("请输入需要翻译的词：")
headers = {
    'Cookie': 'OUTFOX_SEARCH_USER_ID=-717552920@10.108.160.18; JSESSIONID=aaaBwMwL2qJCY4DZ-bjgx; OUTFOX_SEARCH_USER_ID_NCOO=667279274.2182317; ___rl__test__cookies=1587142180400',
    'Referer': 'http://fanyi.youdao.com/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36'
}
url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'


def tras():
    r = time.time()*1000
    i = r + int(random.random()*10)

    salt = i
    ts = r
    sign = hashlib.md5(("fanyideskweb" +keywords +str(i) +"Nw(nmmbP%A-r6U3EUn]Aj").encode('utf-8')).hexdigest()
    bv = hashlib.md5(appVersion.encode('utf-8')).hexdigest()

    data = {
        'i': keywords,
        'from': 'AUTO',
        'to': 'AUTO',
        'smartresult': 'dict',
        'client': 'fanyideskweb',
        'salt': salt,
        'sign': sign,
        'ts': ts,
        'bv': bv,
        'doctype': 'json',
        'version': '2.1',
        'keyfrom': 'fanyi.web',
        'action': 'FY_BY_REALTlME'
    }

    html = requests.post(url,data=data,headers =headers)

    print(html.json()['translateResult'][0][0]['src'])
    print(html.json()['translateResult'][0][0]['tgt'])

if __name__ == '__main__':
    tras()