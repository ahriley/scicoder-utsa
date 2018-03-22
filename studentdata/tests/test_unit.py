from studentdata.student import Student
from studentdata.club import Club
from studentdata.supervisor import Supervisor
from studentdata.city import City

name = "name1 name2"
status = "status"
city = City(name="city")
supervisor = Supervisor(name="super")
clubs = [Club("Chess"), Club("Fencing")]

def test_cityPop():
    assert 900 <= city.population <= 6*10**6

def test_classes():
    newStudent = Student(name,status,city,supervisor,clubs)
    assert newStudent.supervisor.name == "super"
    assert newStudent.city.name == "city"
    assert newStudent.clubs[0].name == "Chess"

def test_manyInstances():
    club1 = Club("club1")
    club2 = Club("club2")
    club1.addStudent(Student(name,status,city))
    assert len(club1.roster) == 1
    assert len(club2.roster) == 0
