# Q8. 다음 리스트에서 60점 이상 점수의 총합을 구해보기

a = [42, 59, 78, 92, 20, 43, 28, 64, 100, 77]
result = 0

for i in a:
    if (i >= 60):
        result = result + i

print("60점 이상 점수의 총합은", result)