import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR / "student_management.db"

class Database:
    def __init__(self, db_path=DB_PATH):
        self.db_path = str(db_path)

    def connect(self):
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        conn.execute("PRAGMA foreign_keys = ON")
        return conn

    def initialize(self):
        with self.connect() as conn:
            conn.executescript('''
            CREATE TABLE IF NOT EXISTS universities (
                university_id TEXT PRIMARY KEY, name TEXT NOT NULL, city TEXT NOT NULL,
                address TEXT, phone TEXT, email TEXT, website TEXT, established_year INTEGER,
                student_count INTEGER, faculty_count INTEGER, department TEXT
            );
            CREATE TABLE IF NOT EXISTS professors (
                professor_id TEXT PRIMARY KEY, first_name TEXT NOT NULL, last_name TEXT NOT NULL,
                age INTEGER NOT NULL, phone TEXT, email TEXT, degree TEXT, specialization TEXT,
                department TEXT, employment_type TEXT
            );
            CREATE TABLE IF NOT EXISTS students (
                student_id TEXT PRIMARY KEY, first_name TEXT NOT NULL, last_name TEXT NOT NULL,
                age INTEGER NOT NULL, birth_place TEXT, major TEXT, semester INTEGER,
                email TEXT, phone TEXT, gpa REAL
            );
            CREATE TABLE IF NOT EXISTS courses (
                course_id TEXT PRIMARY KEY, name TEXT NOT NULL, units INTEGER NOT NULL,
                teacher_id TEXT NOT NULL, capacity INTEGER NOT NULL, semester INTEGER,
                department TEXT, day TEXT, start_time TEXT, end_time TEXT, room TEXT,
                FOREIGN KEY (teacher_id) REFERENCES professors(professor_id) ON UPDATE CASCADE
            );
            CREATE TABLE IF NOT EXISTS enrollments (
                enrollment_id TEXT PRIMARY KEY, student_id TEXT NOT NULL, course_id TEXT NOT NULL,
                enrollment_date TEXT NOT NULL, status TEXT NOT NULL, grade REAL,
                UNIQUE(student_id, course_id),
                FOREIGN KEY(student_id) REFERENCES students(student_id) ON DELETE CASCADE,
                FOREIGN KEY(course_id) REFERENCES courses(course_id) ON DELETE RESTRICT
            );
            CREATE TABLE IF NOT EXISTS grades (
                grade_id TEXT PRIMARY KEY, student_id TEXT NOT NULL, course_id TEXT NOT NULL,
                score REAL NOT NULL, date TEXT NOT NULL,
                UNIQUE(student_id, course_id),
                FOREIGN KEY(student_id) REFERENCES students(student_id) ON DELETE CASCADE,
                FOREIGN KEY(course_id) REFERENCES courses(course_id) ON DELETE RESTRICT
            );
            ''')

    def seed_if_empty(self):
        from data.university_data import UNIVERSITY_DATA
        from data.professors_data import PROFESSORS_DATA
        from data.students_data import STUDENTS_DATA
        from data.courses_data import COURSES_DATA
        from data.enrollments_data import ENROLLMENTS_DATA
        from data.grades_data import GRADES_DATA
        with self.connect() as conn:
            if conn.execute("SELECT COUNT(*) FROM students").fetchone()[0] != 0:
                return
            conn.execute("INSERT INTO universities VALUES (?,?,?,?,?,?,?,?,?,?,?)", UNIVERSITY_DATA)
            conn.executemany("INSERT INTO professors VALUES (?,?,?,?,?,?,?,?,?,?)", PROFESSORS_DATA)
            conn.executemany("INSERT INTO students VALUES (?,?,?,?,?,?,?,?,?,?)", STUDENTS_DATA)
            conn.executemany("INSERT INTO courses VALUES (?,?,?,?,?,?,?,?,?,?,?)", COURSES_DATA)
            conn.executemany("INSERT INTO enrollments(enrollment_id,student_id,course_id,enrollment_date,status) VALUES (?,?,?,?,?)", ENROLLMENTS_DATA)
            conn.executemany("INSERT INTO grades VALUES (?,?,?,?,?)", GRADES_DATA)

    def reset(self):
        with self.connect() as conn:
            conn.executescript('''DROP TABLE IF EXISTS grades; DROP TABLE IF EXISTS enrollments;
            DROP TABLE IF EXISTS courses; DROP TABLE IF EXISTS students; DROP TABLE IF EXISTS professors;
            DROP TABLE IF EXISTS universities;''')
        self.initialize()
        self.seed_if_empty()
