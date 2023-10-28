from http.server import HTTPServer, BaseHTTPRequestHandler
import sqlite3
import json

class ProgramRecordHandler(BaseHTTPRequestHandler):

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

        with open('templates/program.html', 'rb') as html_file:
          response_message = html_file.read()
        self.wfile.write(response_message)

      elif self.path == '/database':
        conn = sqlite3.connect('database.sqlite')
        con = conn.cursor()
        con.execute('SELECT * FROM programs_courses')
        database = con.fetchall()
        conn.close()
        self.send_json_response({'database' : database})

      else:
        self.send_response(404)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        response_message = "Not Found"
        self.wfile.write(response_message('utf-8'))
        self.send_json_response({'error': 'Not Found'}, status_code=404)

    except Exception as e:
      self.send_json_response({'error': str(e)}, status_code=500)
      self.send_response(500)
      self.send_header('Content-type', 'text/plain')
      self.end_headers()
      error_message = f"Error: {str(e)}"
      self.wfile.write(error_message.encode('utf-8'))


def run(server_class=HTTPServer, handler_class=ProgramRecordHandler, port=8080):
  server_address = ('', port)
  httpd = server_class(server_address, handler_class)
  print(f'Starting httpd on port {port}...\n')
  httpd.serve_forever()

if __name__ == '__main__':
  run()


