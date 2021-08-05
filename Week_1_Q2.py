# Q2. 문자열의 내장함수를 이용하여 a#b#c#d으로 바꿔서 출력해보기

a = "a:b:c:d"
new_a = a.replace(":", "#", 4)  # 문자열.replace("검색 문자", "치환 문자", 치환횟수)
print(new_a)