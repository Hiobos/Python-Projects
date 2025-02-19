from .person import Person
from utilities.mission_member import MissionMember

class StudentEngineer(Person, MissionMember):
    def __init__(self, first_name, last_name, university):
        super().__init__(first_name, last_name)
        self.university = university