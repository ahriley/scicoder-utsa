class Supervisor():
    def __init__(self,name,roster=None):
        self.name = name
        if roster is None:
            self.roster = []
        else:
            self.roster = roster

    def addStudent(self,student):
        self.roster.append(student)
