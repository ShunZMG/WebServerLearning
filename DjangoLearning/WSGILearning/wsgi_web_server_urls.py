# -*- coding: utf-8 -*-
from wsgiref.simple_server import make_server

# environ：浏览器的一些数据

# 1.创建路由分发器，负责把url匹配到对应的函数
# 2.开发好对应的业务函数
# 3.接收到请求后，先到达路由分发器，路由分发器判断是否有这个函数，如果有这个function就执行，如果没有，就返回404


def book(environ,start_response):

    print('book page')
    start_response('200 OK', [('Content-Type', 'text/html;charset=utf-8')])

    return [bytes('<h3>hello World2!</h3>', encoding='utf-8')]


def cloth(environ,start_response):
    print('cloth page')
    start_response('200 OK', [('Content-Type', 'text/html;charset=utf-8')])

    return [bytes('<h3>hello World3!</h3>', encoding='utf-8')]


# 路由分发器，可以为函数，从浏览器发来的请求头中获取url，然后进行分配
def url_route():
    urls = {
        '/book': book,
        '/cloth': cloth
    }
    return urls


def run_server(environ,start_response):
    print('run server')
    print(environ)

    urls_list = url_route()  # 拿到所有的url
    request_url = environ.get("PATH_INFO")  # PATH_INFO 为environ中的请求的url信息
    print('request url:',request_url)

    # 判断所拿到的请求是否在url_list字典中，如果存在，就调用相应的函数，若不存在，则返回404
    if request_url in urls_list:
        func_data = urls_list[request_url](environ,start_response)
        return func_data  # 真正返回数据给用户
    else:
        start_response("404",[('Content-Type','text/html;charset=utf-8')])
        return [bytes('<h1>404, Page NOT Found!</h1>',encoding='utf-8')]


s = make_server('localhost',8000,run_server)
s.serve_forever()