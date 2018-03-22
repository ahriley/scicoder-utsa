class Student():
    def __init__(self,name,status,city,supervisor=None,clubs=None):
        self.name = name
        self.status = status
        self.city = city
        if supervisor is None:
            self.supervisor = []
        else:
            self.supervisor = supervisor
        if clubs is None:
            self.clubs = []
        else:
            self.clubs = clubs
