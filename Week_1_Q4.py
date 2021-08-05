# Q4. a 리스트에서 중복 숫자 없애기

a = [1, 2, 2, 3, 3, 4, 4, 5, 6, 6, 6, 7]
new_a = []

for num in a:
    if num not in new_a:
        new_a.append(num)
print(new_a)