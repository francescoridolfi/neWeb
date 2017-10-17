import time
import neWeb_settings, neWeb_loader
from http.server import BaseHTTPRequestHandler, HTTPServer

HOST_NAME = neWeb_settings.settings.host
PORT_NUMBER = neWeb_settings.settings.port


class MyHandler(BaseHTTPRequestHandler):
    def do_HEAD(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):

        paths = neWeb_settings.settings.paths


        real = self.path.split("?")

        if real[0] in paths:
            self.respond(paths[real[0]],real)
        else:
            self.respond({'status': 404},self.path)

    def handle_http(self, status_code, path):
        self.send_response(status_code)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        content = neWeb_settings.settings.resp[path[0]]

        if(content.endswith(".css") or content.endswith(".js")):
            f = open(content, "r")
            txt = f.read()
            f.close()
            content = txt
        else:
            try:
                if(len(path) == 2):
                    arg = path[1].split("&")
                    args = {}
                    for item in arg:
                        item = item.split("=")
                        args[item[0]] = item[1]
                    HTMLs = neWeb_loader.start(args)
                else:
                    HTMLs = neWeb_loader.start({})
                print(content)
                if(content.endswith(".html")):
                    if(content in neWeb_settings.settings.runnable_files):
                        convert = False
                        for html in HTMLs:
                            if(content == html[1]):
                                convert = True
                        try:
                            f = open(content,"r")
                            txt=f.read()
                            f.close()
                            content=txt
                            if(convert == True):
                                chars = html[0]
                                for keys in chars:
                                    char = chars[keys]["char"]
                                    method = chars[keys]["method"]
                                    content = content.replace(char,method)
                        except:
                            content = "<h1>neWeb ERROR: I can't open the file: %s</h1>" % content
                    else:
                        content = "<h1>neWeb ERROR: The file %s is not allowed in neWeb_settings.py!</h1>" % content
            except ValueError as e:
                print(e)

        if (status_code != 200):
            content = neWeb_settings.settings.resp[str(status_code)]

        return bytes(content, 'UTF-8')

    def respond(self, opts, path):
        response = self.handle_http(opts['status'], path)
        self.wfile.write(response)

if __name__ == '__main__':
    server_class = HTTPServer
    httpd = server_class((HOST_NAME, PORT_NUMBER), MyHandler)
    print(time.asctime(), 'Server Starts - %s:%s' % (HOST_NAME, PORT_NUMBER))
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    print(time.asctime(), 'Server Stops - %s:%s' % (HOST_NAME, PORT_NUMBER))