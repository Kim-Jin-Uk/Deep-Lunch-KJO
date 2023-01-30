import random

rand = random.randint(1,101)
check = 0

print('숫자를 맞춰주세요!')
while True:
    print('1~100 사이 입력: ')
    check = int(input())
    if check == rand: break
    print('DOWN' if rand < check else 'UP')
print('정답입니다!')