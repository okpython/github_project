#!/usr/bin/python
#coding:utf-8

from BaseHTTPServer import HTTPServer,BaseHTTPRequestHandler
import json
from SocketServer import ThreadingMixIn
from collections import OrderedDict

class RequestHandler(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()

    def do_GET(self):
        response = {
            'status': 'SUCCESS',
            'data': 'hello from server'
        }
        self._set_headers()
        self.wfile.write(json.dumps(response))

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        info_dict = json.loads(post_data, strict=False, encoding="utf-8", object_pairs_hook=OrderedDict)
        print(info_dict['name'])
        print 'post data from client:'
        # print post_data

        response = {
            'status': 'SUCCESS',
            'data': 'server got your post data'
        }
        self._set_headers()
        self.wfile.write(json.dumps(response))

class ThreadHTTPServer(ThreadingMixIn, HTTPServer):
    """Handle requests in a separate thread
    实现多线程
    """
    pass

server = ThreadHTTPServer(('10.89.196.138', 8081), RequestHandler)
try:
    print('server starte...')
    server.serve_forever()
except Exception as e:
    print(e)