from day09.class_lib.scaleconverter import ScaleConverter

class Converter(ScaleConverter):
    def __init__(self, units_from, units_to, factor, offset):
        super().__init__(units_from, units_to, factor)
        self.offset = offset

    def convert(self, value):
        return self.factor * value + self.offset

conv = Converter('C', 'F', 1.8, 32)
print('Converting 22C')
#print(str(conv.convert(22)) + conv.units_to)
print('%.2fF' % conv.convert(22))