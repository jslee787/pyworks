#GoldCustomer 클래스 정의
from day09.class_lib.customer import Customer

class GoldCustomer(Customer):
    def __init__(self, cid, name):
        super().__init__(cid, name) #부모멤버상속
        self.cgrade = "GOLD"
        self.sale_ratio = 0.1       #구매할인율 10%
        self.bonus_ratio = 0.02     #보너스 적립 2%

    def calc_price(self, price):
        price = price - int(price * self.sale_ratio)    #할인된 가격 = 가격-(가격*할인율)
        self.bonus_point += int(price * self.bonus_ratio)
        return price

