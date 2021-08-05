# Q7. 주어진 자연수가 짝수인지 홀수인지 판별해주는 함수 만들기

def holjjak(a):
    if (a % 2 == 1):
        print("홀수입니다.")
    else:
        print("짝수입니다.")

a = int(input("자연수를 입력해주세요: "))
holjjak(a)