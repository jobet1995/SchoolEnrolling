CREATE TABLE program_courses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    program_name TEXT NOT NULL,
    application_deadline TEXT,
    available_slots INTEGER,
    program_requirements TEXT
);

CREATE TABLE students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    contact_phone TEXT,
    contact_email TEXT,
    contact_address TEXT,
    application_date TEXT,
    application_status TEXT,
    program_course_id INTEGER,
    test_scores TEXT,
    transcripts TEXT,
    recommendation_letters TEXT,
    application_fee_payment_status TEXT,
    application_essays TEXT,
    application_reviewer TEXT,
    FOREIGN KEY (program_course_id) REFERENCES program_courses(id)
);

CREATE TABLE admission_decisions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    decision_date TEXT,
    admission_decision TEXT,
    financial_aid_offered TEXT,
    scholarships_awarded TEXT,
    notes_comments TEXT
);

CREATE TABLE communication_logs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    datetime TEXT,
    communication_type TEXT,
    communication_content TEXT,
    related_to TEXT,
    student_id INTEGER,
    FOREIGN KEY (student_id) REFERENCES students(id)
);

CREATE TABLE enrollments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    enrollment_date TEXT,
    enrollment_status TEXT,
    payment_status TEXT,
    student_id INTEGER,
    academic_advisor TEXT,
    FOREIGN KEY (student_id) REFERENCES students(id)
);

CREATE TABLE prospective_students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    lead_source TEXT,
    lead_qualification_status TEXT,
    interests_preferences TEXT,
    demographic_information TEXT
);

CREATE TABLE events_activities (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    event_name TEXT,
    event_type TEXT,
    attendance_participation TEXT,
    follow_up_actions TEXT
);

CREATE TABLE document_management (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    document_name TEXT,
    document_type TEXT,
    document_data BLOB
);

CREATE TABLE Users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    uname TEXT,
    pword TEXT,
    email TEXT
);

CREATE TABLE subjects (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    subject_name TEXT NOT NULL,
    time TEXT,
    days TEXT,
    program_course_id INTEGER,
    FOREIGN KEY (program_course_id) REFERENCES program_courses(id)
);

CREATE TABLE teachers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    teacher_name TEXT NOT NULL,
    email TEXT,
    phone_number TEXT,
    subject_taught_id INTEGER,
    FOREIGN KEY (subject_taught_id) REFERENCES subjects(id)
);
