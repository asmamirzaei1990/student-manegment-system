from models.grade import Grade
class GradeRepository:
    def __init__(self,db):self.db=db
    def _one(self,r):return Grade(r["grade_id"],r["student_id"],r["course_id"],r["score"],r["date"]) if r else None
    def get_all(self):
        with self.db.connect() as c:return [self._one(r) for r in c.execute("SELECT * FROM grades ORDER BY grade_id")]
    def get_by_id(self,gid):
        with self.db.connect() as c:return self._one(c.execute("SELECT * FROM grades WHERE grade_id=?",(gid,)).fetchone())
    def exists_student_course(self,sid,cid):
        with self.db.connect() as c:return c.execute("SELECT 1 FROM grades WHERE student_id=? AND course_id=?",(sid,cid)).fetchone() is not None
    def add(self,g):
        with self.db.connect() as c:c.execute("INSERT INTO grades VALUES (?,?,?,?,?)",(g.grade_id,g.student,g.course,g.score,g.date))
    def update(self,gid,d):
        if not self.get_by_id(gid):return False
        with self.db.connect() as c:c.execute("UPDATE grades SET student_id=?,course_id=?,score=?,date=? WHERE grade_id=?",(d["student_id"],d["course_id"],d["score"],d["date"],gid))
        return True
    def delete(self,gid):
        with self.db.connect() as c:cur=c.execute("DELETE FROM grades WHERE grade_id=?",(gid,));return cur.rowcount>0
    def find_by_student_or_course(self,k):
        with self.db.connect() as c:return [self._one(r) for r in c.execute("SELECT * FROM grades WHERE student_id=? OR course_id=? ORDER BY grade_id",(k,k))]
