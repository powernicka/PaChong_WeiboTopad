import requests
import os




def get_video():
    url = 'https://api3-core-c-lq.amemv.com/aweme/v1/aweme/post/?source=0&publish_video_strategy_type=0&max_cursor=1586509795000&sec_user_id=MS4wLjABAAAA_7oxbNxptT1MIThDQKEV5ncUV_exgln9G_4zKv9VNGUysmMOEz_UeTx_oY8kUWdB&count=10&ts=1587906368&_rticket=1587906368456&mcc_mnc=46003& HTTP/1.1'
    headers = {
        'Cookie': 'install_id=3667602895542254; ttreq=1$1221f2b0f81368526aa8618792bfc72b481c78a8; passport_csrf_token=04fcdec14612ca93310e6680cd2749b6; d_ticket=fc74c21f2255d3fe2521dfb2437c2adc65c55; odin_tt=334455eab770f3e78d1e0133f2b4370bcea7a053bd285c70a9671cf41a408273a02666954a3547f333acc9ad9bb07358; sid_guard=a79f068807060b06d275be8fe5b34dfa%7C1587903651%7C5184000%7CThu%2C+25-Jun-2020+12%3A20%3A51+GMT; uid_tt=6afb0d3df952f54656ec96479c87e163; sid_tt=a79f068807060b06d275be8fe5b34dfa; sessionid=a79f068807060b06d275be8fe5b34dfa',
        'X-SS-REQ-TICKET': '1587905467351',
        'sdk-version': '1',
        'X-SS-DP': '1128',
        'x-tt-trace-id': '00-b68a95730d567aa57b02b6e0db000468-b68a95730d567aa5-01',
        'User-Agent': 'com.ss.android.ugc.aweme/100401 (Linux; U; Android 6.0.1; zh_CN; MI 5s; Build/V417IR; Cronet/TTNetVersion:3154e555 2020-03-04 QuicVersion:8fc8a2f3 2020-03-02)',
        'X-Gorgon': '04014005400150680da601bd8f6ec82305bce6936f0b20157f93',
        'X-Khronos': '1587905467',
        'x-common-params-v2': 'os_api=23&device_platform=android&device_type=MI%205s&iid=3667602895542254&version_code=100400&app_name=aweme&openudid=d31a58bd880a0ed1&device_id=1521356196817774&os_version=6.0.1&aid=1128&channel=tengxun_new&ssmix=a&manifest_version_code=100401&dpi=270&cdid=e2c5b12c-ff2c-4fe1-8679-7357378ac775&version_name=10.4.0&resolution=810*1440&language=zh&device_brand=Xiaomi&app_type=normal&ac=wifi&update_version_code=10409900&uuid=910000000155621'
    }
    requests.packages.urllib3.disable_warnings()
    html = requests.get(url,headers=headers,verify=False)
    json_data = html.json()['aweme_list']
    for i in json_data:
        url = i['video']['play_addr']['url_list'][0]
        title = i['desc']
        print(title,url)
        # downloads(url,title)


# 下载视频
def downloads(url,title):
    filename = '抖音'
    if not os.path.exists(filename):
        os.mkdir(filename)
    with open('{}/{}.mp4'.format(filename,title), 'wb') as f:
        f.write(requests.get(url).content)
    print("下载视频{}文件".format(title))




if __name__ == '__main__':
    get_video()