from http.server import HTTPServer, BaseHTTPRequestHandler
import sqlite3
import base64
import json

class MyHandler(BaseHTTPRequestHandler):

    def send_json_response(self, response_data, status_code=200):
        self.send_response(status_code)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(response_data).encode())
      
    def do_GET(self):
      try:
        if self.path == '/':
          self.send_response(200)
          self.send_header('Content-type', 'text/html')
          self.end_headers()

          with open('templates/index.html', 'rb') as html_file:
            respose_message = html_file.read()
          self.wfile.write(respose_message)
          ##response_message = "Response GET Request"
          ##self.wfile.write(response_message.encode(encoding='utf-8'))

        elif self.path == '/database':
          conn = sqlite3.connect('database.sqlite')
          c = conn.cursor()
          c.execute('SELECT * FROM students')
          database = c.fetchall()
          conn.close()
          self.send_json_response({'database':database})

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
          self.send_json_response({'error': 'Not Found'}, status_code=404)
          
      except Exception as e:
          self.send_json_response({'error': str(e)}, status_code=500)
          self.send_response(500)
          self.send_header('Content-type', 'text/plain')
          self.end_headers()
          error_message = f"Error: {str(e)}"
          self.wfile.write(error_message.encode('utf-8'))
            
    def do_POST(self):
      try:
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length).decode('utf-8')

        conn = sqlite3.connect('database.sqlite')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO students(name,contact_phone, contact_email, contact_address, application_date, application_status, program_applying_for, test_scores,             transcripts, recommendation_letters, application_fee_payment_status, application_essays, application_reviewer)VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)',(body))
        conn.commit()
        conn.close()
        self.send_json_response({'message': 'Received POST data and inserted into the database.'})
        
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        response_message = "Received POST data and inserted into the database."
        self.wfile.write(response_message.encode('utf-8'))
        
      except Exception as e:
        self.send_json_response({'error': str(e)}, status_code=500)
        self.send_response(500)
        self.send_header('Content-type','text/html')
        self.end_headers()
        error_message = f"error: {str(e)}"
        self.wfile.write(bytes(error_message, 'utf8'))
        self.send_json_response({'error': str(e)}, status_code=500)

    def do_PUT(self):
      try:
        content_length = int(self.headers.get('Content-Length'))
        body = self.rfile.read(content_length).decode('utf-8')
        id = int(self.path.split('/')[-1])

        conn = sqlite3.connect('database.sqlite')
        cursor = conn.cursor()
        cursor.execute('UPDATE students SET name=? WHERE id=?',(body, id))
        conn.commit()
        conn.close()
        conn.send_json_response({'message': 'Received PUT data and updated the database.'})
        
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        response_message = f"Updated student record with ID: {id} in the database"
        self.wfile.write(response_message.encode('utf-8'))
        
      except Exception as e:
        self.send_json_response({'error': str(e)}, status_code=500)
        self.send_response(500)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        error_message = f"error: {str(e)}"
        self.wfile.write(error_message.encode('utf-8'))

    def do_DELETE(self):
      try:
        id = int(self.path.split('/')[-1])

        conn = sqlite3.connect('database.sqlite')
        cursor = conn.cursor()
        cursor.execute('DELETE FROM students WHERE id=?',(id,))
        conn.commit()
        conn.close()
        conn.send_json_response({'message': 'Received DELETE data and deleted the database.'})

        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        response_message = f"Deleted student record with ID: {id} from the database"
        self.wfile.write(response_message.encode('utf-8'))

      except Exception as e:
        self.send_json_response({'error': str(e)}, status_code=500)
        self.send_response(500)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        error_message = f"Error: {str(e)}"
        self.wfile.write(error_message.encode('utf-8'))

    def do_AUTHHEAD(self):
      try:
        self.send_response(401)
        self.send_header('WWW-Authenticate', 'Basic realm=\"Login required\"')
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        
      except Exception as e:
        self.send_response(500)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        error_message = f"Error in do_AUTHHEAD: {str(e)}"
        self.wfile.write(error_message.encode('utf-8'))

    def do_login(self, authorization_header):
      try:
        credentials = authorization_header.split(' ')[1]
        credentials = base64.b64decode(credentials).decode('utf-8')
        username, password = credentials.split(':')

        if username == 'admin' and password == 'admin':
          self.send_response(200)
          self.send_header('Content-type', 'text/plain')
          self.end_headers()
          response_message = "Login successful."
        else:
          self.do_AUTHHEAD()
          response_message = "Login failed. Invalid username or password."
        self.wfile.write(response_message.encode('utf-8'))

      except Exception as e:
        self.send_response(500)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        error_message = f"Error in do_login: {str(e)}"
        self.wfile.write(error_message.encode('utf-8'))
  
def run(server_class=HTTPServer, handler_class=MyHandler, port=8080):
  server_address = ('', port)
  httpd = server_class(server_address, handler_class)
  print(f'Starting httpd on port {port}...\n')
  httpd.serve_forever()

if __name__ == '__main__':
  run()