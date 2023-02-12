def get_count_for_first_name(key,arr):
    count = 0
    for name in arr:
        if name[0] == key:
            count += 1
    return count

def get_count_for_full_name(key,arr):
    return arr.count(key)

def make_set_for(arr):
    return list(set(arr))

# 1. 김씨와 이씨는 각각 몇명인가요?
def solution1(param):
    names = param.split(',')
    print('김씨: ', get_count_for_first_name('김',names))
    print('이씨: ', get_count_for_first_name('이',names))

# 2. "이재영"이라는 이름이 몇번 반복되나요?
def solution2(param):
    names = param.split(',')
    print('이재영: ', get_count_for_full_name('이재영',names))

# 3. 중복을 제거한 이름을 출력하세요.
def solution3(param):
    names = param.split(',')
    print('중복 제거: ', ','.join(make_set_for(names)))
    
# 4. 중복을 제거한 이름을 오름차순으로 정렬하여 출력하세요
def solution4(param):
    names = param.split(',')
    print('중복 제거 정렬: ', ','.join(sorted(make_set_for(names))))
    
param = '이유덕,이재영,권종표,이재영,박민호,강상희,이재영,김지완,최승혁,이성연,박영서,박민호,전경헌,송정환,김재성,이유덕,잔경헌'
solution1(param)
solution2(param)
solution3(param)
solution4(param)