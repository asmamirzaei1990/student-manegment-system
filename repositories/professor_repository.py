from models.professor import Professor
class ProfessorRepository:
    def __init__(self, db): self.db=db
    def _one(self,r): return Professor(r["professor_id"],r["first_name"],r["last_name"],r["age"],r["phone"],r["email"],r["degree"],r["specialization"],r["department"],r["employment_type"]) if r else None
    def get_all(self):
        with self.db.connect() as c:return [self._one(r) for r in c.execute("SELECT * FROM professors ORDER BY professor_id")]
    def get_by_id(self,pid):
        with self.db.connect() as c:return self._one(c.execute("SELECT * FROM professors WHERE professor_id=?",(pid,)).fetchone())
    def add(self,p):
        with self.db.connect() as c:c.execute("INSERT INTO professors VALUES (?,?,?,?,?,?,?,?,?,?)",(p.professor_id,p.first_name,p.last_name,p.age,p.phone,p.email,p.degree,p.specialization,p.department,p.employment_type))
    def update(self,pid,d):
        if not self.get_by_id(pid):return False
        with self.db.connect() as c:c.execute("UPDATE professors SET first_name=?,last_name=?,age=?,phone=?,email=?,degree=?,specialization=?,department=?,employment_type=? WHERE professor_id=?",(d["first_name"],d["last_name"],d["age"],d["phone"],d["email"],d["degree"],d["specialization"],d["department"],d["employment_type"],pid))
        return True
    def delete(self,pid):
        with self.db.connect() as c:cur=c.execute("DELETE FROM professors WHERE professor_id=?",(pid,));return cur.rowcount>0
    def search_by_name(self,k):
        with self.db.connect() as c:return [self._one(r) for r in c.execute("SELECT * FROM professors WHERE lower(first_name||' '||last_name) LIKE lower(?) ORDER BY professor_id",(f"%{k.strip()}%",))]
