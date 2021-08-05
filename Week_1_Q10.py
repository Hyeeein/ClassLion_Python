# Q10. 입력 받은 string에 대해서 대문자와 소문자 개수를 count하는 코드 작성해보기

def countUpperAndLower(s):
    d = {"UC":0, "LC":0}

    for i in s:
        if (i.isupper() == True):       # 대문자일 경우
            d["UC"] += 1
        elif (i.islower() == True):     # 소문자일 경우
            d["LC"] += 1

    print("Input string:", s)
    print("upper case: ", d["UC"])
    print("lower case: ", d["LC"])

countUpperAndLower("Python is Good")