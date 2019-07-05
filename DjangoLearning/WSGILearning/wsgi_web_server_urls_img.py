# -*- coding: utf-8 -*-
from wsgiref.simple_server import make_server
import os
import re
# environ：浏览器的一些数据

# 1.创建路由分发器，负责把url匹配到对应的函数
# 2.开发好对应的业务函数
# 3.接收到请求后，先到达路由分发器，路由分发器判断是否有这个函数，如果有这个function就执行，如果没有，就返回404

# 获取当前文件的文件夹路径
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# BASE_DIR = "C:/Python/Learning/DjangoLearning/"


def img_handler(request_url):
    # 需要对获取到的图片url进行处理，获取到的url只是相对路径，程序无法找到图片，因此需要将其转变为绝对路径
    img_path = "%s%s" %(BASE_DIR,request_url)
    # 判断img_path下的文件是否存在，如果存在，就将其内容返回
    if os.path.isfile(img_path):
        f = open(img_path,'rb')
        img_data = f.read()  # 获取图片内容
        return [img_data, 0]  # 0表示状态，表示文件存在 1表示文件不存在
    return [None,1]


def book(environ,start_response):
    print('book page')
    start_response('200 OK', [('Content-Type', 'text/html;charset=utf-8')])
    data="""
        <h1>Hello my friend</h1>
        <img src="/static/imgs/1.png"/>
    """
    return [bytes(data, encoding='utf-8')]


def cloth(environ,start_response):
    print('cloth page')
    start_response('200 OK', [('Content-Type', 'text/html;charset=utf-8')])

    data="""
        <h1>hello my friend!</h1>
        <img src="/static/imgs/1.png" />
    """
    return [bytes(data, encoding='utf-8')]


# 路由分发器，可以为函数，从浏览器发来的请求头中获取url，然后进行分配
def url_route():
    urls = {
        '/book': book,
        '/cloth': cloth
    }
    return urls


def run_server(environ,start_response):
    urls_list = url_route()  # 拿到所有的url
    request_url = environ.get("PATH_INFO")  # PATH_INFO 为environ中的请求的url信息
    print('request url:',request_url)
    print(BASE_DIR)

    # 判断所拿到的请求是否在url_list字典中，如果存在，就调用相应的函数，若不存在，则返回404
    if request_url in urls_list:
        func_data = urls_list[request_url](environ,start_response)
        return func_data  # 真正返回数据给用户
    elif request_url.startswith("/static/"):  # 判断是否是静态文件
        img_data,img_status = img_handler(request_url)
        if img_status == 0:  # 说明图片数据有内容，加上送回的头部内容后返回img内容
            start_response("200 OK", [('Content-Type', 'text/jpeg;charset=utf-8')])
            return [img_data,]
        elif img_status == 1:  # 如果状态为1，则返回404
            start_response("404 ", [('Content-Type', 'text/html;charset=utf-8')])
            return [bytes('<h1>404, Page NOT Found!</h1>', encoding='utf-8')]
    else:
        start_response("404 ",[('Content-Type','text/html;charset=utf-8')])
        return [bytes('<h1>404, Page NOT Found!</h1>',encoding='utf-8')]


# 创建服务器对象，传入ip地址、端口号和处理函数
s = make_server('localhost',8000,run_server)
# 启动
s.serve_forever()