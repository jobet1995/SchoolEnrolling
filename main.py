from http.server import HTTPServer, BaseHTTPRequestHandler
import sqlite3

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
      try:
        if self.path == '/':
          self.send_response(200)
          self.send_header('Content-type', 'text/html')
          self.end_headers()
          response_message = "Response GET Request"
          self.wfile.write(response_message.encode(encoding='utf-8'))

        elif self.path == '/database':
          conn = sqlite3.connect('database.sqlite')
          c = conn.cursor()
          c.execute('SELECT * FROM students')
          database = c.fetchall()
          conn.close()

          self.send_response(200)
          self.send_header('Content-type', 'text/plain')
          self.end_headers()
          response_message = "database:\n"
          for database in database:
            response_message += f"{database[0]}. {database[1]}\n"
          self.wfile.write(response_message.encode('utf-8'))
            
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

    def do_PUT(self):
      try:
        content_length = int(self.headers.get('Content-Length'))
        body = self.rfile.read(content_length).decode('utf-8')
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        response_message = "Received PUT data:\n" + body
        self.wfile.write(response_message.encode('utf-8'))
        
      except Exception as e:
        self.send_response(500)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        error_message = f"error: {str(e)}"
        self.wfile.write(error_message.encode('utf-8'))
      
httpd = HTTPServer(('', 8000), MyHandler)
httpd.serve_forever()
