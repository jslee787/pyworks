#if 중첩문

num = 13

if num > 10:
    if num % 2 == 0:
        print("10보다 큰 짝수입니다.")
    else:
        print("10보다 큰 홀수 입니다.")
else:
    if num % 2 == 0:
        print("10이하의 짝수입니다.")
    else:
        print("10이하의 홀수 입니다.")

#if ~ elif ~ else문 호환

if num > 10 and num % 2 == 0:
    print("10보다 큰 짝수입니다.")
elif num > 10 and num % 2 != 0:
    print("10보다 큰 홀수 입니다.")
elif num <= 10 and num % 2 == 0:
    print("10이하의 짝수입니다.")
else:
    print("10이하의 홀수 입니다.")
