from day09.class_lib.customer import Customer

class VipCustomer(Customer):
    def __init__(self, cid, name, agent):
        super().__init__(cid, name)
        self.agent = agent          #전문 상담원
        self.cgrade = 'VIP'
        self.sale_ratio = 0.1
        self.bonus_ratio = 0.05

    def calc_price(self, price):
        price = price - int(price * self.sale_ratio)  # 할인된 가격 = 가격-(가격*할인율)
        self.bonus_point += int(price * self.bonus_ratio)
        return price

    def __str__(self):  #부모 정보 상속
        return super().__str__() + '\n전문 상담원 ID는 {}입니다.'.format(self.agent)