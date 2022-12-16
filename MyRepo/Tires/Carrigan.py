from Tires import Tires

class Carrigan(Tires):
    def __init__(self, sensor_readings):
        self.sensor_readings = sensor_readings

    def needs_service(self):
        needs_service = False
        for s in self.sensor_readings:
            if s > .9:
                needs_service = True
        return needs_service