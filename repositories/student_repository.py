from models.student import Student

class StudentRepository:
    def __init__(self, db): self.db = db
    def _one(self, row):
        return Student(row["student_id"], row["first_name"], row["last_name"], row["age"], row["birth_place"], row["major"], row["semester"], row["email"], row["phone"], row["gpa"]) if row else None
    def get_all(self):
        with self.db.connect() as c: return [self._one(r) for r in c.execute("SELECT * FROM students ORDER BY student_id")]
    def get_by_id(self, student_id):
        with self.db.connect() as c: return self._one(c.execute("SELECT * FROM students WHERE student_id=?", (student_id,)).fetchone())
    def add(self, s):
        with self.db.connect() as c: c.execute("INSERT INTO students VALUES (?,?,?,?,?,?,?,?,?,?)", (s.student_id,s.first_name,s.last_name,s.age,s.birth_place,s.major,s.semester,s.email,s.phone,s.gpa))
    def update(self, sid, d):
        if not self.get_by_id(sid): return False
        d = dict(d); d["student_id"] = sid
        with self.db.connect() as c: c.execute("UPDATE students SET first_name=?,last_name=?,age=?,birth_place=?,major=?,semester=?,email=?,phone=?,gpa=? WHERE student_id=?", (d["first_name"],d["last_name"],d["age"],d["birth_place"],d["major"],d["semester"],d["email"],d["phone"],d["gpa"],sid))
        return True
    def delete(self, sid):
        with self.db.connect() as c: cur=c.execute("DELETE FROM students WHERE student_id=?",(sid,)); return cur.rowcount > 0
    def search_by_name(self, keyword):
        p=f"%{keyword.strip()}%"
        with self.db.connect() as c: return [self._one(r) for r in c.execute("SELECT * FROM students WHERE lower(first_name||' '||last_name) LIKE lower(?) ORDER BY student_id",(p,))]
