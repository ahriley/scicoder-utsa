import numpy as np

class City():
    def __init__(self,name,roster=None):
        self.name = name
        self.population = np.random.randint(900,6*10**6)
        if roster is None:
            self.roster = []
        else:
            self.roster = roster

    def addStudent(self,student):
        self.roster.append(student)
