import execjs
import time
import requests
b = int(time.time())*1000+100000000
def get_js():
    # 打开JS文件
    f = open("yuan01.js", 'r', encoding='utf-8')
    line = f.readline()
    hstr = ''
    while line:
        hstr = hstr + line
        line = f.readline()
    return hstr


def get_des_psswd(acc):
    jsstr = get_js()
    # 加载JS文件
    ctx = execjs.compile(jsstr)
    # 调用js方法 第一个参数是JS的方法名，后面的为js方法的参数
    return ctx.call('hex_md5', acc)


def spider():
    session = requests.session()
    v = 0
    c = 0
    for page in range(1, 6):
        baseurl = "http://match.yuanrenxue.com/api/match/1"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36 Edg/92.0.902.55",
            "Host": "match.yuanrenxue.com",
            "Referer": "http://match.yuanrenxue.com/match/1",
            "Cookie": "Hm_lvt_c99546cf032aaa5a679230de9a95c7db=1662961810,1665039628,1665121086; qpfccr=true; no-alert3=true; tk=-9070038626548285971; sessionid=se4gotxiumff757sbklo1h37k6pdj7re; Hm_lvt_9bcbda9cbf86757998a2339a0437208e=1662961822,1665039627,1665126282; Hm_lpvt_9bcbda9cbf86757998a2339a0437208e=1665126282; Hm_lpvt_c99546cf032aaa5a679230de9a95c7db=1665126285"
        }
        if page > 3:
            headers['User-Agent'] = "yuanrenxue.project"
        params = {
            "page": str(page),
            "m": m
        }
        res = session.get(url=baseurl, headers=headers, params=params)
        for each in res.json()['data']:
            print(each['value'])
            v += each['value']
            c += 1
        print("=" * 30)
        time.sleep(1)
    print(v / c)
if __name__ == '__main__':
    m = get_des_psswd(str(b))+'丨'+str(int(b/1000))
    spider()
