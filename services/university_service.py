class UniversityService:
    def __init__(self,repo):self.repo=repo
    def get_all(self):return self.repo.get_all()
