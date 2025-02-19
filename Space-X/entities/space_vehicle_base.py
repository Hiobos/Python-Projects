from abc import ABC, abstractmethod

class SpaceVehicleBase(ABC):
    @abstractmethod
    def launch_sequence(self):
        pass
