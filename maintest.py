import sqlite3
import unittest

def execute_sql(query):
  conn = sqlite3.connect('database.sqlite')
  cursor = conn.cursor()
  cursor.execute(query)
  result = cursor.fetchall()
  conn.close()
  return result
  
class TestDatabase(unittest.TestCase):
  def setUp(self):
    conn = sqlite3.connect('database.sqlite')
    conn.execute(
      '''
          CREATE TABLE IF NOT EXISTS admission_decisions (
              id INTEGER PRIMARY KEY AUTOINCREMENT,
              decision_date TEXT,
              admission_decision TEXT,
              financial_aid_offered TEXT,
              scholarships_awarded TEXT,
              notes_comments TEXT
          )
      '''
    )
    conn.execute("INSERT INTO admission_decisions(decision_date, admission_decision, financial_aid_offered, scholarships_awarded, notes_comments) VALUES ('2020-01-01', 'Accepted', 'Yes', 'Yes', 'Your notes or comments here')")
    conn.execute("INSERT INTO admission_decisions(decision_date, admission_decision, financial_aid_offered, scholarships_awarded, notes_comments) VALUES ('2020-01-01', 'Accepted', 'Yes', 'Yes', 'Your notes or comments here')")
    conn.commit()
    conn.close()

  def tearDown(self):
    conn = sqlite3.connect('database.sqlite')
    conn.execute("DROP TABLE IF Exists admission_decisions")
    conn.commit()
    conn.close()

  def test_execute_sql(self):
    query = "SELECT * FROM admission_decisions"
    result = execute_sql(query)
    self.assertEqual(len(result),2)
    self.assertEqual(result[0],(1, '2020-01-01', 'Accepted', 'Yes', 'Yes', 'Your notes or comments here'))
    self.assertEqual(result[1],(2, '2020-01-01', 'Accepted', 'Yes', 'Yes', 'Your notes or comments here'))
                     

    
if __name__ == '__main__':
  unittest.main()