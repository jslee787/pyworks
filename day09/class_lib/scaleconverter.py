class ScaleConverter:
    def __init__(self, units_from, units_to, factor):
        self.units_from = units_from
        self.units_to = units_to
        self.factor = factor

    def convert(self, value):
        return self.factor * value

if __name__=='__main__':
    sc = ScaleConverter('inches', 'mm', 25)
    print("Converting 2 inches")
    print(str(sc.convert(2)) + sc.units_to)