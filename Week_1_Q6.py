# Q6. List의 element가 Tuple일 경우, 마지막 값을 'Tuple'로 바꾸는 코드를 작성해보기
# 튜플을 리스트로 변환하고, 다시 튜플로 변환해서 리스트에 삽입

a = [3, 4, ('a', 5, 'g'), (30, 'b', 'w'), (40, 2, 'd')]

for i in range(0, 5):
    # 리스트의 요소가 튜플형인 경우 (if문)
    if (type(a[i]) == tuple):
        num = len(a[i])        # num = 튜플형의 길이
        lst = list(a[i])       # 튜플형을 리스트형으로 변환
        lst[num - 1] = 'Tuple'    # 마지막 값을 'Tuple'로 변환
        tp = tuple(lst)     # 리스트형을 튜플형으로 변환
        a[i] = tp

print(a)