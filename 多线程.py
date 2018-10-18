# import threading
# import time
#
#
# #方法一：将要执行的方法作为参数传给Thread的构造方法
# def action(arg):
#     time.sleep(1)
#     print('the arg is:%s\r' % arg)
#     for i in range(4):
#         t = threading.Thread(target=action, args=(i,))
#         t.start()
#
# print('main thread end!')
import os
if not os.path.exists('img2'):
    os.mkdir('./img2')