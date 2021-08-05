# Q9. input 값으로 3,85,24,7,15를 입력 받았을 때 총합을 구하는 코드 작성해보기

a = input("숫자를 입력하세요: ")
b = map(int, a.split(","))  # map(int, list) -> 리스트를 int형으로 변환
result = 0

for i in b:
    result = result + i

print("총합은", result)