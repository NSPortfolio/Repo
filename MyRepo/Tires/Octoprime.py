from Tires import Tires

class Octoprime(Tires):
    def __init__(self, sensor_readings):
        self.sensor_readings = sensor_readings

    def needs_service(self):
        needs_service = False
        sum = 0
        for s in self.sensor_readings:
            sum += s
        if s >= 3:
            needs_service = True
        return needs_service
