from entities.rocket import Rocket
from people.student_engineer import StudentEngineer
from utilities.constants import LAUNCH_CODE

if __name__ == "__main__":
    # Tworzenie rakiety
    falcon9 = Rocket(thrust_power=5000)
    falcon9.set_fuel_level(75)
    
    # Tworzenie inżyniera-studenta
    student = StudentEngineer("Jan", "Kowalski", "Politechnika Warszawska")
    student.report_status()
    
    # Sekwencja startowa
    falcon9.launch_sequence()