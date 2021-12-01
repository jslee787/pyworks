from exercise.calculator import Calculator


class MaxLimitCalculator(Calculator):
    def add(self, val):
        if self.value < 100:
            self.value = 100
            
        return self.value

cal = MaxLimitCalculator()
cal.add(50)
cal.add(60)

print(cal.value)