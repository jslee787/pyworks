from day09.class_lib.airplane import AirPlane

class SuperSonicAirPlane(AirPlane):
    NORMAL = 1
    SUPERSONIC = 2

    def __init__(self):
        self.fly_mode = SuperSonicAirPlane.NORMAL

    def fly(self):
        if self.fly_mode == SuperSonicAirPlane.SUPERSONIC:
            print("비행기가 초음속으로 비행합니다.")
        else:
            super().fly()