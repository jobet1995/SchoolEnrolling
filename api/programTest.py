import sqlite3
import unittest

def execute_sql(query):
    conn = sqlite3.connect('database.sqlite')
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()
    result = cursor.fetchall()
    conn.close()
    return result

class TestDatabase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        conn = sqlite3.connect('database.sqlite')
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS programs_courses (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                program_name TEXT,
                application_deadline TEXT,
                available_slots INTEGER,
                program_requirements TEXT
            )
        ''')
        conn.commit()
        conn.close()

    def setUp(self):
        conn = sqlite3.connect('database.sqlite')
        conn.execute("INSERT INTO programs_courses(program_name, application_deadline, available_slots, program_requirements) VALUES('Python Programming', '2020-05-01', 5, 'Python Programming Course')")
        conn.execute("INSERT INTO programs_courses(program_name, application_deadline, available_slots, program_requirements) VALUES('Java Programming', '2020-05-01', 5, 'Java Programming Course')")
        conn.commit()
        conn.close()

    def tearDown(self):
        conn = sqlite3.connect('database.sqlite')
        conn.execute("DROP TABLE IF EXISTS programs_courses")
        conn.commit()
        conn.close()

    def test_execute_sql(self):
        query = "SELECT * FROM programs_courses"
        result = execute_sql(query)
        self.assertEqual(len(result), 2)
        success_count = 0
        
        self.assertEqual(result[0], (1, 'Python Programming', '2020-05-01', 5, 'Python Programming Course'))
        self.assertEqual(result[1], (2, 'Java Programming', '2020-05-01', 5, 'Java Programming Course'))

        for row in result:
          if row[0] == 1:
            success_count += 1
        self.assertEqual(success_count, 1)
      
        success_rate = (success_count / len(result)) * 100
        self.assertEqual(success_rate, 50.0)

if __name__ == '__main__':
    unittest.main()
