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
