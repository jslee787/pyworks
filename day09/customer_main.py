from day09.class_lib.customer import Customer
from day09.class_lib.goldcustomer import GoldCustomer
from day09.class_lib.vipcustomer import VipCustomer

c = Customer(101, '놀부')
g = GoldCustomer(201, '흥부')
v = VipCustomer(301, '심청', 1004)

#제품구매
cost_c = c.calc_price(10000)
cost_g = g.calc_price(10000)
cost_v = v.calc_price(20000)

#제품 지불 비용 출력
print(c.getname()+'님의 지불 비용은 ' + str(cost_c) + '원 입니다.')
print(g.getname() + '님의 지불 비용은 ' + str(cost_g) + '원 입니다.')
print(v.getname() + '님의 지불 비용은 ' + str(cost_v) + '원 입니다.')

#객체정보
print(c)
print(g)
print(v)