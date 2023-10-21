from http.server import HTTPServer, BaseHTTPRequestHandler

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
      try:
        if self.path == '/':
          self.send_response(200)
          self.send_header('Content-type', 'text/html')
          self.end_headers()
          response_message = "Response GET Request"
          self.wfile.write(response_message.encode(encoding='utf-8'))
            
        else:
          self.send_response(400)
          self.send_header('Content-type','text/plain')
          self.end_headers()
          response_message = "Not Found"
          self.wfile.write(response_message.encode(encoding='utf-8'))
          
      except Exception as e:
          self.send_response(500)
          self.send_header('Content-type', 'text/plain')
          self.end_headers()
          error_message = f"Error: {str(e)}"
          self.wfile.write(error_message.encode('utf-8'))
            
    def do_POST(self):
      try:
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        print(post_data)
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(bytes(post_data, 'utf8'))
      except Exception as e:
        self.send_response(500)
        self.send_header('Content-type','text/html')
        self.end_headers()
        error_message = f"error: {str(e)}"
        self.wfile.write(bytes(error_message, 'utf8'))

httpd = HTTPServer(('', 8000), MyHandler)
httpd.serve_forever()
