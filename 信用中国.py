import requests
import json
import random
headers = {
    'Accept': '*/*',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Cookie': 'FSSBBIl1UgzbN7N443S=9jcY1yPg8LQ_868MVAHM9q2Of0QsgiHPfZqJd6nkTdvpwI2clg1Zi8.dTNS5gY80; insert1_cookie=76657641; Hm_lvt_0076fef7e919d8d7b24383dc8f1c852a=1550800012,1551235202; browseHistory=%5B%7B%22name%22%3A%22%E4%B9%90%E8%A7%86%E6%8E%A7%E8%82%A1(%E5%8C%97%E4%BA%AC)%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8%22%2C%22encryStr%22%3A%22Nmkwcm4xRkFp%5Cn%22%7D%2C%7B%22name%22%3A%22%E4%B9%90%E8%A7%86%E6%8E%A7%E8%82%A1(%E5%8C%97%E4%BA%AC)%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8%22%2C%22encryStr%22%3A%22Nmkwcm4xRkFp%5Cn%22%7D%2C%7B%22name%22%3A%22%E4%B9%90%E8%A7%86%E6%8E%A7%E8%82%A1(%E5%8C%97%E4%BA%AC)%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8%22%2C%22encryStr%22%3A%22WzBpZTt5NEF7%5Cn%22%7D%2C%7B%22name%22%3A%22%E4%B9%90%E8%A7%86%E6%8E%A7%E8%82%A1(%E5%8C%97%E4%BA%AC)%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8%22%2C%22encryStr%22%3A%22OTBqcm4xNEEw%5Cn%22%7D%2C%7B%22name%22%3A%22%E4%B9%90%E8%A7%86%E4%BA%91%E8%AE%A1%E7%AE%97%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8%22%2C%22encryStr%22%3A%22c2ZueXpiMHJx%5Cn%22%7D%2C%7B%22name%22%3A%22%E4%B9%90%E8%A7%86%E6%B1%BD%E8%BD%A6(%E5%8C%97%E4%BA%AC)%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8%22%2C%22encryStr%22%3A%22dDs5cHRwdGN7%5Cn%22%7D%2C%7B%22name%22%3A%22%E9%94%A4%E5%AD%90%E7%A7%91%E6%8A%80(%E5%8C%97%E4%BA%AC)%E8%82%A1%E4%BB%BD%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8%22%2C%22encryStr%22%3A%22ZDZ9bG5iZHJ6%5Cn%22%7D%5D; Hm_lpvt_0076fef7e919d8d7b24383dc8f1c852a=1551247336; FSSBBIl1UgzbN7N443T=3.TPD_8ViVfQkIgIleIPO_Tssd5zgd9QeqxRFe715zBgE8mA2nvwJcEuifqJ4lWt4gqG.9uuMe6kyuMUpKRyCTp9yNvPtfs9JF17rjMVerYhV86vEe5dLI7ocquQuyDJCCJSX3HgpPGZ4tFCDj2OAEvKBPdCqjVmUICt8AM66TwZEK1dKWInt9A9iXPet6q400vp2BUF1t9Yovs1nQMiHcrRBMQWOKaIyLuQqneWMx4iLMG',
    'Host': 'www.creditchina.gov.cn',
    'Referer': 'https://www.creditchina.gov.cn/xinyongxinxi/index.html?index=0&keyword=%E4%B9%90%E8%A7%86',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest'
}
url = 'https://www.creditchina.gov.cn/api/credit_info_search?keyword=乐视&templateId=&page=1&pageSize=10'
proxy_list = [
    {'http':'35.229.97.65:80','https':'222.74.237.246:808'},
    {'http':'35.229.97.65:80','https':'123.146.233.93:53281'},
    {'http':'35.229.97.65:80','https':'123.161.21.106:9797'},
    {'http':'35.229.97.65:80','https':'116.209.52.239:9999'},
    {'http':'35.229.97.65:80','https':'103.227.117.94:8080'},
    {'http':'35.229.97.65:80','https':'197.210.130.46:33329'},
    {'http':'35.229.97.65:80','https':'14.207.6.135:8080'},
    {'http':'35.229.97.65:80','https':'116.197.134.153:80'},
    {'http':'35.229.97.65:80','https':'103.48.207.73:8080'},
    {'http':'35.229.97.65:80','https':'5.175.104.28:53281'},
    {'http':'35.229.97.65:80','https':'185.52.79.107:8181'},
    {'http':'35.229.97.65:80','https':'222.165.195.75:55949'}
]
all_enterprise = []
n = 0
proxy = random.choice(proxy_list)
while n < 20:
    try:
        proxy = random.choice(proxy_list)
        response = requests.request('get', url=url, headers=headers, proxies = proxy, timeout = 5).content.decode('utf-8')
        response = json.loads(response)
    except Exception as e:
        print("代理IP{}失败".format(str(proxy)))
        n += 1
    else:
        for i in response['data']['results']:
            one_enterprise = {}
            one_enterprise['企业名'] = i['name']
            one_enterprise['encryStr'] = i['encryStr'].replace('\n', '')
            all_enterprise.append(one_enterprise)
        break
for i in all_enterprise:
    encryStr = i['encryStr']
    url = 'https://www.creditchina.gov.cn/api/credit_info_detail?encryStr=' + encryStr
    n = 0
    while n < 20:
        try:
            proxy = random.choice(proxy_list)
            response = requests.request('get', url=url, headers=headers, proxies=proxy, timeout = 5).content.decode('utf-8')
            response = json.loads(response)
        except Exception as e:
            print("代理IP{}失败".format(str(proxy)))
            n += 1
        else:
            i['工商注册号'] = response['result']['regno']
            i['法人'] = response['result']['legalPerson']
            i['成立日期'] = response['result']['esdate'][0:10]
            i['企业类型'] = response['result']['enttype']
            i['地址'] = response['result']['dom']
            i['登记机关'] = response['result']['regorg']
            i['统一社会信用代码'] = response['result']['creditCode']
            print("{}——企业基本信息已获取".format(i['企业名']))
            break
for i in all_enterprise:
    name = i['企业名']
    url = 'https://www.creditchina.gov.cn/api/pub_permissions_name?name={}&page=1&pageSize=10'.format(name)
    n = 0
    while n < 20:
        try:
            proxy = random.choice(proxy_list)
            response = requests.request('get', url=url, headers=headers, proxies=proxy, timeout = 5).content.decode('utf-8')
            response = json.loads(response)
        except Exception as e:
            print("代理IP{}失败".format(str(proxy)))
            n += 1
        else:
            xzxk = []
            for a in response['result']['results']:
                one_xzxk = {}
                one_xzxk['行政许可决定书文号'] = a['xkWsh']
                one_xzxk['审核类型'] = a['xkSplb']
                one_xzxk['许可法人'] = a['xkFr']
                one_xzxk['内容许可'] = a['xkNr']
                one_xzxk['许可有效期'] = a['xkYxq']
                one_xzxk['许可决定日期'] = a['xkJdrq']
                one_xzxk['许可截止日期'] = a['xkJzq']
                one_xzxk['地方编码'] = a['xkDfbm']
                one_xzxk['许可机关'] = a['xkXzjg']
                one_xzxk['数据更新时间'] = a['xkSjc'][0:10]
                xzxk.append(one_xzxk)
            i['行政许可'] = xzxk
            print("{}——行政许可信息已获取".format(i['企业名']))
            break
for i in all_enterprise:
    name = i['企业名']
    url = 'https://www.creditchina.gov.cn/api/pub_penalty_name?name={}&page=1&pageSize=10'.format(name)
    n = 0
    while n < 20:
        try:
            proxy = random.choice(proxy_list)
            response = requests.request('get', url=url, headers=headers, proxies=proxy, timeout = 5).content.decode('utf-8')
            response = json.loads(response)
        except Exception as e:
            print("代理IP{}失败".format(str(proxy)))
            n += 1
        else:
            xzcf = []
            for a in response['result']['results']:
                one_xzcf = {}
                one_xzcf['决定书文号'] = a['cfWsh']
                one_xzcf['处罚名称'] = i['企业名']
                one_xzcf['法人代表'] = a['cfFr']
                one_xzcf['处罚类别'] = a['cfCflb1']
                one_xzcf['处罚结果'] = a['cfJg'].replace('\n', '')
                one_xzcf['处罚事由'] = a['cfSy']
                one_xzcf['处罚依据'] = a['cfYj']
                one_xzcf['处罚机关'] = a['cfXzjg']
                one_xzcf['处罚决定日期'] = a['cfJdrq']
                one_xzcf['处罚期限'] = a['cfQx']
                xzcf.append(one_xzcf)
            i['行政处罚'] = xzcf
            print("{}——行政处罚信息已获取".format(i['企业名']))
            break
for i in all_enterprise:
    encryStr = i['encryStr']
    url = 'https://www.creditchina.gov.cn/api/record_param?encryStr={}&creditType=2&dataSource=0&pageNum=1&pageSize=10'.format(encryStr)
    n = 0
    while n < 20:
        try:
            proxy = random.choice(proxy_list)
            response = requests.request('get', url=url, headers=headers, proxies=proxy, timeout = 5).content.decode('utf-8')
            response = json.loads(response)
        except Exception as e:
            print("代理IP{}失败".format(str(proxy)))
            n += 1
        else:
            sxhmd = []
            for a in response['result']:
                one_sxhmd = {}
                one_sxhmd['数据类别'] = a['数据类别']
                one_sxhmd['纳税人名称'] = i['企业名']
                one_sxhmd['数据来源'] = a['数据来源']
                one_sxhmd['序号'] = a['序号']
                one_sxhmd['评价年度'] = a['评价年度']
                one_sxhmd['最新更新日期'] = a['最新更新日期']
                one_sxhmd['文件名'] = a['文件名']
                sxhmd.append(one_sxhmd)
            i['守信红名单'] = sxhmd
            print("{}——守信红名单信息已获取".format(i['企业名']))
            break
for i in all_enterprise:
    encryStr = i['encryStr']
    url = 'https://www.creditchina.gov.cn/api/record_param?encryStr={}&creditType=4&dataSource=0&pageNum=1&pageSize=10'.format(encryStr)
    n = 0
    while n < 20:
        try:
            proxy = random.choice(proxy_list)
            response = requests.request('get', url=url, headers=headers, proxies=proxy, timeout = 5).content.decode('utf-8')
            response = json.loads(response)
        except Exception as e:
            print("代理IP{}失败".format(str(proxy)))
            n += 1
        else:
            zdgzmd = []
            for a in response['result']:
                one_zdgzmd = {}
                one_zdgzmd['数据类别'] = a['数据类别']
                one_zdgzmd['企业名称'] = i['企业名']
                one_zdgzmd['数据来源'] = a['数据来源']
                one_zdgzmd['注册号'] = a['注册号']
                one_zdgzmd['法定代表人'] = a['法定代表人']
                one_zdgzmd['列入经营异常名录原因类型名称'] = a['列入经营异常名录原因类型名称']
                one_zdgzmd['设立日期'] = a['设立日期']
                one_zdgzmd['列入决定机关名称'] = a['列入决定机关名称']
                one_zdgzmd['最新更新日期'] = a['最新更新日期']
                zdgzmd.append(one_zdgzmd)
            i['重点关注名单'] = zdgzmd
            print("{}——重点关注名单信息已获取".format(i['企业名']))
            break
for i in all_enterprise:
    encryStr = i['encryStr']
    url = 'https://www.creditchina.gov.cn/api/record_param?encryStr={}&creditType=8&dataSource=0&pageNum=1&pageSize=10'.format(encryStr)
    n = 0
    while n < 20:
        try:
            proxy = random.choice(proxy_list)
            response = requests.request('get', url=url, headers=headers, proxies=proxy, timeout = 5).content.decode('utf-8')
            response = json.loads(response)
        except Exception as e:
            print("代理IP{}失败".format(str(proxy)))
            n += 1
        else:
            hmd = []
            for a in response['result']:
                one_hmd = {}
                one_hmd['数据类别'] = a['数据类别']
                one_hmd['失信被执行人名称'] = a['失信被执行人名称']
                one_hmd['数据来源'] = a['数据来源']
                one_hmd['案号'] = a['案号']
                one_hmd['企业法人姓名'] = a['企业法人姓名']
                one_hmd['执行法院'] = a['执行法院']
                one_hmd['地域名称'] = a['地域名称']
                one_hmd['执行依据文号'] = a['执行依据文号']
                one_hmd['作出执行依据单位'] = a['作出执行依据单位']
                one_hmd['法律生效文书确定的义务'] = a['法律生效文书确定的义务'].replace('\n', '')
                one_hmd['被执行人的履行情况'] = a['被执行人的履行情况']
                one_hmd['失信被执行人具体情形'] = a['失信被执行人具体情形']
                one_hmd['发布时间'] = a['发布时间']
                one_hmd['立案时间'] = a['立案时间']
                one_hmd['已履行部分'] = a['已履行部分']
                one_hmd['未履行部分'] = a['未履行部分']
                one_hmd['最新更新日期'] = a['最新更新日期']
                hmd.append(one_hmd)
            i['黑名单'] = hmd
            print("{}——黑名单信息已获取".format(i['企业名']))
            break
for i in all_enterprise:
    with open('信用中国//{}.txt'.format(i['企业名']), 'w', encoding='utf-8') as f:
        for k, v in i.items():
            f.write(k)
            f.write("：")
            f.write(str(v))
            f.write('\n')
