from models.university import University
class UniversityRepository:
    def __init__(self,db):self.db=db
    def get_all(self):
        with self.db.connect() as c:
            return [University(*r) for r in c.execute("SELECT university_id,name,city,address,phone,email,website,established_year,student_count,faculty_count,department FROM universities ORDER BY university_id")]
