# -*- coding: utf-8 -*-
from wsgiref.simple_server import make_server

# environ：浏览器的一些数据


def run_server(environ,start_response):
    print('hhahha')

    start_response('200 OK',[('Content-Type','text/html;charset=utf-8')])
    return [bytes('<h3>hellowWolrd!</h3>',encoding='utf-8')]


s = make_server('localhost',8000,run_server)
s.serve_forever()  # 启动服务器
