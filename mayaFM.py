import os
import json

import requests
from contextlib import closing
from progressbar import ProgressBar

from down_line import ProgressBar

# start_url = 'https://www.ximalaya.com/revision/play/album?albumId=' \
#             '3595841&pageNum={}&sort=-1&pageSize=30'
# 3595841 分类ID
# pageNum={} 分页码

# 运行主目录程序


def xi_ma():
    # 找URL
    start_url = 'https://www.ximalaya.com/revision/play/album?albumId=' \
                '3595841&pageNum={}&sort=-1&pageSize=30'

    # 解析url 得到的网页
    # 增加header头 简单的反扒技术
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                      '(KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
    }

    for i in range(8):
        url = start_url.format(i + 1)   # 翻页效果相当于提交分页，也就是下一页
        print(url)
        # 提交网址
        r = requests.get(url, headers=headers)
        # 获取数据
        ret = r.content.decode('utf-8')
        # 转换JSON格式
        result = json.loads(ret)
        # 遍历测试结果
        for i in result['data']['tracksAudioPlay']:
            # print(i['trackName'], '' + i['src'])
            src = i['src']
            name = i['trackName']
            # 保存数据
            #     with open('./img/{}.m4a' .format(name), 'ab') as f:
            # f.write(music.content)

            with closing(requests.get(src, headers=headers, stream=True)) as response:
                chunk_size = 1024
                content_size = int(response.headers['content-length'])
                progress = ProgressBar(name, total=content_size, unit='KB', chunk_size=chunk_size,
                                       run_status='正在下载', fin_status='下载完毕')
                if not os.path.exists('img'):
                    os.mkdir('./img')
                with open('./img/{}.m4a' .format(name), 'ab') as file:
                    for data in response.iter_content(chunk_size=chunk_size):
                        file.write(data)
                        progress.refresh(count=len(data))


if __name__ == '__main__':
    xi_ma()
