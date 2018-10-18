# a = '{'name': {'name1': {'name2': 'python'}}}' # 转换为json  '' 前后带有的字典 转换成JSON
# b = a['name']['name1']['name2']
# # print(b)
# print(b)
# b = json.loads(a) # json.loads() 能够把字符串变成字典
# print(b = a['name']['name1']['name2'])
#
# c ={'name':'pytchon'}
# print(c['name'])


# 测试获取分类

import json
import requests


class get_ID:

    def get_url():
        url = 'https://www.ximalaya.com/revision/getRankList?code=yinyue'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                          '(KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
        }
        r = requests.get(url, headers=headers).content.decode()
        ret = json.loads(r)
        result = []
        for i in ret['data']['albums']:
            result = i['id']
            print(result)
        return


if __name__ == '__main__':
    get_ID.get_url()


