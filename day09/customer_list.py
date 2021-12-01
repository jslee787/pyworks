#리스트로 고객 관리하기
from day09.class_lib.customer import Customer
from day09.class_lib.goldcustomer import GoldCustomer
from day09.class_lib.vipcustomer import VipCustomer

customer = [
    Customer(101, '놀부'),
    Customer(102, '팥쥐'),
    GoldCustomer(201, '흥부'),
    GoldCustomer(202, '콩쥐'),
    VipCustomer(301, '심청', 1004)
]

print('***** 구매 가격과 보너스 포인트 계산 *****')
for c in customer:
    cost = c.calc_price(10000)
    print(c.getname() + '님의 지불 금액은 '+ format(cost, ',d') + '원 입니다.')

print('***** 고객 정보 출력 *****')
for i in customer:
    print(i)