class Customer:
    def __init__(self, cid, name):
        self.cid = cid
        self.name = name
        self.cgrade = "SILVER"
        self.bonus_point = 0
        self.bonus_ratio = 0.01

    def getname(self):
        return self.name

    def calc_price(self, price):
        self.bonus_point += int(price * self.bonus_ratio)
        return price

    def __str__(self):
        return '{}님의 등급은 {}이고, 보너스 포인트는 {}점 입니다.' \
               ''.format(self.name, self.cgrade, self.bonus_point)