from .space_vehicle_base import SpaceVehicleBase
from utilities.constants import LAUNCH_CODE

class Rocket(SpaceVehicleBase):
    def __init__(self, thrust_power):
        self._fuel_level = 0
        self.thrust_power = thrust_power
    
    def set_fuel_level(self, fuel):
        self._fuel_level = fuel
    
    def get_fuel_level(self):
        return self._fuel_level
    
    def launch_sequence(self):
        if self._fuel_level > 50:
            print(f"Rakieta startuje z mocą {self.thrust_power}! Kod startowy: {LAUNCH_CODE}")
        else:
            print("Za mało paliwa do startu!")