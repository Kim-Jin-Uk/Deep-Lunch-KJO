# 0은 어쩌지..
def neg_pos_separation_for(arr):
    pos_arr = []
    neg_arr = []
    for value in arr:
        if value > 0:
            pos_arr.append(value)
        else:
            neg_arr.append(value)
    return neg_arr + pos_arr

print(neg_pos_separation_for([-1,1,3,-2,2]))