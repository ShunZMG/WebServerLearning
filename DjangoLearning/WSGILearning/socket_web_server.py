# -*- coding: utf-8 -*-

import socket


def main():
    # 创建socket对象
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    # 绑定端口
    sock.bind(('localhost',8000))
    # 开始监听，最大连接数设置为5
    sock.listen(5)

    while True:
        # 等待连接
        conn, addr = sock.accept()
        # 接收来自浏览器的请求内容
        data = conn.recv(1024)
        print(data, addr)

        # 给浏览器返回内容，先返回头部内容，包含状体码，并制定返回内容的类型，以及编码类型
        conn.send(b'HTTP/1.1 200 OK\r\nContent-Type:text/html;charset=utf-8\r\n\r\n')
        # 然后再返回数据
        conn.send('you are so beautiful!'.encode('utf-8'))

        # 关闭socket连接
        conn.close()


if __name__ == '__main__':
    main()