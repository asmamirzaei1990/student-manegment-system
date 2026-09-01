from models.course import Course
class CourseRepository:
    def __init__(self,db):self.db=db
    def _one(self,r):
        return Course(r["course_id"],r["name"],r["units"],r["teacher_id"],r["capacity"],r["semester"],r["department"],r["day"],r["start_time"],r["end_time"],r["room"]) if r else None
    def get_all(self):
        with self.db.connect() as c:return [self._one(r) for r in c.execute("SELECT * FROM courses ORDER BY course_id")]
    def get_by_id(self,cid):
        with self.db.connect() as c:return self._one(c.execute("SELECT * FROM courses WHERE course_id=?",(cid,)).fetchone())
    def add(self,c):
        with self.db.connect() as x:x.execute("INSERT INTO courses VALUES (?,?,?,?,?,?,?,?,?,?,?)",(c.course_id,c.name,c.units,c.teacher,c.capacity,c.semester,c.department,c.day,c.start_time,c.end_time,c.room))
    def update(self,cid,d):
        if not self.get_by_id(cid):return False
        with self.db.connect() as x:x.execute("UPDATE courses SET name=?,units=?,teacher_id=?,capacity=?,semester=?,department=?,day=?,start_time=?,end_time=?,room=? WHERE course_id=?",(d["name"],d["units"],d["teacher_id"],d["capacity"],d["semester"],d["department"],d["day"],d["start_time"],d["end_time"],d["room"],cid))
        return True
    def delete(self,cid):
        with self.db.connect() as x:cur=x.execute("DELETE FROM courses WHERE course_id=?",(cid,));return cur.rowcount>0
    def search_by_name(self,k):
        with self.db.connect() as x:return [self._one(r) for r in x.execute("SELECT * FROM courses WHERE lower(name) LIKE lower(?) ORDER BY course_id",(f"%{k.strip()}%",))]
    def count_enrollments(self,cid):
        with self.db.connect() as x:return x.execute("SELECT COUNT(*) FROM enrollments WHERE course_id=?",(cid,)).fetchone()[0]
