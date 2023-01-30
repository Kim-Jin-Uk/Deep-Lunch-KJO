import random

rand = random.randint(1,20) / 10
order = 0 if rand < 1 else 1
print('선공 입니다' if rand < 1 else '후공 입니다')

call = 0
count = 0

while call < 31:
    if count % 2 == order:
        size = input('호출할 개수를 입력하세요 : ')
        size = int(size)
        for i in range(size):
            call += 1
            print(f'사용자 : "{call}"')
    else:
        size = random.randint(1, 3)
        for i in range(size):
            call += 1
            print(f'컴퓨터 : "{call}"')
    count += 1

print('사용자의 승리!!' if count % 2 == order else '컴퓨터의 승리!!')