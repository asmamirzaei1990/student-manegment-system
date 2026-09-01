from models.enrollment import Enrollment
class EnrollmentRepository:
    def __init__(self,db):self.db=db
    def _one(self,r): return Enrollment(r["enrollment_id"],r["student_id"],r["course_id"],r["enrollment_date"],r["status"],r["grade"]) if r else None
    def get_all(self):
        with self.db.connect() as c:return [self._one(r) for r in c.execute("SELECT * FROM enrollments ORDER BY enrollment_id")]
    def get_by_id(self,eid):
        with self.db.connect() as c:return self._one(c.execute("SELECT * FROM enrollments WHERE enrollment_id=?",(eid,)).fetchone())
    def exists_student_course(self,sid,cid):
        with self.db.connect() as c:return c.execute("SELECT 1 FROM enrollments WHERE student_id=? AND course_id=?",(sid,cid)).fetchone() is not None
    def add(self,e):
        with self.db.connect() as c:c.execute("INSERT INTO enrollments VALUES (?,?,?,?,?,?)",(e.enrollment_id,e.student,e.course,e.enrollment_date,e.status,e.grade))
    def update(self,eid,d):
        if not self.get_by_id(eid):return False
        with self.db.connect() as c:c.execute("UPDATE enrollments SET student_id=?,course_id=?,enrollment_date=?,status=? WHERE enrollment_id=?",(d["student_id"],d["course_id"],d["enrollment_date"],d["status"],eid))
        return True
    def delete(self,eid):
        with self.db.connect() as c:cur=c.execute("DELETE FROM enrollments WHERE enrollment_id=?",(eid,));return cur.rowcount>0
    def find_by_student_or_course(self,k):
        with self.db.connect() as c:return [self._one(r) for r in c.execute("SELECT * FROM enrollments WHERE student_id=? OR course_id=? ORDER BY enrollment_id",(k,k))]
