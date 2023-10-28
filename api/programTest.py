import unittest
import requests

class TestProgramRecordHandler(unittest.TestCase):

  def test_do_GET(self):
    response = requests.get('http://localhost:8080/')
    self.assertEqual(response.status_code, 200)

    response = requests.get('http://localhost:8080/database')
    self.assertEqual(response.status_code, 200)
    self.assertTrue('database' in response.json())

    response = requests.get('http://localhost:8080/nonexistent')
    self.assertEqual(response.status_code, 404)
    self.assertTrue('error' in response.json())

  def test_do_POST(self):
    data = {
      'program_name': 'Program A',
      'application_deadline': '2023-12-31',
      'available_slots': 50,
      'program_requirements': 'Bachelor\'s degree'
    }

    response = requests.post('htt://localhost:8080/database', json=data)
    self.assertEqual(response.status_code, 200)

  def test_do_PUT(self):
    data = {
        'program_name': 'Updated Program A',
        'application_deadline': '2023-12-31',
        'available_slots': 60,
        'program_requirements': 'Bachelor\'s degree with honors'
    }

    response = requests.put('http://localhost:8080/database/Program A', json=data)
    self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
  unittest.main()