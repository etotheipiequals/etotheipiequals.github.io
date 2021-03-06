# Python http.server that sets Access-Control-Allow-Origin header.
# https://gist.github.com/razor-x/9542707

import os
import sys
import http.server
import socketserver
import webbrowser

PORT = 8000

class HTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        http.server.SimpleHTTPRequestHandler.end_headers(self)

def server(port):
    httpd = socketserver.TCPServer(('', port), HTTPRequestHandler)
    return httpd

if __name__ == "__main__":
    port = PORT
    httpd = server(port)
    try:
        #os.chdir('build')
        print("\n Serving presentation at localhost:" + str(port)
              +"\n = = = = = = = = = = = = = = = = = = = = = = = = = = = = \n\n")
        print("\n Press   Ctrl + C   to stop web server. \n\n")
        webbrowser.open("localhost:%d/presentation.html" % port, new=2)
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n...shutting down http server")
        httpd.shutdown()
        sys.exit()
