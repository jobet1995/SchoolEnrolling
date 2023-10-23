import sqlite3

try:
    conn = sqlite3.connect('enroll.sqlite')
    c = conn.cursor()

    c.execute('''
        CREATE TABLE students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            contact_phone TEXT,
            contact_email TEXT,
            contact_address TEXT,
            application_date TEXT,
            application_status TEXT,
            program_course TEXT,
            test_scores TEXT,
            transcripts TEXT,
            recommendation_letters TEXT,
            application_fee_payment_status TEXT,
            application_essays TEXT,
            application_reviewer TEXT,
            FOREIGN KEY (program_course) REFERENCES program_courses(id)
        )
    ''')

    c.execute('''
        CREATE TABLE admission_decisions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            decision_date TEXT,
            admission_decision TEXT,
            financial_aid_offered TEXT,
            scholarships_awarded TEXT,
            notes_comments TEXT
        )
    ''')

    c.execute('''
        CREATE TABLE communication_logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            datetime TEXT,
            communication_type TEXT,
            communication_content TEXT,
            related_to TEXT, -- Applicant or Student
            student_id INTEGER,
            FOREIGN KEY (student_id) REFERENCES students (id)
        )
    ''')

    c.execute('''
        CREATE TABLE programs_courses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            program_name TEXT,
            application_deadline TEXT,
            available_slots INTEGER,
            program_requirements TEXT
        )
    ''')

    c.execute('''
        CREATE TABLE enrollments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            enrollment_date TEXT,
            enrollment_status TEXT,
            payment_status TEXT,
            student_id INTEGER,
            academic_advisor TEXT,
            FOREIGN KEY (student_id) REFERENCES students (id)
        )
    ''')

    c.execute('''
        CREATE TABLE prospective_students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            lead_source TEXT,
            lead_qualification_status TEXT,
            interests_preferences TEXT,
            demographic_information TEXT
        )
    ''')

    c.execute('''
        CREATE TABLE events_activities (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            event_name TEXT,
            event_type TEXT,
            attendance_participation TEXT,
            follow_up_actions TEXT
        )
    ''')

    c.execute('''
        CREATE TABLE document_management (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            document_name TEXT,
            document_type TEXT,
            document_data BLOB
        )
    ''')
    c.execute('''
        CREATE TABLE Users (
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          uname TEXT,
          pword TEXT,
          email TEXT
        )
    ''')

    c.execute('''
         CREATE TABLE subjects (
            id INTEGER PRIMARY    KEY AUTOINCREMENT,
            subject_name TEXT NOT NULL,
            program_course_id INTEGER,
    FOREIGN KEY (program_course_id) REFERENCES program_courses(id)
            time TEXT,
            days TEXT
        )
    ''')
    c.execute('''
        CREATE TABLE teachers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            teacher_name TEXT NOT NULL,
            email TEXT,
            phone_number TEXT,
            subject_taught_id INTEGER,
            FOREIGN KEY (subject_taught_id) REFERENCES subjects(id)
        )
    ''')
    c.execute('''
    CREATE TABLE program_courses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    program_name TEXT NOT NULL,
    application_deadline TEXT,
    available_slots INTEGER,
    program_requirements TEXT
       )
   ''')
  
  
    conn.commit()
    conn.close()
except Exception as e:
    print("Error creating database:", e)