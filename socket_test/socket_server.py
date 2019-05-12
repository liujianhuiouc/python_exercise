# !/usr/bin/env python
# -*- coding: utf-8 -*-


from socket import socket, AF_UNIX, SOCK_STREAM
import threading
import os


class SocketServer(object):
    def __init__(self, server_address):
        self.server_address = server_address

    def start(self):
        self.socket = socket(AF_UNIX, SOCK_STREAM)
        self.socket.bind(self.server_address)
        self.socket.listen(5)
        print("file no", self.socket.fileno())

        while 1:
            conn, client_address = self.socket.accept()
            print("connection file", conn.fileno())
            thread = threading.Thread(target=SocketServer.dispatch, args=(conn, client_address))
            thread.start()

    @staticmethod
    def dispatch(conn, client_address):
        print('client address is %s' % client_address)
        data = conn.recv(1024)
        print(data)
        conn.sendall('hello world')


if __name__ == '__main__':
    server_address = '/Users/liujianhui/a1.sock'
    os.remove(server_address) if os.path.exists(server_address) else 0
    socket_server = SocketServer(server_address)
    socket_server.start()

